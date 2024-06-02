# Django Capstone Project
 
## Project Overview

This project is a Django-based web application designed as a capstone project for the HyperionDev Software Engineering bootcamp.

## Setup

### Using Virtual Environment

1. **Clone the repository**:
    git clone https://github.com/AbrieBurger20/Django
    cd Django

2. **Create a virtual environment**:
    python -m venv [venv]

3. **Activate the virtual environment**:
    - On Windows:
      venv\Scripts\activate
      
    - On Unix or MacOS:
      source venv/bin/activate
      
4. **Install the dependencies**:
    pip install -r requirements.txt
    
5. **Apply the migrations**:
    python manage.py migrate

6. **Run the development server**:
    python manage.py runserver
   
### Using Docker

1. **Build the Docker image**:
    docker build -t django 
    
2. **Run the Docker container**:
    docker run -d -p 8000 django

