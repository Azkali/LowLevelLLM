#!/bin/bash
uv python install 3.13
uv venv --python 3.13
uv sync --extra rocm
source .venv/bin/activate
uv run dev
