FROM python:latest

RUN mkdir /app
# exceptions are in the .dockerignore file
# COPY .. /app

RUN mkdir /app/source_documents
RUN mkdir /app/models

COPY pyproject.toml /app
COPY /db /app
COPY /models /app/models
COPY /source_documents /app/source_documents
COPY .env /app
COPY controller.py /app
COPY ingest.py /app
COPY privateGPT.py /app
COPY constants.py /app

WORKDIR /app

#Idealy poetry should be directly in the parent docker image 
RUN pip install poetry

RUN poetry config virtualenvs.create false 
#THIS IS WAY TO BIG, NEED TO FIX (7GB)
RUN poetry install --only main

CMD ["python", "ingest.py"]
CMD ["python", "controller.py"]