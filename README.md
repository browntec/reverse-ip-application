# Reverse IP App

This project implements a simple web application that extracts the origin public IP of any incoming request, reverses it, and stores the reversed IP in a database. The application is containerized using Docker, and it is deployed using Kubernetes with Helm charts. A CI/CD pipeline is included to automate building, pushing, and deploying the application.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Build Docker Image](#2-build-docker-image)
  - [3. Run Locally](#3-run-locally)
  - [4. Helm Deployment](#4-helm-deployment)
  - [5. CI/CD Pipeline](#5-cicd-pipeline)
- [Endpoints](#endpoints)
- [Helm Chart](#helm-chart)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Reverse the origin public IP address of incoming requests.
- Store reversed IP addresses in an SQLite database (can be swapped with other databases).
- Fully containerized using Docker.
- Kubernetes Helm chart for deploying to a K8s cluster.
- CI/CD pipeline for automated image building, pushing, and deployment.

## Tech Stack

- **Language**: Python (Flask)
- **Database**: SQLite (can be replaced with PostgreSQL or MySQL)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Helm**: Used for Kubernetes resource templating and deployment
- **CI/CD**: GitHub Actions
- **Cloud**: Google Cloud Platform (GCP) (for Kubernetes deployment)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/https://github.com/browntec/reverse-ip-application
```

### 2. Build Docker Image
To build the Docker image locally:

```bash
docker build -t reverse-ip-app:v1 .
```
### 3. Run Locally
You can run the application locally using the following command:

```bash
docker run -p 8080:8080 reverse-ip-app:v1
The app will be accessible at http://localhost:8080.
```
### 4. Helm Deployment
First, ensure you have a Kubernetes cluster running and kubectl and Helm installed. Follow these steps:

Create a Kubernetes cluster (using GCP, AWS, or any other provider).
Install Helm:
```bash
helm install reverse-ip-app ./helm-chart
The application should now be deployed, and you can access it via the service's LoadBalancer IP.
```
### 5. CI/CD Pipeline
The CI/CD pipeline is configured in GitHub Actions. It automates the following tasks:

Builds the Docker image.
Pushes the image to a Docker registry (Docker Hub).
Deploys the app to a Kubernetes cluster using Helm.
To set up the CI/CD pipeline:

Add the following secrets to your GitHub repository:
DOCKER_USERNAME: Your Docker Hub username.
DOCKER_PASSWORD: Your Docker Hub password.
AWS_CREDENTIALS: AWS service account credentials for K8s deployment.
On push to the main branch, the CI/CD pipeline will automatically trigger and deploy the app.
Endpoints : http://a27ab2b4063ae422890ddf24042756b6-132266440.us-west-2.elb.amazonaws.com:8080
Helm Chart
The Helm chart for this application defines the following resources:

Deployment: Specifies the pod running the app.
Service: Exposes the app via a LoadBalancer.
Modify the values.yaml file to customize deployment settings such as the image repository, tag, and service type.

CI/CD Pipeline
The CI/CD pipeline is defined in the .github/workflows/cicd.yml file. It performs the following steps:

Build Docker Image: Builds the application image using Docker.
Push Docker Image: Pushes the image to a Docker registry.
Deploy: Deploys the Helm chart to a Kubernetes cluster.
GitHub Secrets Needed:
DOCKER_USERNAME: Docker Hub username.
DOCKER_PASSWORD: Docker Hub password.
AWS_CREDENTIALS: 
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
EKS_CLUSTER_NAME




