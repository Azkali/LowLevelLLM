from argparse import ArgumentParser
from llama_supercharged.modes.single_model import single_model
from llama_supercharged.modes.multi_model import multi_model

def parser():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", type=str, help="Model name")
    parser.add_argument("-y", "--yaml_file", type=str, help="YAML file")
    parser.add_argument("-j", "--json_file", type=str, help="JSON file")
    parser.add_argument("-c", "--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()

def main(model: str, json_file: str, yaml_file: str = "", cache_dir: str = "cache", messages: list = []):
    if yaml_file:
        multi_model(yaml_file, cache_dir)
    else:
        single_model(model, json_file, cache_dir, messages)

def run():
    args = parser()
    main(args.model, args.json_file, args.yaml_file, args.cache_dir)


if __name__ == "__main__":
    run()
