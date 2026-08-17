# Employee Management System on AWS

## Project Overview

This project demonstrates the design, deployment, automation, monitoring, and security of a cloud-native Employee Management System using AWS services, Docker, Terraform, and GitHub Actions.

The project was completed across four phases:

Week 1: Application Development & Containerization
Week 2: Infrastructure as Code (Terraform)
Week 3: CI/CD Automation
Week 4: Monitoring, Scaling & Security

---

# Architecture

Internet
↓
Application Load Balancer
↓
Auto Scaling Group
↓
EC2 Instance
↓
Flask Application (Docker)
↓
Amazon RDS PostgreSQL

Inside VPC:

Public Subnet 1
Public Subnet 2

Private Subnet 1
Private Subnet 2

---

# Technologies Used

## Application Layer

- Python
- Flask
- PostgreSQL
- HTML/CSS

## Containerization

- Docker
- Docker Hub

## Cloud Platform

- AWS

Services used:

- EC2
- VPC
- RDS PostgreSQL
- Auto Scaling Group
- Application Load Balancer
- CloudWatch
- IAM
- Security Groups

## Infrastructure as Code

- Terraform

## CI/CD

- GitHub Actions

---

# Week 1: Application Development

## Features

- Create Employee
- Read Employee
- Update Employee
- Delete Employee

Full CRUD operations implemented.

## Docker

Application containerized using Docker.

### Build

docker build -t employee-app .

### Run

docker run -p 5000:5000 employee-app

Image stored on Docker Hub.

---

# Week 2: Infrastructure Deployment

## VPC

Created custom VPC:

10.0.0.0/16

## Subnets

### Public

- Public Subnet 1
- Public Subnet 2

### Private

- Private Subnet 1
- Private Subnet 2

## Internet Gateway

Provides internet access to public subnets.

## NAT Gateway

Created to enable outbound internet access from private resources.

## Security Groups

### Flask Security Group

- HTTP (80)
- SSH (22)

### ALB Security Group

- HTTP (80)

### RDS Security Group

- PostgreSQL (5432)

## Database

Amazon RDS PostgreSQL deployed in private subnets.

## Compute

- Launch Template
- Auto Scaling Group

## Load Balancing

Application Load Balancer deployed across multiple Availability Zones.

---

# Week 3: CI/CD Pipeline

## GitHub Actions Workflow

Pipeline triggers on push to main branch.

Workflow:

1. Checkout Repository
2. Login Docker Hub
3. Build Docker Image
4. Push Docker Image
5. SSH into EC2
6. Deploy Latest Container

## GitHub Secrets

- DOCKER_USERNAME
- DOCKER_PASSWORD
- EC2_HOST
- EC2_USER
- EC2_SSH_KEY
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD

## Benefits

- Automated deployments
- Reduced human error
- Faster software delivery

---

# Week 4: Monitoring, Scaling & Security

## Monitoring

CloudWatch configured for:

- CPU Utilization
- Network Usage
- EC2 Monitoring
- RDS Monitoring

## Auto Scaling

Target Tracking Policy configured.

### Scale Up

CPU > 70%

### Scale Down

CPU below threshold

## Security

### Network Isolation

- Public Subnets
- Private Subnets

### Database Protection

RDS deployed privately.

### SSH Restriction

SSH access restricted to trusted IP addresses.

### Secrets Management

Sensitive values stored in GitHub Secrets.

### Encryption

RDS storage encryption enabled.

### Least Privilege

Security Groups configured to allow only required traffic.

---

# Challenges Encountered

## ALB Deployment Failure

Issue:

Public subnets were created in the same Availability Zone.

Resolution:

Moved one public subnet into a different Availability Zone and recreated dependent resources.

## Docker Deployment Failure

Issue:

Application attempted database connection using localhost.

Resolution:

Implemented environment variables and connected Flask application to Amazon RDS.

## GitHub Push Failure

Issue:

Terraform provider files exceeded GitHub file size limits.

Resolution:

Configured .gitignore and removed Terraform-generated files from source control.

---

# Outcomes

Successfully deployed and automated a cloud-native Employee Management System with:

- Infrastructure as Code
- CI/CD Automation
- High Availability
- Monitoring
- Scaling
- Security Controls

---

# Author

Dumisani Malindi
