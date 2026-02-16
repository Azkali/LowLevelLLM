from .llm import LLM
from llama_cpp import Llama, llama_chat_format as chat_formats

FORMATS = {
    name: obj
    for name, obj in vars(chat_formats).items()
    if isinstance(obj, type)
}

class LlamaLLM(LLM):
    def __init__(self, json_file: str, cache_dir: str = "cache"):
        super().__init__(json_file, cache_dir)
        self.llm = Llama(**self._set_params())

    def callback(self, response):
        return self.llm(prompt=self.instruction, **self.prompt_args)

    def _handle_chat_completion(self):
        return self.llm.create_chat_completion(self.data["chat_completion"])

    def download_model(self, **kwargs):
        return Llama.from_pretrained(local_dir=str(self.model_dir), **kwargs)


class LlamaCPPMultiModal(LlamaLLM):
    def _handle_chat_format(self):
        if self.fmt is None or self.fmt not in FORMATS:
            print("Missing or invalid format")
            return None
        if self.fmt != "audio" and not self.clip_path:
            print("Missing clip model path")
            return None
        return FORMATS[self.fmt](clip_model_path=self.clip_path)

    def _set_params(self):
        return {"chat_handler": self._handle_chat_format(), **self.params}


class AutoLlamaType(LlamaLLM):
    def callback(self):
        if (self.data.get("capabilities") == "text"):
            run = LlamaLLM(json_file, cache_dir)
        elif (self.data.get("capabilities") == "video"):
            run = LlamaCPPMultiModal(json_file, cache_dir)
        else:
            raise ValueError("Invalid chat format")
        return run.callback()
