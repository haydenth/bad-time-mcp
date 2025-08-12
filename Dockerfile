# Use latest Python image as base
FROM python:latest

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY bad_time_mcp.py .

# Expose port 8000 (standard FastAPI/Uvicorn port)
EXPOSE 8000

# Run the server with Uvicorn when container starts
# Using the FastMCP app from bad_time_mcp.py
CMD ["uvicorn", "bad_time_mcp:mcp.app", "--host", "0.0.0.0", "--port", "8000"]
