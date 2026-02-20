from argparse import ArgumentParser
from llama_supercharged.multimodel import MultiModel

def multi_model(yaml_file: str):
    multimodel = MultiModel(yaml_file=yaml_file)
    multimodel()
