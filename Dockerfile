FROM python:latest

RUN mkdir /app

COPY pyproject.toml /app
COPY /db /app
COPY /models /app
COPY /source_documents /app
COPY .env /app
COPY controller.py /app
COPY ingest.py /app
COPY privateGPT.py /app

WORKDIR /app

#Idealy poetry should be directly in the parent docker image 
RUN pip install poetry

#false
RUN poetry config virtualenvs.create true 
RUN poetry install --only main

CMD ["python", "controller.py"]