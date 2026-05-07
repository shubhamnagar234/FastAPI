from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Shubham', 'Arun'])]
    email: EmailStr
    linkedin_url: HttpUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]


def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated into database')

patient_info = {
    'name': 'shubham', 
    'email': 'abc@gmail.com', 
    'linkedin_url': 'https://linkedin.com/in/shubham', 
    'age': '20', 
    'weight': 60,
    'married': False,
    'allergies': ['dust', 'oil'],
    'contact_details': {'phone': '9876543210'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)