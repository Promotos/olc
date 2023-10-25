# olc

## Installation

### Windows
1. Install Ubuntu on WSL via  `wsl ---install`
2. Start Ubuntu
3. Install CUDA (https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
4. Install Ollama (https://ollama.ai/download/linux)

## Start Ollama

After the installation start Ollama by `ollama serve`

If you get an error like
```
Error: listen tcp 127.0.0.1:11434: bind: address already in use
```

You can define the address to use for Ollama by setting the environment variable `OLLAMA_HOST`
```
export OLLAMA_HOST=localhost:8888
```

Run the LLM serving should give you the following output
```
wsl:~$ ollama serve
2023/10/25 19:38:15 images.go:822: total blobs: 0
2023/10/25 19:38:15 images.go:829: total unused blobs removed: 0
2023/10/25 19:38:15 routes.go:662: Listening on 127.0.0.1:8888 (version 0.1.5)
```