from argparse import ArgumentParser
from llama_supercharged.llm import LLM
from llama_supercharged.backends.llamacpp import *
from llama_supercharged.generator import Generator

def parser():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", type=str, help="Model name")
    parser.add_argument("-y", "--yaml_file", type=str, help="YAML file")
    parser.add_argument("-j", "--json_file", type=str, help="JSON file")
    parser.add_argument("-c", "--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()

def main(model: str, json_file: str, yaml_file: str = "", cache_dir: str = "cache", messages: list = []):
    if yaml_file:
        generator = Generator(yaml_file=yaml_file, cache_dir=cache_dir)
        generator()

    backend_class = globals().get(model)
    if backend_class is None:
        raise ValueError(f"Backend class '{model}' not found. Available: {', '.join([k for k in globals() if not k.startswith('__')])}")

    if not messages:
        backend = backend_class(json_file=json_file, cache_dir=cache_dir)
    else:
        backend = backend_class(json_file=json_file, cache_dir=cache_dir, messages=messages)

    print(f"Using backend: {backend_class.__name__}")
    backend()
