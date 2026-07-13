# Use a lightweight python image
FROM python:3.9-slim

# Install system dependencies needed for OpenCV, PyTorch, and git
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Copy requirements_deploy.txt first to leverage Docker cache
COPY requirements_deploy.txt requirements.txt

# Install dependencies.
# We fetch CPU-only PyTorch and torchvision to keep the image small.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Ensure static/ directory exists and has write permissions for saving uploaded images
RUN mkdir -p static && chmod -R 777 static

# Expose the default Hugging Face Spaces port
EXPOSE 7860

# Run the Flask app
CMD ["python", "app.py"]
