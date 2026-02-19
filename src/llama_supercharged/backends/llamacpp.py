from llama_supercharged.llm import LLM
from llama_cpp import Llama, llama_chat_format as chat_formats
from typing import override

# L1JSON/redJSON -> llamaLLM inflation:
# params         -> model                     load parameters.
# prompt         -> model                     generation parameters.
# data           -> model                     generation messages.

##########################################################
#つづ: break down generation into lower-level components.#
#      also reconsider just switching bindings. ＿|￣|○  #
#                                                        #
#      replicate xform's mtype mechanism (see printing)  #
##########################################################

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

        return output # probably won't work.
        # ^ didn't, but for other reasons (concatenates during print).
        # v this doesn't expose as much data as it should, but it's fine for now.
        #return output["choices"][0]["message"]["content"]
        # ignore all above. line 24 was the issue.

    def _load_model(self):
        self.model = Llama.from_pretrained(**self.params, local_dir=self.cache_dir)

    # should i not define this function?
    # that would call the super one, right?
    # but i think i'll leave it since it'll be used in the future.
    # and i think i'll leave it because the comments are there.
    # ^ i wrote a poem haha.
    def _load_data(self):
        super()._load_data()

        # PPD -> P1
        # read 4 lines ahead.
        # PPD -> P2
        # read 2 lines ahead.
        # PPD -> D
        # (no actionable that is necessary.)
