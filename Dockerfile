FROM python:3.11-slim

# Install system dependencies including Tesseract
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-eng \
    tesseract-ocr-all \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

# Expose the port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import socket; socket.create_connection(('localhost', 8000), timeout=5)" || exit 1

# Run Daphne for both WebSockets and HTTP
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "padlevb.asgi:application"]