# SSED Lab 5

A lightweight Python HTTP server demonstrating simple interest calculation.

## Project Overview

The application exposes an HTTP GET endpoint that returns a JSON response
containing the service status, version, and a sample interest calculation.

## Technology Stack

- Python 3.12
- HTTP Server
- JSON
- Docker
- GitHub Actions

## Run Locally

```bash
python app/main.py
```

The server listens on port 8000.

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Run Using Docker

```bash
docker build -t ssed-lab5 .
docker run -p 8000:8000 ssed-lab5
```

## Maintainer

Diya Maheshwari

GitHub: https://github.com/Diyaaa-12
