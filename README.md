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

## Pull a model
Execute the following command to pull the llama model
```
ollama pull llama2
```
Make sure you are using the same OLLAMA_HOST where your server is started.

On the server you should see output like:
```
[GIN] 2023/10/25 - 19:45:38 | 200 |        35.1µs |       127.0.0.1 | HEAD     "/"
[GIN] 2023/10/25 - 19:45:38 | 200 |     385.599µs |       127.0.0.1 | GET      "/api/tags"
2023/10/25 19:45:41 download.go:126: downloading 22f7f8ef5f4c in 64 59 MB part(s)
...
```