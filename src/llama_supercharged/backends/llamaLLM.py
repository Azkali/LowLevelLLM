from llama_supercharged.llm import LLM
from typing import override

# L1JSON/redJSON -> llamaLLM inflation:
# params         -> model                     load parameters.
# prompt         -> model                     generation parameters.
# data           -> model                     generation messages.

#################################################
#TODO: switch "back back end" to something else.#
#################################################

class llamaLLM(LLM):
    @override
    def callback(self):
        sendback = "llamaLLM back end does not currently have a \"back back end\"."
        print(sendback)
        return sendback
