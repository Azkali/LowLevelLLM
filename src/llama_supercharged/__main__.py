from argparse import ArgumentParser
from .llm import LLM
from .backends.xformLLM import xformLLM

def parser():
    parser = ArgumentParser()
    parser.add_argument("-j", "--json_file", type=str, help="JSON file")
    parser.add_argument("-c", "--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()

if __name__ == "__main__":
    args = parser()

    pt = xformLLM(json_file="examples/prompts/text_xform.json", cache_dir=args.cache_dir)
    print(pt())
    del pt

    pt = xformLLM(json_file="examples/prompts/image_xform.json", cache_dir=args.cache_dir)
    print(pt())
    del pt

    pt = xformLLM(json_file="examples/prompts/video_xform.json", cache_dir=args.cache_dir)
    print(pt())
    del pt
