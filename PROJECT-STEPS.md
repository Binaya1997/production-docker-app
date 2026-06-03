Docker Production-Style Multi-Container Application - Complete Setup Guide
Objective

Build a production-style Docker application consisting of:

Nginx Reverse Proxy
Frontend Application
Flask Backend API
PostgreSQL Database
Docker Compose
Docker Volumes
Docker Networks
Environment Variables
Health Checks
Prerequisites

Install:

Docker
Docker Compose Plugin

Verify:

docker --version

docker compose version

Step 1 - Create Project Structure

mkdir production-docker-app

cd production-docker-app

mkdir frontend backend nginx

Project structure:

production-docker-app/

├── frontend/

├── backend/

├── nginx/

├── docker-compose.yml

└── .env

Step 2 - Create Frontend

Create:

frontend/index.html

Paste:

Step 3 - Frontend Dockerfile

Create:

frontend/Dockerfile

Paste:

FROM nginx

COPY index.html /usr/share/nginx/html/index.html

Step 4 - Backend Application

Create:

backend/app.py

Paste:

from flask import Flask
import psycopg2
import os

app = Flask(name)

@app.route("/")
def home():
return "Backend API Running"

@app.route("/health")
def health():
return "OK", 200

@app.route("/db")
def db():

try:

    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

    conn.close()

    return "Database Connection Successful"

except Exception as e:

    return str(e)

if name == "main":

app.run(host="0.0.0.0", port=5000)
Step 5 - Requirements File

Create:

backend/requirements.txt

Paste:

flask
psycopg2-binary

Step 6 - Backend Dockerfile

Create:

backend/Dockerfile

Paste:

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update &&
apt-get install -y curl &&
pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

Step 7 - Nginx Reverse Proxy

Create:

nginx/default.conf

Paste:

server {

listen 80;

location / {

    proxy_pass http://frontend:80;

}

location /api/ {

    proxy_pass http://backend:5000/;

}

}

Step 8 - Environment Variables

Create:

.env

Paste:

DB_HOST=postgres

DB_NAME=mydb

DB_USER=postgres

DB_PASSWORD=postgres123

Step 9 - Docker Compose

Create:

docker-compose.yml

Paste:

services:

frontend:

build: ./frontend

container_name: frontend

backend:

build: ./backend

container_name: backend

environment:

  DB_HOST: ${DB_HOST}

  DB_NAME: ${DB_NAME}

  DB_USER: ${DB_USER}

  DB_PASSWORD: ${DB_PASSWORD}

healthcheck:

  test: ["CMD", "curl", "-f", "http://localhost:5000/health"]

  interval: 10s

  timeout: 5s

  retries: 3

postgres:

image: postgres:15

container_name: postgres

environment:

  POSTGRES_DB: ${DB_NAME}

  POSTGRES_USER: ${DB_USER}

  POSTGRES_PASSWORD: ${DB_PASSWORD}

volumes:

  - postgres_data:/var/lib/postgresql/data

nginx:

image: nginx:latest

container_name: nginx

ports:

  - "80:80"

volumes:

  - ./nginx/default.conf:/etc/nginx/conf.d/default.conf

depends_on:

  - frontend

  - backend

volumes:

postgres_data:

Step 10 - Build Project

Run:

docker compose up -d --build

Step 11 - Verify Containers

docker ps

Expected:

frontend

backend

postgres

nginx

Backend should become:

healthy

Step 12 - Test Application

Frontend:

http://SERVER_IP

Backend:

http://SERVER_IP/api/

Database Test:

http://SERVER_IP/api/db

Useful Commands

View Containers:

docker ps

View Logs:

docker logs backend

docker logs postgres

docker logs nginx

Inspect Health:

docker inspect backend

Enter Container:

docker exec -it backend sh

docker exec -it nginx sh

docker exec -it postgres bash

Stop Project:

docker compose down

Start Project:

docker compose up -d

Rebuild Project:

docker compose up -d --build

Troubleshooting Labs

Lab 1 - Docker DNS Failure

Change:

DB_HOST=postgres1

Expected:

could not translate host name

Lab 2 - Nginx Upstream Failure

Change:

proxy_pass http://backend123:5000/

Expected:

host not found in upstream

Lab 3 - Route Failure

Remove trailing slash:

proxy_pass http://backend:5000

Expected:

404 Not Found

Lab 4 - Database Outage

Stop database:

docker stop postgres

Expected:

Database connection failure

Lab 5 - Healthcheck Failure

Change:

/health

to

/health123

Expected:

backend becomes unhealthy

Lab 6 - Authentication Failure

Change:

DB_PASSWORD=wrongpassword

Expected:

FATAL: password authentication failed

Skills Learned
Dockerfiles
Docker Compose
Reverse Proxy
Volumes
Networks
Environment Variables
Health Checks
Service Discovery
Container Troubleshooting
Multi-Service Architecture
Production-Style Docker Deployment

IMAGES IN DOCKER HUB:

docker pull binayadevops/production-docker-app-frontend

docker pull binayadevops/nginx:alpine

docker pull binayadevops/postgres:15

docker pull binayadevops/production-docker-app-backend




