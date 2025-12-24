# Use official Rasa image (with all dependencies)
FROM rasa/rasa:3.6.21-full

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install Rasa SDK for custom actions with proper permissions
USER root
RUN pip install rasa-sdk==3.6.0
USER 1001

# Expose Rasa and action server ports
EXPOSE 5005
EXPOSE 5055

# Default command: run Rasa server with API
CMD ["sh", "-c", "rasa run --enable-api --cors '*' --port 5006"]
