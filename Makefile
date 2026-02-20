.PHONY: rocm metal cpu

rocm:
	uv python install 3.13
	uv venv --python 3.13
	CMAKE_ARGS="-DGGML_VULKAN=ON -DGGML_RPC=ON" uv sync --extra rocm
	uv run rocm

metal:
	uv python install 3.13
	uv venv --python 3.13
	CMAKE_ARGS="-DGGML_METAL=ON -DGGML_RPC=ON" uv sync --extra metal
	uv run metal

cpu:
	uv python install 3.13
	uv venv --python 3.13
	CMAKE_ARGS="-DGGML_RPC=ON" uv sync --extra cpu
	uv run cpu
