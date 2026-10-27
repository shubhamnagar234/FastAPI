# 🚀 FastAPI & Machine Learning: Zero to Production & Cloud Deployment

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/ASGI-Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.6+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-EC2%20Deployment-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/ec2/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

An end-to-end, production-grade guide to modern web APIs, schema validation, data engineering, and real-time Machine Learning model serving with **FastAPI**, **Pydantic v2**, **Docker**, and **AWS EC2**.

This repository serves as a complete learning journey and production blueprint—progressing from basic HTTP concepts and ASGI asynchronous architecture to building full RESTful CRUD systems, engineering feature pipelines, serving ML inference endpoints, containerizing applications with Docker, and deploying to cloud infrastructure on AWS.

---

## 📌 Table of Contents

- [Architectural Overview](#-architectural-overview)
- [Repository Structure](#-repository-structure)
- [12-Module Deep Dive](#-12-module-deep-dive)
  - [01. Introduction to APIs](#01-introduction-to-apis)
  - [02. How to Setup FastAPI & Architecture](#02-how-to-setup-fastapi--architecture)
  - [03. HTTP Methods in FastAPI](#03-http-methods-in-fastapi)
  - [04. Path & Query Parameters with Status Codes](#04-path--query-parameters-with-status-codes)
  - [05. Pydantic v2 Masterclass](#05-pydantic-v2-masterclass)
  - [06. POST Requests & Request Body Validation](#06-post-requests--request-body-validation)
  - [07. PUT & DELETE: Full CRUD Lifecycle](#07-put--delete-full-crud-lifecycle)
  - [08. Serving Machine Learning Models with FastAPI](#08-serving-machine-learning-models-with-fastapi)
  - [09. Improving the FastAPI API: Production Architecture](#09-improving-the-fastapi-api-production-architecture)
  - [10. Docker for Machine Learning & APIs](#10-docker-for-machine-learning--apis)
  - [11. How to Dockerize a FastAPI Application](#11-how-to-dockerize-a-fastapi-application)
  - [12. Deploying FastAPI on AWS EC2 with Streamlit](#12-deploying-fastapi-on-aws-ec2-with-streamlit)
- [Featured Applications](#-featured-applications)
- [Technology Matrix](#-technology-matrix)
- [Getting Started Locally](#-getting-started-locally)
- [Docker Quickstart](#-docker-quickstart)
- [AWS Deployment Guide](#-aws-deployment-guide)
- [Interactive API Documentation](#-interactive-api-documentation)
- [Contributing & License](#-contributing--license)

---

## 🏛 Architectural Overview

```
                      ┌──────────────────────────────────────────────┐
                      │                 Client Tier                  │
                      │  (Browser / Web App / Streamlit / Mobile)    │
                      └──────────────────────┬───────────────────────┘
                                             │ HTTP / JSON
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │              Uvicorn ASGI Server             │
                      └──────────────────────┬───────────────────────┘
                                             │ Async Loop
                                             ▼
                      ┌──────────────────────────────────────────────┐
                      │               FastAPI Gateway                │
                      │   - Routing & Dependency Injection           │
                      │   - Pydantic v2 Serialization & Coercion     │
                      │   - Automatic OpenAPI Documentation          │
                      └──────────────┬───────────────────────────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
    ┌──────────────────────────┐           ┌──────────────────────────┐
    │  Patient Management App  │           │   ML Serving Pipeline    │
    │  - Path / Query Params   │           │  - Dynamic Feature Eng.  │
    │  - CRUD Lifecycle        │           │  - Model (.pkl) Predict  │
    │  - JSON Persistence      │           │  - Confidence Scoring    │
    └──────────────────────────┘           └──────────────────────────┘
                                                         │
                                                         ▼
                                           ┌──────────────────────────┐
                                           │  Docker Container on AWS │
                                           │  - Amazon Linux / Ubuntu │
                                           │  - EC2 Inbound Rules     │
                                           │  - High Availability     │
                                           └──────────────────────────┘
```

---

## 📂 Repository Structure

```
FastAPI/
├── 01_Introduction_to_APIs/                       # API fundamentals, client-server models & ML perspectives
│   ├── README.md
│   └── images/
├── 02_How_to_setup_FastAPI/                       # ASGI vs WSGI, Uvicorn setup, first endpoint & docs
│   ├── README.md
│   ├── main.py
│   └── images/
├── 03_HTTP_Methods_in_FastAPI/                    # Static vs Dynamic web, HTTP verbs, JSON data loading
│   ├── README.md
│   ├── main.py
│   ├── patients.json
│   └── images/
├── 04_Path_and_Query_Params_in_FastAPI/           # Dynamic routes, Path/Query validation, HTTPException
│   ├── README.md
│   ├── main.py
│   ├── patients.json
│   └── images/
├── 05_Pydantic_Crash_Course/                      # Deep dive: BaseModels, Field, Model & Computed Validators
│   ├── 01_why_pydantic.py
│   ├── 02_pydantic_demo.py
│   ├── 03_pydantic_depth.py
│   ├── 04_field_validator.py
│   ├── 05_model_validator.py
│   ├── 06_computed_fields.py
│   ├── 07_nested_models.py
│   ├── 08_serialization.py
│   └── README.md
├── 06_Post_Request_in_FastAPI/                    # Request bodies, Pydantic model injection, 201 Created
│   ├── README.md
│   ├── main.py
│   ├── patients.json
│   └── images/
├── 07_PUT_and_DELETE_in_FastAPI/                  # Partial updates (exclude_unset), deletions & full CRUD
│   ├── README.md
│   ├── main.py
│   ├── patients.json
│   └── images/
├── 08_Serving_ML_Models_with_FastAPI/             # Random Forest training, pickle export, inference & Streamlit
│   ├── README.md
│   ├── fastapi_ml_model.ipynb
│   ├── insurance.csv
│   ├── model.pkl
│   ├── app.py
│   ├── frontend.py
│   └── images/
├── 09_Improving_the_FastAPI_API/                  # Enterprise architecture: config, schema, model separation
│   ├── README.md
│   ├── app.py
│   ├── requirements.txt
│   ├── config/
│   │   └── city_tier.py
│   ├── schema/
│   │   ├── user_input.py
│   │   └── prediction_response.py
│   └── model/
│       ├── model.pkl
│       └── predict.py
├── 10_Docker_for_Machine_Learning/                # Docker runtime, daemon, images, container lifecycle & specs
│   ├── README.md
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── images/
├── 11_How_to_Dockerize_a_FastAPI_API_Application/ # Production Dockerfile, image build, port bindings & registry push
│   ├── README.md
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── config/
│   ├── model/
│   ├── schema/
│   └── images/
├── 12_How_to_Deploy_a_FastAPI_API_on_AWS/         # AWS EC2 deployment, remote Docker execution & Streamlit client
│   ├── README.md
│   ├── main.py
│   ├── frontend.py
│   ├── requirements.txt
│   ├── config/
│   ├── model/
│   └── schema/
├── .gitignore                                     # Clean repository exclusions (venv, caches, models)
├── LICENSE                                        # MIT License
├── README.md                                      # Project Master Documentation
└── requirements.txt                               # Repository-level Python dependencies
```

---

## 🔍 12-Module Deep Dive

### [01. Introduction to APIs](01_Introduction_to_APIs/)

- **Core Technology**: REST, HTTP/HTTPS, JSON Data Exchange, Client-Server Protocol.
- **Description**: Establishes foundational concepts of Application Programming Interfaces (APIs). Uses the classic restaurant waiter analogy (Client → API → Backend → Database) to illustrate request/response mechanics.
- **Key Concepts Covered**:
  - Decoupling frontend presentation from backend logic.
  - Multi-client architecture: One backend API serving Web, iOS, and Android applications simultaneously.
  - Language independence: Enabling Python, Java, Go, and PHP clients to exchange structured JSON.
  - Machine Learning perspective: How real-time ML systems expose inference endpoints to decouple model compute from client applications.
- **Visuals Included**: API architecture diagrams, multi-platform flowcharts, and client-server communication models.

---

### [02. How to Setup FastAPI & Architecture](02_How_to_setup_FastAPI/)

- **Core Technology**: FastAPI, Starlette, Pydantic, Uvicorn, ASGI.
- **Description**: Detailed exploration of FastAPI's core philosophy ("Fast to Run" & "Fast to Code") and ASGI asynchronous runtime.
- **Key Concepts Covered**:
  - **Starlette Foundation**: Asynchronous Server Gateway Interface (ASGI) processing concurrent requests via Python's async event loop.
  - **WSGI vs. ASGI Comparison**: Why traditional WSGI frameworks (e.g., Flask with Gunicorn) block workers during I/O, whereas ASGI (FastAPI with Uvicorn) handles high-concurrency non-blocking operations.
  - **Auto-Documentation**: Instant interactive OpenAPI documentation via Swagger UI (`/docs`) and ReDoc (`/redoc`).
  - **Code Exploration**: Initializing `FastAPI()`, creating path operations with `@app.get()`, and running the development server with live reload:
    ```bash
    uvicorn main:app --reload
    ```

---

### [03. HTTP Methods in FastAPI](03_HTTP_Methods_in_FastAPI/)

- **Core Technology**: HTTP Verbs (GET, POST, PUT, DELETE), JSON Persistence, REST Design.
- **Description**: Transitioning from static sites to dynamic web services handling CRUD (Create, Read, Update, Delete) operations.
- **Key Concepts Covered**:
  - The role of HTTP verbs: GET (fetch data), POST (create resource), PUT (update state), DELETE (remove resource).
  - Launching the **Patient Management System** project: reading structured medical records from `patients.json`.
  - Creating endpoints to return project metadata and full patient directories.

---

### [04. Path & Query Parameters with Status Codes](04_Path_and_Query_Params_in_FastAPI/)

- **Core Technology**: FastAPI `Path`, `Query`, `HTTPException`, HTTP Status Codes (RFC 9110).
- **Description**: Deep dive into dynamic URL routing, query-based data filtering, and explicit HTTP status code communication.
- **Key Concepts Covered**:
  - **Path Parameters**: Identifying specific resources via dynamic URL segments (`/patient/{patient_id}`) with parameter metadata and examples using `Path(...)`.
  - **Query Parameters**: Implementing sorting and filtering logic (`/sort?sort_by=bmi&order=desc`) using `Query(...)`.
  - **HTTP Status Codes Categorization**:
    - `2xx` Success (200 OK, 201 Created, 204 No Content)
    - `3xx` Redirection
    - `4xx` Client Errors (400 Bad Request, 404 Not Found, 422 Unprocessable Entity)
    - `5xx` Server Errors (500 Internal Server Error, 503 Service Unavailable)
  - **Error Handling**: Graceful error handling using `HTTPException` with custom details.

---

### [05. Pydantic v2 Masterclass](05_Pydantic_Crash_Course/)

- **Core Technology**: Pydantic v2, Python Type Annotations, Type Coercion, Data Validation.
- **Description**: A comprehensive standalone crash course in Pydantic v2 covering schema definitions, constraints, custom validators, and serialization.
- **Key Concepts & Code Breakdown**:
  - `01_why_pydantic.py`: Why manual dictionary validation fails and how type hints prevent runtime bugs.
  - `02_pydantic_demo.py` & `03_pydantic_depth.py`: `BaseModel` inheritance, `Field(...)` constraints (`gt`, `lt`, `min_length`, regex), default values, and automatic type coercion.
  - `04_field_validator.py`: Custom field sanitization with `@field_validator` (e.g., domain whitelist checks and name uppercasing).
  - `05_model_validator.py`: Cross-field validation with `@model_validator(mode='after')` (e.g., password confirmation or age-dependency checks).
  - `06_computed_fields.py`: Dynamically derived attributes using `@computed_field` (e.g., auto-calculating BMI and clinical health category from height and weight).
  - `07_nested_models.py`: Handling hierarchical nested JSON schemas with child models.
  - `08_serialization.py`: Exporting models to dictionaries and JSON using `.model_dump()` and `.model_dump_json()` with `include`, `exclude`, and `exclude_unset` filters.

---

### [06. POST Requests & Request Body Validation](06_Post_Request_in_FastAPI/)

- **Core Technology**: HTTP POST, Request Body, Pydantic Model Integration, JSONResponse.
- **Description**: Ingesting and validating incoming JSON payloads sent by clients using Pydantic schemas in FastAPI endpoints.
- **Key Concepts Covered**:
  - Request body parsing and automatic validation against the `Patient` schema.
  - Handling invalid payloads: FastAPI automatically responds with standard `422 Unprocessable Entity` containing field-level error messages.
  - Persisting new records to disk in `patients.json`.
  - Returning semantic HTTP status codes using `JSONResponse(status_code=201, ...)`.

---

### [07. PUT & DELETE: Full CRUD Lifecycle](07_PUT_and_DELETE_in_FastAPI/)

- **Core Technology**: HTTP PUT, HTTP DELETE, Partial Updates (`exclude_unset=True`), RESTful State Management.
- **Description**: Completing the Patient Management System API by adding resource updating and deletion endpoints.
- **Key Concepts Covered**:
  - **PUT Operations**: Updating existing patient records via `/edit/{patient_id}`.
  - **Partial Update Patterns**: Using `PatientUpdate` with `Optional[T] = None` and `patient_update.model_dump(exclude_unset=True)` so users only update fields they specify.
  - **Re-validation**: Re-instantiating the updated data through the primary `Patient` model to automatically recalculate dynamic computed properties (BMI and verdict).
  - **DELETE Operations**: Removing patient records safely from the dataset with proper 404 existence verification.

---

### [08. Serving Machine Learning Models with FastAPI](08_Serving_ML_Models_with_FastAPI/)

- **Core Technology**: Scikit-Learn (Random Forest), Pandas, NumPy, Pickle, FastAPI, Streamlit.
- **Description**: End-to-end Machine Learning model serving—from data preparation and training to API deployment and frontend UI consumption.
- **Key Concepts Covered**:
  - **Model Training (`fastapi_ml_model.ipynb`)**: Training a Random Forest Classifier on `insurance.csv` to predict Insurance Premium Categories (`Low`, `Medium`, `High`).
  - **Feature Engineering Pipeline**: Deriving key predictive features (BMI, Lifestyle Risk, Age Group, City Tier) and serializing the trained model to `model.pkl`.
  - **FastAPI Model Gateway (`app.py`)**: Loading `model.pkl` on startup, accepting raw user data, auto-engineering features on-the-fly using Pydantic computed fields, and returning predictions.
  - **Streamlit Interactive UI (`frontend.py`)**: Building a web interface with forms and sliders that makes HTTP POST requests to the FastAPI endpoint to display predictions in real time.

---

### [09. Improving the FastAPI API: Production Architecture](09_Improving_the_FastAPI_API/)

- **Core Technology**: Enterprise Python Architecture, Separation of Concerns (SoC), Response Models, Health Checks.
- **Description**: Refactoring the ML API into a clean, maintainable, production-ready modular codebase.
- **Architecture & Highlights**:
  - **Modular Directory Layout**:
    - `config/city_tier.py`: Centralized configuration constants and city tier classifications.
    - `schema/user_input.py`: Modular Pydantic request schema with field validation.
    - `schema/prediction_response.py`: Strict output validation schema defining `predicted_category`, `confidence`, and `class_probabilities`.
    - `model/predict.py`: Encapsulated inference logic, model loading, and `MODEL_VERSION` tracking.
    - `app.py`: Clean routing gateway with error handling.
  - **Health Monitoring**: Dedicated `/health` endpoint reporting system status, model load state, and active model version.
  - **Confidence Scores**: Returning full class probability breakdowns alongside the primary prediction.
  - **Defensive Programming**: Try-catch blocks handling unexpected inference failures gracefully with `500` error responses.

---

### [10. Docker for Machine Learning & APIs](10_Docker_for_Machine_Learning/)

- **Core Technology**: Docker Engine, Container Runtime, Dockerfile Directives, Docker Hub.
- **Description**: Deep dive into containerization principles, resolving environment discrepancies ("works on my machine"), and packaging ML applications.
- **Key Concepts Covered**:
  - **Docker Engine Architecture**: Interaction between the Docker CLI, REST API, and Docker Daemon (`dockerd`).
  - **Images vs. Containers**: Immutable, layered image definitions vs. active, isolated runtime instances.
  - **Dockerfile Directives**: Comprehensive guide to `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`, `EXPOSE`, `ENV`, `ARG`, and `VOLUME`.
  - **Registries**: Pushing, pulling, and versioning images using Docker Hub, AWS ECR, and Google Container Registry.
  - **Microservices & MLOps**: Benefits of containerization for CI/CD pipelines, reproducible research, and cloud portability.

---

### [11. How to Dockerize a FastAPI Application](11_How_to_Dockerize_a_FastAPI_API_Application/)

- **Core Technology**: Multi-layer Docker Builds, Python 3.11-slim, Port Forwarding, Container Networking.
- **Description**: Step-by-step containerization of the modular FastAPI Machine Learning application.
- **Key Concepts Covered**:
  - Writing an optimized production `Dockerfile`:
    ```dockerfile
    FROM python:3.11-slim
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .
    EXPOSE 8000
    CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
    ```
  - **Build & Run Workflow**:

    ```bash
    # Build container image
    docker build -t your-docker-username/fastapi-ml-app:latest .

    # Run detached container with port forwarding
    docker run -d -p 8000:8000 your-docker-username/fastapi-ml-app:latest
    ```

  - Pushing images to **Docker Hub** for cloud distribution.

---

### [12. Deploying FastAPI on AWS EC2 with Streamlit](12_How_to_Deploy_a_FastAPI_API_on_AWS/)

- **Core Technology**: Amazon Web Services (AWS), EC2 (Ubuntu), Linux CLI, Security Groups, Streamlit Client.
- **Description**: Deploying the containerized FastAPI ML application onto a live cloud server on AWS EC2 and connecting an external Streamlit client.
- **Key Concepts Covered**:
  - **EC2 Instance Provisioning**: Launching an Ubuntu instance and connecting via SSH.
  - **Docker Host Setup**: Installing and configuring Docker on EC2:
    ```bash
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo usermod -aG docker $USER
    ```
  - **Pull & Run**: Pulling the production image from Docker Hub and running it on EC2.
  - **Networking & Security Groups**: Configuring AWS inbound firewall rules to allow traffic on ports `8000` / `8080`.
  - **Frontend Integration**: Connecting the Streamlit dashboard (`frontend.py`) directly to the public AWS EC2 IP address for live predictions.

---

## 💡 Featured Applications

### 1. Patient Management REST API

A healthcare data service providing full CRUD capabilities with input validation and automated metric derivation.

- **Endpoints**:
  - `GET /`: Project overview.
  - `GET /view`: List all patient records.
  - `GET /patient/{patient_id}`: Retrieve record by ID with validation.
  - `GET /sort?sort_by=height&order=asc`: Dynamic sorting by height, weight, or BMI.
  - `POST /create`: Register patient with validated physical metrics, calculating BMI and weight classification automatically.
  - `PUT /edit/{patient_id}`: Partial update of patient fields with automatic re-computation.
  - `DELETE /delete/{patient_id}`: Remove record with 404 verification.

### 2. Insurance Premium Predictor (MLOps Pipeline)

An end-to-end Machine Learning service predicting insurance premium categories (`Low`, `Medium`, `High`) based on lifestyle and demographic risk factors.

- **Endpoints**:
  - `GET /`: Human-readable service message.
  - `GET /health`: Monitoring endpoint returning status, model state, and active version.
  - `POST /predict`: Inference endpoint returning predictions, confidence metrics, and class probabilities.
- **Frontend**: Streamlit dashboard with real-time prediction cards and probability visualizations.

---

## 🛠 Technology Matrix

| Category                      | Technologies & Tools                                                                                                                                                                                                   |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend & API Framework**   | [FastAPI](https://fastapi.tiangolo.com/), [Starlette](https://www.starlette.io/), [Uvicorn](https://www.uvicorn.org/)                                                                                                  |
| **Data Validation & Schemas** | [Pydantic v2](https://docs.pydantic.dev/) (`BaseModel`, `Field`, `field_validator`, `model_validator`, `computed_field`)                                                                                               |
| **Machine Learning & Data**   | [Scikit-Learn](https://scikit-learn.org/) (Random Forest), [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Pickle](https://docs.python.org/3/library/pickle.html), [Jupyter](https://jupyter.org/) |
| **Frontend UI**               | [Streamlit](https://streamlit.io/), [Requests](https://requests.readthedocs.io/)                                                                                                                                       |
| **Containerization & DevOps** | [Docker](https://www.docker.com/), [Docker Engine](https://docs.docker.com/engine/), [Dockerfile](https://docs.docker.com/engine/reference/builder/), [Docker Hub](https://hub.docker.com/)                            |
| **Cloud Infrastructure**      | [AWS EC2](https://aws.amazon.com/ec2/), Ubuntu Linux, Security Groups                                                                                                                                                  |
| **API Standards**             | REST, OpenAPI 3.0, Swagger UI, ReDoc, JSON, HTTP/1.1 & HTTP/2                                                                                                                                                          |

---

## 🚀 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/shubhamnagar234/FastAPI.git
cd FastAPI
```

### 2. Set Up a Python Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell):
.venv\Scripts\Activate.ps1

# Activate on macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run Any Module

To run the production ML application in `09_Improving_the_FastAPI_API`:

```bash
cd 09_Improving_the_FastAPI_API
uvicorn app:app --reload --port 8000
```

To run the Streamlit frontend:

```bash
cd 08_Serving_ML_Models_with_FastAPI
streamlit run frontend.py
```

---

## 🐳 Docker Quickstart

To run the production-ready containerized application locally:

```bash
# Navigate to the dockerized module
cd 11_How_to_Dockerize_a_FastAPI_API_Application

# Build the Docker image
docker build -t fastapi-ml-service:latest .

# Run the container
docker run -d -p 8000:8000 --name ml-api fastapi-ml-service:latest

# Check container status
docker ps

# Verify the health endpoint
curl http://localhost:8000/health
```

---

## ☁️ AWS Deployment Guide

To deploy the API on a live Amazon EC2 instance:

```bash
# 1. SSH into your EC2 Ubuntu instance
ssh -i "your-key.pem" ubuntu@ec2-your-instance-ip.compute-1.amazonaws.com

# 2. Update packages and install Docker
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# 3. Log out and reconnect to apply group changes
exit
ssh -i "your-key.pem" ubuntu@ec2-your-instance-ip.compute-1.amazonaws.com

# 4. Pull and run your container from Docker Hub
docker pull your-docker-username/fastapi-ml-app:latest
docker run -d -p 8000:8000 --restart always your-docker-username/fastapi-ml-app:latest

# 5. Security Group Configuration:
# In the AWS EC2 Management Console, open Security Groups for your instance.
# Add an Inbound Rule:
# Type: Custom TCP | Port Range: 8000 | Source: Anywhere (0.0.0.0/0)
```

Now configure your local Streamlit `frontend.py` to target your AWS public IP:

```python
API_URL = "http://<YOUR_AWS_EC2_PUBLIC_IP>:8000/predict"
```

---

## 📖 Interactive API Documentation

Once your FastAPI server is running, explore and test the endpoints directly through auto-generated OpenAPI documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)  
  _Interactive documentation enabling one-click API testing, request payload building, and live response inspection._
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)  
  _Clean, production-oriented specification documentation with schema diagrams._

---

## 🤝 Contributing & License

Contributions, feedback, and improvements are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Crafted with ❤️ by <b>Shubham Nagar</b>
</p>
