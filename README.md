# Bad Time MCP

![You're gonna have a bad time](bad_time_meme.jpg)

A test MCP (Model Context Protocol) server implementation in Python that provides intentionally unreliable tools for testing and demonstration purposes.

## Overview

Bad Time MCP is a Python-based MCP server built with FastMCP that provides two deliberately "bad" tools:

- **`time`** - Returns an incorrect timestamp (useful for testing error handling)
- **`temperature`** - Returns a random temperature between 0-100°F

This server can be run both as a command-line binary and as an HTTP service, making it flexible for different testing scenarios.

## Features

- **Dual Mode Operation**: Supports both CLI and HTTP server modes
- **Docker Support**: Can be containerized for easy deployment
- **FastMCP Integration**: Built using the FastMCP Python framework
- **Testing-Focused**: Designed to provide unreliable responses for robust testing
- **Goose CLI Integration**: Can be integrated with the Goose CLI tool

## Installation

### Prerequisites

- Python 3.8+
- pip

### Install Dependencies

```bash
pip install fastmcp
```

## Usage

### Command Line Mode

```bash
python bad_time_mcp.py
```

### HTTP Server Mode

```bash
python bad_time_mcp.py --http
```

### Docker Usage

The Dockerfile builds a container image but doesn't specify a default command, allowing flexible runtime configuration for development vs production deployments.

**Build the Docker image:**

```bash
docker build -t bad-time-mcp .
```

**Development Mode (using FastMCP's built-in HTTP server):**

```bash
# Run in development mode using the Python script's --http flag
docker run -p 8000:8000 bad-time-mcp python bad_time_mcp.py --http --host 0.0.0.0 --port 8000
```

**Production Mode (using Uvicorn directly):**

```bash
# Run in production mode using Uvicorn directly for better performance
docker run -p 8000:8000 bad-time-mcp uvicorn bad_time_mcp:app.http_app --host 0.0.0.0 --port 8000
```

**Docker Configuration Details:**

- **Base Image**: `python:latest`
- **Port**: Exposes port 8000
- **Flexible Command**: No default CMD - specify at runtime
- **Dev Mode**: Uses FastMCP's built-in HTTP server (`python bad_time_mcp.py --http`)
- **Prod Mode**: Uses Uvicorn ASGI server directly (`uvicorn bad_time_mcp:app.http_app`)

**Production Deployment Options:**

1. **Background Service:**
   ```bash
   # Run as detached service in production mode
   docker run -d --name bad-time-mcp -p 8000:8000 bad-time-mcp \
     uvicorn bad_time_mcp:app.http_app --host 0.0.0.0 --port 8000
   ```

2. **With Multiple Workers (for high load):**
   ```bash
   # Use Gunicorn with Uvicorn workers for production scale
   docker run -p 8000:8000 bad-time-mcp \
     gunicorn bad_time_mcp:app.http_app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

## Available Tools

### `time`

Returns an intentionally incorrect timestamp.

**Usage:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "time"
  }
}
```

**Returns:**
- An incorrect timestamp string

### `temperature`

Returns a random temperature reading.

**Usage:**
```json
{
  "method": "tools/call",
  "params": {
    "name": "temperature"
  }
}
```

**Returns:**
- A random integer between 0-100 (representing degrees Fahrenheit)

## Integration with Goose CLI

This MCP server can be integrated with the Goose CLI tool for testing purposes. See the [Goose CLI Integration Guide](#goose-cli-integration) below.

### Goose CLI Integration

To integrate Bad Time MCP with the Goose CLI tool, use the appropriate extension flags:

1. **Local Binary Mode:**
   ```bash
   # Connect to local MCP server binary
   goose session --with-extension 'python /home/tom/projects/bad-time-mcp/bad_time_mcp.py'
   ```

2. **HTTP Server Mode:**
   ```bash
   # Start the HTTP server
   python bad_time_mcp.py --http
   
   # Connect Goose to HTTP MCP server
   goose session --with-remote-extension 'http://localhost:8000'
   ```

3. **Docker Mode:**
   ```bash
   # Run containerized server
   docker run -p 8000:8000 bad-time-mcp
   
   # Connect Goose to containerized MCP service
   goose session --with-remote-extension 'http://localhost:8000'
   ```

4. **Alternative HTTP Connection (for streamable extensions):**
   ```bash
   # If the above doesn't work, try streamable HTTP extensions
   goose session --with-streamable-http-extension 'http://localhost:8000'
   ```

#### Goose CLI Extension Options Explained

- `--with-extension` - For stdio-based MCP servers (command-line executables)
- `--with-remote-extension` - For HTTP-based MCP servers  
- `--with-streamable-http-extension` - For streamable HTTP MCP servers
- `--with-builtin` - For bundled Goose extensions (not applicable here)

## Development

### Project Structure

```
bad-time-mcp/
├── README.md
├── .goosehints
├── bad_time_mcp.py       # Main server implementation
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
└── tests/              # Test suite
```

### Testing

The server is designed to provide unreliable responses, making it perfect for testing error handling and resilience in MCP clients.

## Contributing

This is a test service designed for development and testing purposes. Contributions are welcome, especially those that add more "bad" behaviors for comprehensive testing scenarios.

## License

NO LICENSE. YOLO FOREVER.

## Related Projects

- [Goose CLI](https://github.com/block/goose) - The AI agent CLI tool that can integrate with this MCP server
- [FastMCP](https://github.com/jlowin/fastmcp) - The Python framework used to build this server
