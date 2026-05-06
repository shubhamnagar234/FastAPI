# FastAPI Philosophy | How to setup FastAPI | Installation and Code Demo

#### FastAPI is a modern, high-performance, web framework for building APIs quickly and efficiently with Python.

![FastAPI](images/fastapi.png)

It is designed for:

- Fast development
- Clean code structure
- Automatic API documentation
- Async support
- High performance similar to Node.js and Go

FastAPI is widely used for:

- Backend development
- Machine Learning APIs
- AI applications
- Microservices
- Real-time applications

#### One of the best features of FastAPI is its simplicity and developer-friendly experience, making it a great choice for beginners as well as production-grade systems.

## Technical Architecture

- FastAPI is built upon two core libraries

![Technical Architecture](images/starlette_and_pydantic.png)

### Starlette

- It manages how your API receives requests and sends back responses.
- Starlette is a lightweight ASGI framework/toolkit that provides the core building blocks for modern async web applications and APIs.

- FastAPI is built on top of Starlette, which is why FastAPI applications are fast, scalable, and support asynchronous programming.

#### Features

- Lightweight and minimal
- ASGI support
- Async request handling
- Routing and middleware support
- High performance backend foundation

### Pydantic

- It is used to check if the data coming into your API is correct and in the right format.
- Pydantic is a powerful Python library used for data validation and settings management using Python type hints.

- FastAPI uses Pydantic internally for request validation, response models, and automatic data parsing.

#### Features

- Automatic data validation
- Type-safe request handling
- JSON serialization
- Clean schema generation
- Easy integration with FastAPI

## Philosophy of FastAPI

- FastAPI is built on two primary pillars: Performance and Development Speed.

![Philosophy of FastAPI](images/two_primary_pillars.png)

### Fast to Run

- Unlike older, synchronous frameworks like Flask (which use WSGI), FastAPI utilizes ASGI (Asynchronous Server Gateway Interface) and the Uvicorn server to handle concurrent requests efficiently.
- It also supports async/await syntax, allowing the application to process other tasks while waiting for I/O operations (like model predictions), which significantly reduces latency.

### Fast to Code

- The framework is designed for developer productivity.
- It leverages Pydantic for automatic, type-hinted data validation and includes built-in, interactive API documentation (Swagger UI) that updates automatically as you define your endpoints.

## Why FastAPI is Fast to Run?

### Web Server → SGI → API Flow

![Web Server → SGI → API Flow](images/Fast_to_Run1.png)

This flowchart explains how a request moves through a Python web application architecture.

1. The client sends an HTTP request to the web server.
2. The SGI layer acts as the communication bridge between the server and application code.
3. The API processes the request logic.
4. A JSON response is returned back to the client.

This architecture helps separate:

- Request handling
- Application logic
- Response generation

It is commonly used in backend systems, ML APIs, and modern web applications.

### Flask vs FastAPI Architecture

This comparison highlights the difference between traditional synchronous frameworks like Flask and asynchronous frameworks like FastAPI.

![Flask vs FastAPI Architecture](images/Fast_to_Run1.png)

#### Flask (WSGI)

- Uses synchronous request handling
- Processes one request at a time per worker
- Built on WSGI and Werkzeug
- Commonly served using Gunicorn

#### FastAPI (ASGI)

- Supports asynchronous programming
- Handles multiple requests efficiently
- Built on ASGI and Starlette
- Commonly served using Uvicorn

FastAPI provides better performance and scalability for modern APIs, especially in real-time systems, AI applications, and high-concurrency backend services.

## Why FastAPI is Fast to Code?

- Automatic Input Validation.
- Auto-Generated Interactive Documentation.
- Seamless Integration with Modern Ecosystem (ML/DL Libraries, OAuth, JWT, SQL Alchemy, Docker, Kubernetes etc.)
