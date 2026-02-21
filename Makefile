.PHONY: vulkan metal cpu setup

PYTHON_VERSION := 3.13

setup:
	uv python install $(PYTHON_VERSION)
	uv venv --python $(PYTHON_VERSION)

define run_backend
	CMAKE_ARGS="$(1)" uv sync
	uv run dev
endef

vulkan: setup
	$(call run_backend,-DGGML_VULKAN=ON -DGGML_RPC=ON)

metal: setup
	$(call run_backend,-DGGML_METAL=ON -DGGML_RPC=ON)

cpu: setup
	$(call run_backend,-DGGML_RPC=ON)
