FROM python:3.11-slim

WORKDIR /app

# Add dependencies
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl jq \
    && pip install --no-cache-dir -r requirements.txt

# Copy Flask app
COPY src/ .

# Default command for the web service
CMD ["python", "app.py"]
