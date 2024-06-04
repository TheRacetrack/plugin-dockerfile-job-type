import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/live")
def live_endpoint():
    return {
        'deployment_timestamp': int(os.environ.get('JOB_DEPLOYMENT_TIMESTAMP', 0)),
    }


@app.get("/ready")
def ready_endpoint():
    return {}


class PerformPayload(BaseModel):
    numbers: list[float]


@app.post("/pub/job/{job_name}/{job_version}/perform")
def perform_endpoint(job_name: str, job_version: str, payload: PerformPayload):
    return sum(payload.numbers)
