# Racetrack Plugin: Dockerfile Job Type

This is a plugin for [Racetrack](https://github.com/TheRacetrack/racetrack)
which extends it with Dockerfile-based Job Type.

With Dockerfiles, you can deploy any image to Racetrack
as long as it handles HTTP calls and adheres to [few rules](https://theracetrack.github.io/racetrack/docs/development/plugins-job-types/#wrapper-principles).

"dockerfile" job type itself is dead simple. It basically says that a Dockerfile will be provided by a Job, in its main directory.

It's intended to handle the HTTP calls to your Web server written 
in any programming language, enclosed in a docker image by Dockerfile recipe.

## Setup
1. Install `racetrack` client and generate ZIP plugin by running `make bundle`.

2. Activate the plugin in Racetrack Dashboard Admin page
  by uploading the zipped plugin file.

## Usage
You can deploy [sample Dockerfile job](./sample/dockerfile-python) by running:
```bash
racetrack deploy sample/dockerfile-python
```

# Development
Setup & activate Python venv (this is required for local development):

```bash
# in a project-root directory
make setup
. venv/bin/activate
```

# Releasing a new version
1. Make sure you have latest `racetrack` client.
2. Change the current version in a [plugin-manifest.yaml](./src/plugin-manifest.yaml)
3. Create ZIP plugin: `make bundle`
