# DevOps with Docker: Docker Compose, Fall 2026

Exercise layout and tests are copied from the official course template:
https://github.com/docker-hy/exercises-docker-compose

## Completed exercises

- `2_01`: writes the simple service logs to `log.txt` through a bind mount.
- `2_02`: runs the simple HTTP service at http://localhost:8080.
- `2_03-10`: Compose project for exercise 2.3, frontend at
  http://localhost:5001 and backend at http://localhost:8080.

Run `docker compose up -d` from the corresponding exercise directory.
Before the first run of 2.1, create an empty `log.txt` in `2_01` with
`touch log.txt` (PowerShell: `New-Item -ItemType File log.txt`). The official
test creates this file automatically; generated logs are ignored by Git.
Stop the project with `docker compose down`. Exercises 2.2 and 2.3 use
the same host port 8080, so stop one before starting the other.

## Build and publish the example project images

From this repository's root:

```sh
docker build -t jhlow0106/compose-frontend:latest example-app/frontend
docker build -t jhlow0106/compose-backend:latest example-app/backend
docker push jhlow0106/compose-frontend:latest
docker push jhlow0106/compose-backend:latest
```

The Compose file uses the public images. Later exercises update the same
`2_03-10` directory; their tests may fail until those exercises are completed.
