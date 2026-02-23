import json


# Parametrized model instance
# json_file -> str: json path
class LLM:
    def __init__(self, json_file: str):
        self.load_data(json_file)

    def __call__(self):
        self.callback()

    def callback(self):
        pass

    def load_data(self, json_file: str):
        with open(json_file, "r", encoding="utf-8") as f:
            self.l1json = json.load(f)

    def _load_data(self):
        # L1JSON/redJSON structure.
        self.params = self.l1json.get("params")  # PPD -> P1
        self.prompt = self.l1json.get("prompt")  # PPD -> P2
        self.data = self.l1json.get("data")  # PPD -> D
