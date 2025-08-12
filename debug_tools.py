#!/usr/bin/env python3
"""
Debug script to test tools/list with different parameter formats
"""
import json
import requests
import time

BASE_URL = "http://localhost:8000/mcp"

def test_tools_list():
    # First initialize
    init_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize", 
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {"name": "debug-client", "version": "1.0.0"}
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    
    print("Testing initialize...")
    response = requests.post(BASE_URL, json=init_payload, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    
    # Get session ID
    session_id = response.headers.get('mcp-session-id')
    print(f"Session ID: {session_id}")
    
    if not session_id:
        print("No session ID returned!")
        return
    
    # Test different formats for tools/list
    test_cases = [
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/list", "params": {}},
        {"jsonrpc": "2.0", "id": 4, "method": "tools/list", "params": None},
        {"jsonrpc": "2.0", "id": 5, "method": "tools/list", "params": []},
    ]
    
    headers_with_session = {
        **headers,
        "mcp-session-id": session_id
    }
    
    for i, payload in enumerate(test_cases):
        print(f"\nTest case {i+1}: {payload}")
        response = requests.post(BASE_URL, json=payload, headers=headers_with_session)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    test_tools_list()
