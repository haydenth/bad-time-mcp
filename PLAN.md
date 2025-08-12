# Bad Time MCP - Development Plan

This document outlines the development plan for the Bad Time MCP server, a test service built with FastMCP that provides intentionally unreliable tools for testing purposes.

## Project Overview

**Goal**: Create a Python-based MCP server that can run both as a CLI tool and HTTP service, providing two "bad" tools for testing error handling and resilience in MCP clients.

**Target Features**:
- `time` tool - returns incorrect timestamps
- `temperature` tool - returns random temperatures (0-100°F)
- Dual mode: CLI and HTTP server
- Docker support
- Goose CLI integration

## Phase 1: Core Implementation 🚀

### 1.1 Main Server Implementation
- [ ] Create `bad_time_mcp.py` with FastMCP server setup
- [ ] Implement `time` tool with incorrect timestamp generation
- [ ] Implement `temperature` tool with random temperature (0-100°F)
- [ ] Add command-line argument parsing for mode selection
- [ ] Basic error handling and logging

### 1.2 Project Structure Setup
- [ ] Create `requirements.txt` with FastMCP and dependencies
- [ ] Set up proper Python package structure
- [ ] Create basic `.gitignore` for Python projects
- [ ] Add development dependencies (pytest, black, etc.)

**Deliverables**: Working MCP server with both tools functional

## Phase 2: Dual Mode Support 🔄

### 2.1 CLI Mode Implementation
- [ ] Standard MCP protocol over stdin/stdout
- [ ] JSON-RPC message handling
- [ ] Proper MCP handshake and capability negotiation
- [ ] Tool discovery and execution

### 2.2 HTTP Server Mode
- [ ] HTTP-based MCP protocol support
- [ ] RESTful API endpoints for MCP operations
- [ ] Proper HTTP status codes and error responses
- [ ] CORS support for web clients

**Deliverables**: Server can operate in both CLI and HTTP modes

## Phase 3: Containerization 🐳

### 3.1 Docker Setup
- [ ] Create `Dockerfile` with multi-stage build
- [ ] Expose appropriate ports (default: 8000)
- [ ] Add health check endpoints
- [ ] Proper signal handling for graceful shutdown

### 3.2 Container Orchestration
- [ ] Create `docker-compose.yml` for development
- [ ] Add environment variable configuration
- [ ] Volume mounts for development mode
- [ ] Network configuration for service discovery

**Deliverables**: Fully containerized application ready for deployment

## Phase 4: Goose CLI Integration 🪿

### 4.1 Research Integration Patterns
- [ ] Examine `/home/tom/projects/goose` for MCP integration examples
- [ ] Document Goose MCP server configuration methods
- [ ] Understand connection protocols and message formats

### 4.2 Integration Documentation
- [ ] Create step-by-step integration guides for each mode:
  - Local binary execution
  - HTTP server connection
  - Docker container connection
- [ ] Add troubleshooting section
- [ ] Create example configuration files

### 4.3 Testing Integration
- [ ] Test local binary mode with Goose CLI
- [ ] Test HTTP server mode with Goose CLI
- [ ] Test Docker mode with Goose CLI
- [ ] Document any compatibility issues

**Deliverables**: Complete integration guide and tested compatibility

## Phase 5: Testing & Polish ✨

### 5.1 Test Suite Development
- [ ] Unit tests for both `time` and `temperature` tools
- [ ] Integration tests for MCP protocol compliance
- [ ] HTTP API endpoint tests
- [ ] Docker container functionality tests
- [ ] End-to-end tests with real MCP clients

### 5.2 Development Tooling
- [ ] Add pre-commit hooks for code quality
- [ ] Set up linting with flake8/black
- [ ] Add type hints and mypy checking
- [ ] Create development scripts (`make` or `scripts/`)

### 5.3 Documentation Polish
- [ ] Add code examples to README
- [ ] Create API documentation
- [ ] Add troubleshooting guides
- [ ] Include performance considerations

**Deliverables**: Production-ready codebase with comprehensive testing

## Technical Decisions & Implementation Details

### "Bad" Behavior Design

#### Time Tool Options:
1. **Random Offset**: Add/subtract random hours/days from current time
2. **Fixed Wrong Timezone**: Always return time in wrong timezone
3. **Completely Random**: Generate random timestamps within a range
4. **Mixed Strategies**: Randomly choose between different "bad" behaviors

**Recommendation**: Start with random offset (±1-30 days) for predictable badness

#### Temperature Tool:
- Simple random integer generation (0-100)
- Consider adding occasional out-of-range values for extra "badness"
- Could add random units (Celsius when Fahrenheit expected)

### HTTP API Design

**Option A**: Pure MCP-over-HTTP
- Maintain exact MCP protocol over HTTP transport
- Single endpoint accepting JSON-RPC messages

**Option B**: RESTful MCP Wrapper  
- `/tools` - GET for tool discovery
- `/tools/{name}` - POST for tool execution
- More HTTP-native but diverges from MCP standard

**Recommendation**: Option A for MCP compliance, with Option B as stretch goal

### Configuration Strategy

```yaml
# config.yaml example
badness_level: medium
time_tool:
  strategy: random_offset
  max_offset_days: 30
temperature_tool:
  min_temp: 0
  max_temp: 100
  occasional_outliers: true
```

## Success Criteria

- [ ] Both tools work reliably in their "unreliable" way
- [ ] Server runs stably in both CLI and HTTP modes
- [ ] Docker container builds and runs successfully
- [ ] Successful integration with Goose CLI in all modes
- [ ] Comprehensive test coverage (>80%)
- [ ] Clear documentation for setup and usage

## Timeline Estimate

- **Phase 1**: 2-3 days
- **Phase 2**: 2-3 days  
- **Phase 3**: 1-2 days
- **Phase 4**: 2-3 days (depends on Goose research)
- **Phase 5**: 2-3 days

**Total Estimated Time**: 9-14 days

## Next Steps

1. Start with Phase 1.1 - implement the core MCP server with both tools
2. Test basic functionality before moving to dual-mode support
3. Iterate quickly and test integration points early
4. Document discoveries and decisions as we go

## Questions for Resolution

1. How "bad" should the tools be? (fail occasionally vs. just wrong data)
2. Should we support configuration files for different badness levels?
3. Any specific Goose CLI integration requirements beyond basic MCP support?
4. Are there other "bad" tools we should consider adding?
