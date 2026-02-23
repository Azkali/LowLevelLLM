from argparse import ArgumentParser

from supercharger.backends.llamaLLM import llamaLLM
from supercharger.backends.xformLLM import xformLLM
from supercharger.llm import LLM
from supercharger.modes.multi_model import multi_model
from supercharger.modes.single_model import single_model


def parser():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", type=str, help="Model name")
    parser.add_argument("-y", "--yaml_file", type=str, help="YAML file")
    parser.add_argument("-j", "--json_file", type=str, help="JSON file")
    return parser.parse_args()


def main(model: str, json_file: str = "", yaml_file: str = "", messages: list = []):
    if yaml_file:
        print(f"Loading YAML file... {yaml_file}")
        multi_model(yaml_file)
    elif json_file and model:
        print(f"Loading JSON file... {json_file}")
        single_model(model, json_file, messages)
    else:
        exit("Please provide either a JSON file AND a valid model name or a YAML file")


def run():
    args = parser()
    main(args.model, args.json_file, args.yaml_file)


if __name__ == "__main__":
    run()
