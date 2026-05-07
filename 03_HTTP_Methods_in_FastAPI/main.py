import json
from fastapi import FastAPI

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get("/")
def project():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {"message": "A fully functional patient management system"}

@app.get("/view")
def view():
    data = load_data()
    return data