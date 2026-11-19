# DevOps with Docker: Docker Compose, Fall 2026

Exercise layout and tests are copied from the official course template:
https://github.com/docker-hy/exercises-docker-compose

## Completed exercises

- `2_01`: writes the simple service logs to `log.txt` through a bind mount.
- `2_02`: runs the simple HTTP service at http://localhost:8080.
- `2_03-10`: the evolving project for exercises 2.3–2.10. Open
  http://localhost:8000 through Nginx. `/api/` requests go to the backend;
  other requests go to the frontend. Redis and Postgres are internal services.
  The backend waits for both database health checks before starting.
  Postgres 18 data is bound to `2_03-10/database` on the host.

Run `docker compose up -d` from the corresponding exercise directory.
Before the first run of 2.1, create an empty `log.txt` in `2_01` with
`touch log.txt` (PowerShell: `New-Item -ItemType File log.txt`). The official
test creates this file automatically; generated logs are ignored by Git.
Stop the project with `docker compose down`. The final application only
publishes Nginx's port 8000 on localhost; frontend, backend, Redis and
Postgres have no host port mappings.

## Exercise 2.11: development environment

Exercise `2_11` adds a containerized development environment for my Docker
Quick Reference application from Part 1. Its source is bind mounted and a
Python polling reloader applies saved edits without rebuilding the image.
Run `docker compose up --build -d` in `2_11` and open http://localhost:18091.
See [2_11/README.md](2_11/README.md) for setup and validation details.

## Build and publish the example project images

From this repository's root:

```sh
docker build --build-arg REACT_APP_BACKEND_URL=/api -t jhlow0106/compose-frontend:proxy example-app/frontend
docker build -t jhlow0106/compose-backend:latest example-app/backend
docker push jhlow0106/compose-frontend:proxy
docker push jhlow0106/compose-backend:latest
```

The Compose file uses public images. The `proxy` frontend tag embeds `/api`
as its backend URL, so browser requests stay on the Nginx origin. The older
`latest` frontend tag remains available for the earlier direct-port setup.

## Database persistence and tests

The database password in Compose is a local course example, not a production
credential. Postgres has no published host port. Its data directory is ignored
by Git and survives `docker compose down` followed by `docker compose up -d`.
Deleting `2_03-10/database` after stopping this exercise's containers resets
the course messages. Do not delete it when you want to keep your data.

The official 2.6 and 2.7 tests were run before adding Nginx, including message
creation, persistence after container recreation, and message loss after
deleting the test data directory. In the final proxy setup, the official
earlier-stage tests skip themselves and 2.8–2.10 test the complete stack.

## Exercise 2.5 (submitted directly in the course quiz)

Using the official `scaling-exercise` project from
https://github.com/docker-hy/material-applications/tree/main/scaling-exercise:

```sh
docker compose up -d --scale compute=3
```

Three compute instances distribute the ten calculation requests through the
provided load balancer. This exercise is separate from `2_03-10`.

For local verification, port 3000 was already occupied, so the following
`docker-compose.override.yml` was used alongside the original project's file:

```yaml
services:
  calculator:
    ports: !override
      - "127.0.0.1:3001:3000"
  load-balancer:
    ports: !override
      - "127.0.0.1:80:80"
```

The test page is then at http://localhost:3001. The application source
and compute/load-balancer configuration are unchanged.
