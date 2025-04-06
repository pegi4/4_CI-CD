#!/bin/bash

# Exit on any error
set -e

# Build the server image
echo "Building server image..."
cd server
docker build -t server:v1 .
cd ..

# Build the client image
echo "Building client image..."
cd client
docker build -t client:v1 .
cd ..

# Create a Docker network (if it doesn’t exist)
echo "Creating Docker network..."
docker network inspect my-network >/dev/null 2>&1 || docker network create my-network

# Stop and remove any existing containers (optional, to avoid conflicts)
echo "Stopping and removing existing containers..."
docker rm -f server 2>/dev/null || true
docker rm -f client 2>/dev/null || true

# Run the server container
echo "Running server container..."
docker run -d --name server --network my-network server:v1

# Run the client container
echo "Running client container..."
docker run -d --name client --network my-network -p 9861:9861 client:v1

# Get the IP address of the client container
echo "Fetching client IP address..."
CLIENT_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' client)

echo "Containers are up! Check them with 'docker ps'"
echo "Client IP address: $CLIENT_IP"
echo "Access client at http://localhost:9861"