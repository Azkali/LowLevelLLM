import yaml
from llama_supercharged.modes.single_model import single_model

class MultiModel:
    def __init__(self, yaml_file: str, cache_dir: str = "cache"):
        self.yaml_file = yaml_file
        self.cache_dir = cache_dir
        self.model_dir = Path(cache_dir) / "models"
        self.model_dir.mkdir(parents=True, exist_ok=True)
        self.config = self.load_config()

    def __call__(self):
        messages = []
        for step in self.config:
            model = self.config[step].get('model')
            json_file = self.config[step].get('json_file')
            depends_on = self.config[step].get('depends_on', [])

            if self.last_output:
                messages.append({"role": "user", "content": f"Use the output of step {self.last_output} as input."})

            if step == self.config.keys()[0]:
                self.execute_step(step, model, json_file, [], messages=messages)
            else:
                self.execute_step(step, model, json_file, depends_on, messages=messages)

    def execute_step(self, step: str, model: str, json_file: str, depends_on: list = [], messages: list = []):
        print(f"Executing step {step} with model {model} and dependencies {depends_on}")
        self.last_output = single_model(model=model, json_file=json_file, cache_dir=self.cache_dir, messages=messages)

    def load_config(self):
        with open(self.yaml_file, 'r') as file:
            return yaml.safe_load(file)
