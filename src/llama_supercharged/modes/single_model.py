from llama_supercharged.llm import LLM
from llama_supercharged.backends.llamaLLM import *

def single_model(model: str, json_file: str, cache_dir: str = "cache", messages: list = []):
    backend_class = globals().get(model)
    if backend_class is None:
        raise ValueError(f"Backend class '{model}' not found. Available: {', '.join([k for k in globals() if not k.startswith('__')])}")

    if not messages:
        backend = backend_class(json_file=json_file, cache_dir=cache_dir)
    else:
        backend = backend_class(json_file=json_file, cache_dir=cache_dir, messages=messages)

    print(f"Using backend: {backend_class.__name__}")
    backend()

def main(model: str, json_file: str, yaml_file: str = "", cache_dir: str = "cache", messages: list = []):
    if yaml_file:
        multi_model(yaml_file, cache_dir)
    else:
        single_model(model, json_file, cache_dir, messages)
