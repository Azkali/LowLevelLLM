from argparse import ArgumentParser
from supercharger.multimodel import MultiModel

def multi_model(yaml_file: str):
    multimodel = MultiModel(yaml_file=yaml_file)
    multimodel()
