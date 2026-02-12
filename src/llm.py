import json
import argparse
from llama_cpp import Llama
from typing import Optional, List

# Parametrized model instance
# repo_id -> str: model repo id
# model -> str: model path
# prompt -> str: prompt text
# instruction -> str: instruction text
# cache_dir -> str: cache directory
# rpc_servers -> Optional[List[str]]: rpc servers
# tensor_split -> Optional[List[float]]: tensor split
# **kwargs: additional parameters dict
class Llm:
    def __init__(
            self,
            repo_id: str,
            model: str,
            json_path: str,
            instruction: str,
            cache_dir: str = "cache",
            rpc_servers: Optional[List[str]] = None,
            tensor_split: Optional[List[float]] = None,
            **kwargs):
        self.model = model
        self.prompt = self.load_prompt_json()
        self.repo_id = repo_id
        self.instruction = instruction
        self.local_dir = cache_dir + "/models/"
        self.model_path = self.local_dir + self.model
        self.tensor_split = [0.2, 0.8]
        self.rpc_servers = [
            "192.168.1.124:50052",
            "0.0.0.0:50052"
        ]

    def run(self):
        self.llm = Llama(
            model_path=self.model_path,
            n_gpu_layers=-1,
            rpc_servers=self.rpc_servers,
            tensor_split=self.tensor_split,
            **kwargs
        )

    def prompt(self):
        self.last_prompt = self.llm(
            prompt=self.prompt,
            max_tokens=None,
            stop=["Q:", "\n"],
            echo=True
        )

    def download_model(self):
        Llama.from_pretrained(
            repo_id=self.repo_id,
            filename=self.model,
            local_dir=self.local_dir
        )

    def load_prompt_json(self):
        with open(self.prompt_json_path, 'r') as f:
            return json.load(f)
