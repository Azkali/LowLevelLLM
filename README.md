# Supercharger

Supercharger is a Python library that provides a simple interface to the different LLM back ends. It is designed to be easy to use and to provide a high level of performance.

# Building

```sh
make [vulkan|cpu|metal]
```

For ROCm:
```sh
docker build -f Dockerfile.rocm -t supercharger/rocm .
docker run -it --rm --privileged supercharger/rocm
```
