FROM python:3.11-slim-bookworm

RUN pip install fastapi
COPY main.py /src/
WORKDIR /src/
CMD fastapi run --port 7000 main.py

LABEL racetrack-component="job"
