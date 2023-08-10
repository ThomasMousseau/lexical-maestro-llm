FROM python:latest

RUN mkdir /app

# exceptions are in the .dockerignore file
#COPY .. /app

COPY pyproject.toml /app
COPY /db /app
COPY /models /app
COPY /source_documents /app
COPY .env /app
COPY controller.py /app
COPY ingest.py /app
COPY privateGPT.py /app
copy constants.py /app

WORKDIR /app

#Idealy poetry should be directly in the parent docker image 
RUN pip install poetry

RUN poetry config virtualenvs.create false 
RUN poetry install --only main

CMD ["python", "ingest.py"]
CMD ["python", "controller.py"]