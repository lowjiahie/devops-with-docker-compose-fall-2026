# Exercise 2.11: my containerized development environment

I added a Docker Compose development environment to Docker Quick Reference,
the Python application created for exercise 1.15 and deployed in exercise 1.16.
The original project is available at
https://github.com/lowjiahie/devops-with-docker-fall-2026/tree/main/1_15.
This directory contains a copy of its application source and the development
configuration, so a fresh clone of this repository is sufficient.

## Start developing

From this directory, run:

```sh
docker compose up --build -d
docker compose logs -f
```

Open http://localhost:18091. The health endpoint is
http://localhost:18091/health and returns `{"status": "ok"}`.
Only Docker and a text editor are needed on the host; Python runs inside
the container and the application has no third-party Python dependencies.

Edit a command or heading in `app.py`, save it, and refresh the browser.
Compose bind mounts the host file read-only into `/app/app.py`.
The development runner polls its contents every 0.5 seconds, restarts the
Python child process when the file changes, and stops it on shutdown.
Polling also works with Windows bind mounts without relying on filesystem
notification forwarding. No image rebuild or container recreation is needed
for changes to `app.py`. Changes to `dev.py` or the Dockerfile require
`docker compose up --build -d`.

The image runs as an unprivileged user. The development port is bound to
localhost. This reloader is for local development; the earlier cloud
deployment continues to use the application directly.

Stop the environment with `docker compose down`.

## Validation

I built and started the environment, checked the home page and health
endpoint, edited the host application's heading, and confirmed that the new
heading appeared in the HTTP response without rebuilding or recreating the
container. Restoring the original file triggered another reload. The
container ID stayed the same during both changes, and the health check
reported healthy.
