import llama_supercharged.TRLog as TRLog
from llama_supercharged.llm import LLM
from llama_supercharged.backends.llamaLLM import llamaLLM
from llama_supercharged.backends.xformLLM import xformLLM
from llama_supercharged.modes.single_model import single_model
from llama_supercharged.modes.multi_model import multi_model
import logging
from argparse import ArgumentParser

TRLog.setup()
logger = logging.getLogger("lib.INIT")
logger.info("SUPERCHARGER is up.")

def parser():
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", type=str, help="Model name")
    parser.add_argument("-y", "--yaml_file", type=str, help="YAML file")
    parser.add_argument("-j", "--json_file", type=str, help="JSON file")
    return parser.parse_args()

def main(model: str, json_file: str = "", yaml_file: str = "", messages: list = []):
    if yaml_file:
        logger.info(f"initializing using YAML... ({yaml_file})")
        multi_model(yaml_file)
    elif json_file and model:
        logger.info(f"initializing using JSON... ({json_file})")
        single_model(model, json_file, messages)
    else:
        logger.critical("please provide either a JSON file and model name, or a YAML file.")
        exit()

def run():
    args = parser()
    main(args.model, args.json_file, args.yaml_file)

if __name__ == "__main__":
    run()
