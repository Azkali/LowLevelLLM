import json
from pathlib import Path
from llama_cpp import Llama
from llama_cpp import llama_chat_format as chat_formats

FORMATS = {
    name: obj
    for name, obj in vars(chat_formats).items()
    if isinstance(obj, type)
}

# Parametrized model instance
# json -> str: json path
# cache_dir -> str: cache directory path
class LLM:
    def __init__(self, json_file: str, cache_dir: str = "cache"):
        self.model_dir = Path(cache_dir) / "models"
        self.model_dir.mkdir(parents=True, exist_ok=True)

        self._load_json(json_file)
        self.llm = Llama(**self._set_params())

    def __call__(self):
        instruction = self.data.get("instruction", "")
        prompt_args = self.data.get("prompt", {})
        return self.llm(prompt=instruction, **prompt_args)

    def _load_json(self, json_file: str):
        with open(json_file, 'r', encoding="utf-8") as f:
            self.data = json.load(f)

        self.data.setdefault("params", {})
        self.data.setdefault("prompt", {})

    def _handle_chat_format(self):
        fmt = self.data.get("format")
        clip_path = self.data.get("clip_model_path")

        if fmt and clip_path and fmt in FORMATS:
            return FORMATS[fmt](clip_model_path=clip_path)

        return None

    def _set_params(self):
        chat_handler = self.__handle_chat_format()
        params = self.data.get("params", {})
        return {"chat_handler": chat_handler, **params}

    def download_model(self, **kwargs):
        return Llama.from_pretrained(local_dir=str(self.model_dir), **kwargs)
