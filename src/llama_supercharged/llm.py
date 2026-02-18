import json
from pathlib import Path

# Parametrized model instance
# json_file -> str: json path
# cache_dir -> str: cache directory path
class LLM:
    def __init__(self, json_file: str, cache_dir: str = "cache"):
        self.cache_dir = cache_dir
        self.model_dir = Path(cache_dir) / "models"
        self.load_data(json_file)

    def __call__(self):
        self.callback()

    def callback(self):
        pass

    # rename to load_redjson?
    def load_data(self, json_file: str):
        with open(json_file, 'r', encoding="utf-8") as f:
            self.redjson = json.load(f)

    def _load_data(self):
        # redJSON structure.
        self.params = self.redjson.get("params")
        self.prompt = self.redjson.get("prompt")
        self.data = self.redjson.get("data")
