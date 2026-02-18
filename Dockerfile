
FROM rocm/pytorch:latest

# Install uv
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        curl \
        libvulkan-dev \
        glslc
RUN pip install uv

# Install the package
COPY . /app
WORKDIR /app

# Run the development server
CMD ["bash", "entrypoint.sh"]
