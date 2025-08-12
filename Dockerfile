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

# No CMD specified - allows flexible runtime configuration
# Use docker run commands to specify dev vs prod execution mode
