# base image
FROM python:3.9-slim

# workdir
WORKDIR /app

# copy
COPY . /app

# run
RUN pip install -r requirements.txt

# command
CMD ["python", "./app.py"]
# CMD ["streamlit", "run", "./app.py"]