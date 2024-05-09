# PianoVibes_Community

Welcome to PianoVibes_Community, a platform dedicated to Amapiano music enthusiasts. This README.md file provides instructions on how to build and run the PianoVibes_Community project using venv and Docker.

## Table of Contents

- [Introduction](#introduction)
- [Setup Using venv](#setup-using-venv)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Setup Using Docker](#setup-using-docker)
  - [Prerequisites](#prerequisites-docker)
  - [Installation Steps](#installation-steps-docker)
- [Important Notes](#important-notes)

## Introduction

PianoVibes_Community is a platform that brings together fans of Amapiano music to discuss trends, share playlists, discover artists, and connect with fellow enthusiasts.

## Setup Using venv

### Prerequisites
- Python 3.x installed
- Git installed
- pip (Python package manager) installed

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Shenge06/PianoVibes_Community.git
Navigate to the project directory:
bash
Copy code
cd PianoVibes_Community
Create and activate a virtual environment:
bash
Copy code
python -m venv env
source env/bin/activate
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configure Django settings:
Rename example.env to .env.
Update .env with your Django project settings, including DEBUG, DATABASES, SECRET_KEY, etc.
Run migrations:
bash
Copy code
python manage.py migrate
Start the development server:
bash
Copy code
python manage.py runserver
Access the application:
Open your web browser and navigate to http://localhost:8000/
Setup Using Docker

Prerequisites
Docker installed
Docker Compose installed
Installation Steps
Clone the repository:
bash
Copy code
git clone https://github.com/Shenge06/PianoVibes_Community.git
Navigate to the project directory:
bash
Copy code
cd PianoVibes_Community
Build the Docker containers:
bash
Copy code
docker-compose build
Start the Docker containers:
bash
Copy code
docker-compose up
Access the application:
Open your web browser and navigate to http://localhost:8000/
Important Notes

Secrets: Do not commit secrets such as passwords or access tokens to public repos. Update .env and Docker Compose files with appropriate credentials.
Environment Variables: Make sure to configure environment variables for production deployment.
Support: For further assistance or troubleshooting, refer to the project documentation or contact the support team.
Enjoy using PianoVibes_Community!
