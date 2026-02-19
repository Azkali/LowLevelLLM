from llama_supercharged.llm import LLM
from llama_cpp import Llama
from typing import override

# L1JSON/redJSON -> llamaLLM inflation:
# params         -> model                     load parameters.
# prompt         -> model                     generation parameters.
# data           -> model                     generation messages.

#################################################
#TODO: switch "back back end" to something else.#
#################################################

class LlamaLLM(LLM):
    def __init__(self, json_file: str, cache_dir: str = "cache", **kwargs):
        super().__init__(json_file, cache_dir)
        self._load_data()
        self._load_model()

    @override
    def callback(self):
        output = self.model.create_chat_completion(**self.data, **self.prompt, stream=True)

        for token in output:
            delta = token["choices"][0].get("delta", {})
            content = delta.get("content", {})
            print(content, end="", flush=True)

        return output

    def _load_model(self):
        self.model = Llama.from_pretrained(**self.params, local_dir=self.cache_dir)
