FROM docker.io/library/python:3.12.15-slim-trixie@sha256:a0f57064cbdcd6285fa45f51237ab0b35ea8ebaed06a1f5973e89e19dfb86704

# Install uv
RUN pip install --no-cache-dir uv

# Install vicalerts using uv
RUN uv pip install --system vicalerts

# Create a non-root user
RUN useradd -m -u 1000 vicalerts

# Set working directory
WORKDIR /app

# Switch to non-root user
USER vicalerts

# Copy healthcheck script
COPY healthcheck.py /healthcheck.py

# Run vicalerts run with database in mounted volume, polling every 60 seconds (recommended)
CMD ["vicalerts", "run", "--db", "/data/vicalerts.db", "--no-progress", "--interval", "60"]