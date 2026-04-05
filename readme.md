Flask Application with CI/CD & Docker Deployment

A production-style Flask web application deployed using Docker, GitHub Actions (CI/CD), and AWS EC2.

This project demonstrates automated build, push, and deployment pipeline using modern DevOps practices.


Features

🐳 Dockerized application
🔁 Automated CI/CD pipeline using GitHub Actions
📦 Docker image pushed to Docker Hub
☁️ Auto-deployment on AWS EC2 via SSH
🏷️ Versioned Docker images using commit SHA
🚀 One-push deployment (push → live app)
🛠️ Tech Stack
Backend: Flask
Containerization: Docker
CI/CD: GitHub Actions
Cloud: AWS EC2
Registry: Docker Hub
⚙️ CI/CD Workflow

The pipeline is triggered whenever code is pushed to the main branch.

🔄 Steps:
Checkout Code
Login to Docker Hub
Build Docker Image
Tagged with: latest
Push Image to Docker Hub
SSH into EC2
Pull Latest Image
Stop Old Container
Run New Container


📂 Project Structure
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/workflows/
│   └── ci-cd.yml
└── README.md