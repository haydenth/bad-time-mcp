#!/usr/bin/env python3
"""
Simple test script to verify the Bad Time MCP server tools work correctly.
"""

import requests
import json
import subprocess
import threading
import time
import signal
import sys

def test_http_mode():
    """Test the server in HTTP mode."""
    print("🌐 Testing HTTP Mode...")
    
    # Start the server in a subprocess
    server_process = subprocess.Popen([
        sys.executable, "bad_time_mcp.py", "--http", "--port", "8001"
    ])
    
    # Give the server time to start
    time.sleep(2)
    
    try:
        base_url = "http://localhost:8001"
        
        # Test time tool
        print("📅 Testing time tool...")
        time_response = requests.post(f"{base_url}/call", json={
            "tool": "time",
            "arguments": {}
        })
        print(f"Time result: {time_response.json()}")
        
        # Test temperature tool  
        print("🌡️ Testing temperature tool...")
        temp_response = requests.post(f"{base_url}/call", json={
            "tool": "temperature", 
            "arguments": {}
        })
        print(f"Temperature result: {temp_response.json()}")
        
        print("✅ HTTP mode tests passed!")
        
    except Exception as e:
        print(f"❌ HTTP mode test failed: {e}")
    
    finally:
        # Clean up server process
        server_process.terminate()
        server_process.wait()

def test_tools_directly():
    """Test the tools directly by importing the module."""
    print("🔧 Testing tools directly...")
    
    # Import our module
    import bad_time_mcp
    
    # Test time tool multiple times to see variation
    print("📅 Testing time tool (5 calls):")
    for i in range(5):
        result = bad_time_mcp.time()
        print(f"  {i+1}. {result}")
    
    # Test temperature tool multiple times
    print("🌡️ Testing temperature tool (5 calls):")
    for i in range(5):
        result = bad_time_mcp.temperature()
        print(f"  {i+1}. {result}")
    
    print("✅ Direct tool tests completed!")

if __name__ == "__main__":
    print("🚀 Bad Time MCP Server Test Suite")
    print("=" * 40)
    
    # Test tools directly first
    test_tools_directly()
    
    print("\n" + "=" * 40)
    
    # Test HTTP mode
    test_http_mode()
    
    print("\n🎉 All tests completed!")
