# Pydantic Crash Course | Data Validation in Python

![Pydantic](images/pydantic.png)

#### Pydantic helps you define clear, type-safe data models and automatically validates the data—saving you tons of time.

#### Pydantic, a powerful Python library designed for data validation and building type-safe data models.

#### Pydantic is essential for production-grade software by solving issues related to dynamic typing and manual validation boilerplate.

## How Pydantic Works

- A three-step process involving model definition, instantiation for automatic validation, and implementation in functions.

- 1. **Define a Pydantic model** that represents the **ideal schema** of the data.
  - This includes the expected fields, their types, and any validation contraints (e.g., **gt=0** for the positive numbers).

- 2. **Instantiate the model with raw input data** (usually a dictionary or JSON-like structure).
  - Pydantic will automatically **validate** the data and **coerce** it into the correct Python types (if possible).
  - If the data doesn't meet the model's requirements, Pydantic raises a **ValidationError**.

- 3. **Pass the validated model object** to function or use it throughout your codebase.
  - This ensures that every part og your program works with **clean, type-safe, and logically valid data**.

## Advanced Validation Features

### Field Validators

- To apply specific, custom logic to individual fields using the @field_validator decorator.

### Model Validators

- Handling cross-field dependencies, where validation for one field depends on another.

### Computed Fields

- Dynamically calculating values (e.g., BMI) based on other model fields.

### Nested Models

- Organizing complex data structures by nesting one Pydantic model within another.

## Serialization

- To export your Pydantic objects into standard Python dictionaries or JSON formats, including options to control specific fields with include, exclude, and exclude_unset.
