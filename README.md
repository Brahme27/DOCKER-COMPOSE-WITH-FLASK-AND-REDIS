# Flask + Redis with Docker Compose

## What is Docker Compose?
Docker Compose is a tool used to define and manage multi-container Docker applications. It allows you to configure services, networks, and volumes in a single YAML file (`docker-compose.yml`) and run multiple containers with a single command.

## About This Project
This project is a simple Flask web application that uses Redis to count page visits. The project is containerized using Docker Compose, making it easy to deploy and manage.

In this project, Docker Compose is used to manage two Docker containers:

Flask App (flask-app) - Built using the Dockerfile (custom image).
Redis (redis) - Uses the official redis image from Docker Hub.

### Project Files
- `app.py` - Flask application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container setup
- `docker-compose.yml` - Defines services

## Basic Docker Compose Commands

### 1. **Build and Run the Containers**
```sh
docker-compose up --build
```
- Starts the Flask app on `http://localhost:8000`
- Redis runs in the background

### 2. **Stop the Containers**
```sh
docker-compose down
```

### 3. **Run in Detached Mode (Background)**
```sh
docker-compose up -d
```

### 4. **View Running Containers**
```sh
docker ps
```

## Usage
Open a browser and visit:
```
http://localhost:8000
```
You should see:
```
Hello! This page has been refreshed X times.
```