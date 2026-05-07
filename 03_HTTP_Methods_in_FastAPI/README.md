# HTTP Methods in FastAPI

## Static vs Dynamic Websites

Software applications can generally be divided into two categories:

- Static Websites
- Dynamic Websites

![Static vs Dynamic Websites](images/software_types.png)

### Static Websites

Static websites display fixed content and usually do not change frequently.

Examples:
- Blogs
- Portfolio websites
- Government websites
- Documentation pages

### Dynamic Websites

Dynamic websites generate content dynamically based on user interactions and database operations.

Dynamic applications commonly perform CRUD operations:

- Create
- Read
- Update
- Delete

Examples:
- Social media platforms
- E-commerce websites
- Banking applications
- Dashboard systems

![Static vs Dynamic Websites' Examples](images/examples.png)

## Client and Server Communication

This architecture demonstrates how clients communicate with servers using the HTTP protocol.

### Flow

1. Client sends an HTTP request
2. Server processes the request
3. Server returns a response back to the client

The website server can serve:
- Static content
- Dynamic content

Dynamic systems usually interact with databases and business logic to perform operations like creating, updating, reading, or deleting data.

![Client and Server Communication](images/website_flow.png)

## HTTP Methods (HTTP Verbs)

HTTP methods define the type of operation performed on a resource.

### GET

Used to retrieve data from the server.

Example:
- Fetch user details
- Read blog posts

---

### POST

Used to send new data to the server.

Example:
- Create a new user
- Submit a form

---

### PUT

Used to update existing data.

Example:
- Update profile information
- Edit product details

---

### DELETE

Used to remove data from the server.

Example:
- Delete a user
- Remove a post

![HTTP Methods (HTTP Verbs)](images/http_methods.png)

## CRUD Operations in APIs

Most backend applications revolve around CRUD operations.

| Operation | HTTP Method | Description |
|-----------|-------------|-------------|
| Create | POST | Add new data |
| Read | GET | Retrieve data |
| Update | PUT | Modify existing data |
| Delete | DELETE | Remove data |

CRUD operations are the foundation of modern APIs and database-driven applications.
