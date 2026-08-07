Project Overview
Architecture Diagram
Installation Steps
Docker Commands
Database Setup
Screenshots

## Prerequisites

This application requires PostgreSQL.

## Start PostgreSQL

docker run --name postgres-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=employee -p 5432:5432 -d postgres:16

## Start Application

docker run -p 5000:5000 -e DB_HOST=host.docker.internal -e DB_NAME=employee -e DB_USER=postgres -e DB_PASSWORD=password dumisanimalindi/employee-app:v3