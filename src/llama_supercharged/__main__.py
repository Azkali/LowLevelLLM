from argparse import ArgumentParser
from .llm import LLM

def parser():
    parser = ArgumentParser()
    parser.add_argument("-j", "--json", type=str, help="JSON file")
    parser.add_argument("-c", "--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()

if __name__ == "__main__":
    args = parser()
    pt = LLM(json=args.json, cache_dir=args.cache_dir)
    pt()
