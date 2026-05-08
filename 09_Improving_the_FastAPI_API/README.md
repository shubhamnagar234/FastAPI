# Improving the FastAPI API

## Improvements
- Create a new folder
- Field validator for city feature
- Add routes
    - Home
    - Health
- Add Model version
- Separation of logic
    - Pydantic model
    - City tier
    - ML logic
- Try catch
- Add confidence score
- Response Model

## Response Model
- In FastAPI, a response model defines the structure of the data that our API endpoint will return.
- It helps in
    - Generating clean API docs (/docs)
    - Validating output (so our API doesn't return malformed responses).
    - Filtering unnecessary data from the response.