# Sample: Dockerfile Python Job
This job sums up given numbers.
It provides its own Dockerfile, which is being used by Racetrack when building the job.

# Deploying
Run in this directory:
```sh
racetrack deploy
```

# Calling a Job
```sh
racetrack call dockerfile-python --version=latest /perform '{"numbers":[40,2]}'
# Expect:
# 42.0
```
