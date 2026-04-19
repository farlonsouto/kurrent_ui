FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY conda/environment.yml .
# Note: Using pip here is faster for small UI containers
RUN pip install streamlit requests pillow

# Copy the source code
COPY src/ /app/src/

# Set the working directory to where the script actually lives
WORKDIR /app/src/ui

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "kurrent_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
