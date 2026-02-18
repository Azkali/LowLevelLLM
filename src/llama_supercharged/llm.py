import json
from pathlib import Path

# Parametrized model instance
# json_file -> str: json path
# cache_dir -> str: cache directory path
class LLM:
    def __init__(self, json_file: str, cache_dir: str = "cache", **kwargs):
        self.additionals = kwargs
        self.json_file = json_file
        self.cache_dir = cache_dir
        self.model_dir = Path(cache_dir) / "models"
        self.model_dir.mkdir(parents=True, exist_ok=True)
        self._load_data()

    def __call__(self):
        self.callback()

    def callback(self):
        pass

    def _load_data(self):
        with open(self.json_file, 'r', encoding="utf-8") as f:
            self.data = json.load(f)

        self.fmt = self.data.get("format", "text")
        self.params = self.data.get("params")
        self.prompt = self.data.get("prompt")
        self.instruction = self.data.get("instruction")
        self.clip_path = self.data.get("clip_model_path", None)

    def _set_params(self):
        return {**self.params, **self.additionals}
