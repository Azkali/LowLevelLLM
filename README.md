# Llama Supercharged

Llama supercharged is a Python library that provides a simple interface to the Llama model. It is designed to be easy to use and to provide a high level of performance.

# Building

```sh
# macOS
CMAKE_ARGS="-DGGML_METAL=ON -DGGML_RPC=ON" uv sync --extra cpu

# Linux with Vulkan
CMAKE_ARGS="-DGGML_VULKAN=ON -DGGML_RPC=ON" uv sync --extra rocm
```
