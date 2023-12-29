## About

Write a message and cast it into the ocean. Someone else will get your message. And you will get someone else's!

## Running locally

```bash
chmod +x start.sh
./start.sh
```

You can also run in a Docker container

```bash
docker build -t bottle:latest .
docker run -d -p 8080:8080 bottle:latest
```

navigate to `http://localhost:8080` in your browser.
