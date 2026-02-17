from llama_supercharged.main import main, parser

if __name__ == "__main__":
    args = parser()
    main(args.model, args.json_file, args.cache_dir)
