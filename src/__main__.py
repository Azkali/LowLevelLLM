from argparse import ArgumentParser
from llama_supercharged.src.llm import Llm

def parser():
    parser = ArgumentParser()
    parser.add_argument("-r", "--repo_id", type=str, help="repo id")
    parser.add_argument("-m", "--model", type=str, help="model name")
    parser.add_argument("-p", "--prompt", type=str, help="prompt")
    parser.add_argument("-i", "--instruction", type=str, help="instruction")
    parser.add_argument("-s", "--rpc_servers", type=str, nargs="+", help="RPC servers")
    parser.add_argument("-t", "--tensor_split", type=float, nargs="+", help="Tensor split")
    parser.add_argument("-c", "--cache_dir", type=str, default="cache", help="Cache directory")
    return parser.parse_args()

if __name__ == "__main__":
    args = parser()
    pt = Llm(
        repo_id=args.repo_id,
        model=args.model,
        prompt=args.prompt,
        instruction=args.instruction,
        rpc_servers=args.rpc_servers,
        tensor_split=args.tensor_split,
        cache_dir=args.cache_dir
    )
    pt.text()
