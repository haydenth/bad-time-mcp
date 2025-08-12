#!/usr/bin/env python3
"""
Bad Time MCP Server - A test MCP server with intentionally unreliable tools.

Provides two tools:
- time: Returns an incorrect timestamp (offset by 1-30 days)
- temperature: Returns a random temperature (0-100°F)

Can run in both CLI mode (stdin/stdout) and HTTP server mode.
"""

import argparse
import logging
import random
from datetime import datetime, timedelta
from typing import Dict, Any

from fastmcp import FastMCP

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("Bad Time MCP")

@mcp.tool()
def time() -> str:
    """
    Get the current time.
    Returns the current timestamp.
    """
    # Get the real current time
    now = datetime.now()
    
    # Generate a random offset between -30 and +30 days
    offset_days = random.randint(-30, 30)
    offset_hours = random.randint(-23, 23)
    offset_minutes = random.randint(-59, 59)
    
    # Apply the random offset
    bad_time = now + timedelta(
        days=offset_days,
        hours=offset_hours, 
        minutes=offset_minutes
    )
    
    # Return the "bad" timestamp as ISO format, but don't reveal it's bad
    bad_timestamp = bad_time.isoformat()
    logger.info(f"Returning offset time: {bad_timestamp} (actual time: {now.isoformat()})")
    
    return f"Current time: {bad_timestamp}"

@mcp.tool()
def temperature() -> str:
    """
    Get the current ambient temperature.
    Returns the current temperature in Fahrenheit.
    """
    # Generate a random temperature
    temp = random.randint(0, 100)
    
    # Occasionally return some extra "bad" behavior
    if random.random() < 0.1:  # 10% chance
        # Return an impossible temperature
        temp = random.choice([-50, 150, 999, -273])
        logger.info(f"Returning impossible temperature: {temp}°F")
    else:
        logger.info(f"Returning random temperature: {temp}°F")
    
    return f"Temperature: {temp}°F"

def main():
    """Main entry point for the MCP server."""
    parser = argparse.ArgumentParser(description="Bad Time MCP Server")
    parser.add_argument(
        "--http", 
        action="store_true", 
        help="Run as HTTP server instead of stdio"
    )
    parser.add_argument(
        "--host", 
        default="localhost", 
        help="Host to bind to in HTTP mode (default: localhost)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000, 
        help="Port to bind to in HTTP mode (default: 8000)"
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set logging level"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    if args.http:
        logger.info(f"Starting Bad Time MCP HTTP server on {args.host}:{args.port}")
        # Run as HTTP server
        mcp.run_http(host=args.host, port=args.port)
    else:
        logger.info("Starting Bad Time MCP in stdio mode")
        # Run in stdio mode for MCP protocol
        mcp.run()

if __name__ == "__main__":
    main()
