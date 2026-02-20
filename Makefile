.PHONY: rocm cpu

rocm:
	uv python install 3.13
	uv venv --python 3.13
	CMAKE_ARGS="-DGGML_VULKAN=ON -DGGML_RPC=ON" uv sync --extra rocm
	uv run rocm

cpu:
	uv python install 3.13
	uv venv --python 3.13
	CMAKE_ARGS="-DGGML_METAL=ON -DGGML_RPC=ON" uv sync --extra cpu
	uv run cpu
