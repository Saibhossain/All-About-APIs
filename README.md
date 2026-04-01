# 👨‍💻 Author
# **Md Saib Hossain**
**AI Engineer • AI / ML / LLM & AI Safety Researcher**  
**Agentic AI Developer • Researcher in Autonomous & Multi-Agent Systems • Advanced Agentic AI Architect**

Designing safe, scalable, and human-centered intelligent systems for real-world healthcare and autonomous AI applications.

<p align="left">
  <a href="mailto:saibhossain5@gmail.com">
    <img src="https://img.shields.io/badge/Email-saibhossain5%40gmail.com-red?style=flat&logo=gmail">
  </a>
  <a href="https://saibhossain.github.io/">
    <img src="https://img.shields.io/badge/Portfolio-Visit-blue?style=flat&logo=google-chrome">
  </a>
  <a href="https://github.com/Saibhossain">
    <img src="https://img.shields.io/badge/GitHub-Profile-black?style=flat&logo=github">
  </a>
  <a href="https://linkedin.com/in/saib-hossain-182834229">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin">
  </a>
</p>

# Project Descriptions



## 5-project learning path
    All-About_APIs/
    ├── project1_hello_api/
    ├── project2_crud_api/
    ├── project3_auth_api/
    ├── project4_ai_api/
    └── project5_production_ready_api/

# Learning roadmap
    
    Project	Goal	What you learn
    Project 1	First FastAPI app	routes, GET/POST, request/response, Pydantic, docs
    Project 2	CRUD API	create/read/update/delete, path params, query params
    Project 3	Auth API	login, JWT, protected routes, password hashing
    Project 4	AI API	inference endpoint, file upload, model/service layer
    Project 5	Production-ready API	clean architecture, env config, Docker, logging, deployment

## Project 1 — Hello API
    This project will teach:
    
    what happens when API receives a request
    how FastAPI route works
    how request body works
    how validation works
    how to run with Uvicorn
    how to test in /docs

##### File structure

    All-About_APIs/
    └── project1_hello_api/
        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── schemas.py
        │   └── routes.py
        ├── requirements.txt
        └── README.md


## Project 2 — Student CRUD API

This project teaches the next real step after Project 1:

* CRUD = Create, Read, Update, Delete
* path parameters
* query parameters
* request body
* response models
* status codes
* router-based file structure
* simple API-key protection for write operations

FastAPI is a Python API framework built on Starlette and Pydantic, so it gives you routing, request handling, validation, and automatic docs together.

##### File structure
    All-About_APIs/
    └── project2_student_crud_api/
        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── schemas.py
        │   ├── database.py
        │   ├── dependencies.py
        │   └── routes/
        │       ├── __init__.py
        │       └── students.py
        ├── requirements.txt
        └── README.md

## Project 3 — Auth API with JWT
    This project teaches:
    
    user registration
    password hashing
    login
    JWT access token
    protected routes
    current user endpoint
    role-based protected endpoint
    clean file structure
    
    This is still beginner-friendly, but much closer to real backend work.

##### File structure

    All-About_APIs/
    └── project3_auth_api/
        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── schemas.py
        │   ├── database.py
        │   ├── security.py
        │   ├── dependencies.py
        │   └── routes/
        │       ├── __init__.py
        │       ├── auth.py
        │       └── users.py
        ├── requirements.txt
        └── README.md

###  What this project will do

We will create these endpoints:
    
    Method	Endpoint	Purpose
    GET	/	health/welcome
    POST	/auth/register	create user
    POST	/auth/login	login and get JWT
    GET	/users/me	get current logged-in user
    GET	/users/admin-only	protected admin route


    





































#