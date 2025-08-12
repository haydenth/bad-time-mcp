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

The server can be containerized and deployed as a Docker service using Uvicorn.

**Build the Docker image:**

```bash
docker build -t bad-time-mcp .
```

**Run as HTTP service:**

```bash
docker run -p 8000:8000 bad-time-mcp
```

The containerized server will automatically start with Uvicorn and be available at `http://localhost:8000`.

**Docker Configuration Details:**

- **Base Image**: `python:latest`
- **Server**: Uvicorn ASGI server (optimal for FastAPI/FastMCP)
- **Port**: Exposes port 8000
- **Startup Command**: `uvicorn bad_time_mcp:mcp.app --host 0.0.0.0 --port 8000`

**Production Deployment:**

For production environments, consider:

1. **Reverse Proxy Setup:**
   ```bash
   # Example with nginx reverse proxy
   docker run -d --name bad-time-mcp -p 8000:8000 bad-time-mcp
   # Configure nginx to proxy to localhost:8000
   ```

2. **Multiple Workers:**
   ```bash
   # Build custom image with gunicorn + uvicorn workers
   CMD ["gunicorn", "bad_time_mcp:mcp.app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
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

To integrate Bad Time MCP with the Goose CLI tool:

1. **Local Binary Mode:**
   ```bash
   # Add to your Goose configuration
   goose --mcp-server "python /path/to/bad-time-mcp.py"
   ```

2. **HTTP Server Mode:**
   ```bash
   # Start the HTTP server
   python bad_time_mcp.py --http
   
   # Configure Goose to connect to HTTP endpoint
   goose --mcp-server "http://localhost:8000"
   ```

3. **Docker Mode:**
   ```bash
   # Run containerized server
   docker run -p 8000:8000 bad-time-mcp
   
   # Connect Goose to containerized service
   goose --mcp-server "http://localhost:8000"
   ```

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
