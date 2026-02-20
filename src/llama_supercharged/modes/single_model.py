from llama_supercharged.llm import LLM
from llama_supercharged.backends import *

def single_model(model: str, json_file: str, messages: list = []):
    backend_class = globals().get(model)
    if backend_class is None:
        raise ValueError(f"Backend class '{model}' not found. Available: {', '.join([k for k in globals() if not k.startswith('__')])}")

    if not messages:
        backend = backend_class(json_file=json_file)
    else:
        backend = backend_class(json_file=json_file, messages=messages)

    print(f"Using backend: {backend_class.__name__}")
    backend()
