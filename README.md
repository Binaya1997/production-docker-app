Docker Production-Style Multi-Container Application
Project Overview

This project demonstrates a production-style Dockerized application stack using:

Nginx Reverse Proxy
Frontend Application
Python Flask Backend API
PostgreSQL Database
Docker Compose
Docker Networks
Docker Volumes
Health Checks
Environment Variables

The goal was to learn Docker beyond basic containers by building and troubleshooting a real multi-service architecture.

Architecture

Browser
→ Nginx Reverse Proxy
→ Frontend

Browser
→ Nginx Reverse Proxy
→ Flask Backend
→ PostgreSQL Database

Project Structure

production-docker-app/

├── frontend/

│ ├── Dockerfile

│ └── index.html

├── backend/

│ ├── Dockerfile

│ ├── app.py

│ └── requirements.txt

├── nginx/

│ └── default.conf

├── .env

└── docker-compose.yml

Technologies Used
Docker
Docker Compose
Nginx
Python Flask
PostgreSQL
Linux
Features Implemented
Reverse Proxy

Nginx acts as a reverse proxy and routes requests:

/ → Frontend
/api/ → Backend
Multi-Service Architecture

Services communicate through Docker networking:

frontend
backend
postgres
nginx
Persistent Storage

PostgreSQL data is stored using Docker volumes.

Environment Variables

Application configuration is managed using a .env file.

Health Checks

Docker monitors backend health using:

curl http://localhost:5000/health

Custom Docker Network

Containers communicate using Docker DNS:

backend → postgres

nginx → backend

Running the Project
Clone Repository

git clone

cd production-docker-app

Start Application

docker compose up -d --build

Verify Containers

docker ps

Access Application

Frontend:

http://

Backend:

http:///api/

Database Test:

http:///api/db

Environment Variables

Example .env

DB_HOST=postgres

DB_NAME=mydb

DB_USER=postgres

DB_PASSWORD=postgres123

Health Check Configuration

Backend health endpoint:

/health

Docker Compose health check:

healthcheck:

test: ["CMD", "curl", "-f", "http://localhost:5000/health"]

interval: 10s

timeout: 5s

retries: 3

Practical Troubleshooting Performed
1. Docker DNS Failure

Issue:

DB_HOST=postgres1

Error:

could not translate host name

Learning:

Docker DNS and service discovery.

2. Nginx Upstream Failure

Issue:

proxy_pass http://backend123:5000

Error:

host not found in upstream

Learning:

Reverse proxy upstream troubleshooting.

3. Route Mismatch

Issue:

Incorrect proxy_pass path handling.

Error:

404 Not Found

Learning:

Nginx URL rewriting and routing.

4. Database Container Stopped

Issue:

PostgreSQL container stopped.

Learning:

Container dependency troubleshooting.

5. Health Check Failure

Issue:

Incorrect health endpoint URL.

Result:

Container became unhealthy.

Learning:

Docker health checks and container status monitoring.

6. Authentication Failure

Issue:

Wrong database password.

Error:

FATAL: password authentication failed

Learning:

Configuration and credential troubleshooting.

7. Infrastructure Network Failure

Issue:

VMware NAT service stopped.

Error:

Unable to pull Docker images.

Learning:

Difference between Docker problems and infrastructure/network problems.

Key Docker Concepts Practiced
Dockerfiles
Multi-stage builds
Docker Compose
Volumes
Networks
Reverse Proxy
Environment Variables
Health Checks
Container Inspection
Service Discovery
Troubleshooting
Outcome

This project helped build practical Docker skills by implementing and troubleshooting a production-style multi-container application stack instead of only running standalone containers.
