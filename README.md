# Flask Remote Docker

Minimal Flask service packaged with Docker.

## Run locally

```bash
docker build -t flask-remote .
docker run --rm -p 8000:8000 flask-remote
```

Open `http://localhost:8000/` or `http://localhost:8000/health`.
