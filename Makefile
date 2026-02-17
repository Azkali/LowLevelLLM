# user settings. change these if you fail to install (because, for example, you have a very complex environment).
PYTHON ?= python3
PIP := $(PYTHON) -m pip

# build flags. change these if you want to change sub-library behaviour.
CMAKE_FLAGS ?= "-DGGML_VULKAN=ON -DGGML_RPC=ON"

#################### STOP!

export CMAKE_ARGS="$(CMAKE_FLAGS)"

install:
	@echo "installing with configured flags (${CMAKE_ARGS}) in normal mode..."
	@$(PIP) install --upgrade .

dev:
	@echo "installing with configured flags (${CMAKE_ARGS}) in editable mode..."
	@$(PIP) install --upgrade -e .

uninstall:
	@echo "uninstalling..."
	@$(PIP) uninstall llama_supercharged -y

spring-clean: uninstall
	@echo "spring-cleaning the environment..."
	@$(PIP) cache purge
	@rm -rf src/*.egg-info
	@find src/ -name "__pycache__" -exec rm -rf {} +

.PHONY: install install-dev uninstall spring-clean
