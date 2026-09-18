# Hairdresser Web App

A simple CMS web app built with Django and Docker.

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting started

**1. Create your `.env` file**

Copy the variables below into a file called `.env` in the root of the project and fill in your values:

```
DB_NAME=hairdresser
DB_USER=hairdresser
DB_PASSWORD=hairdresser
DB_HOST=db
SECRET_KEY=your-secret-key-here
DEBUG=True
```

> The `.env` file is listed in `.gitignore` — it will never be committed to git. This is intentional: it contains secrets (passwords, keys) that should not be shared.

**2. Build the image**

This reads the `Dockerfile` and installs all dependencies (like `pip install`).
```bash
docker-compose build
```

**3. Start the server**

This starts both the database (`db`) and the web app (`web`). Migrations run automatically before the server starts.
```bash
docker-compose up
```

App runs at http://localhost:8000

---

## Running Django commands

Django and Python live inside the Docker container, not on your machine. You have two ways to run commands inside the container:

### `docker-compose exec` — use this when the server is already running

`exec` runs a command inside a container that is **already up**. Think of it like opening a second terminal window inside the running container.

```bash
docker-compose exec web python manage.py <command>
```

### `docker-compose run` — use this when the server is stopped

`run` spins up a **brand new** container just to run that one command, then stops it. Slower, and should only be used when `docker-compose up` is not already running.

```bash
docker-compose run web python manage.py <command>
```

**Rule of thumb:** if `docker-compose up` is running in a terminal, use `exec`. If not, use `run`.

---

## Common Django commands

| What you want to do | Command (server running) |
|---|---|
| Create an admin user | `docker-compose exec web python manage.py createsuperuser` |
| Create migrations after changing a model | `docker-compose exec web python manage.py makemigrations` |
| Apply migrations to the database | `docker-compose exec web python manage.py migrate` |
| Start a new Django app | `docker-compose exec web python manage.py startapp <appname>` |

## Common Docker commands

| Command | What it does |
|---|---|
| `docker-compose up` | Start all services (db + web) |
| `docker-compose down` | Stop all services |
| `docker-compose build` | Rebuild the image (run after changing `requirements.txt` or `Dockerfile`) |
| `docker-compose restart web` | Restart only the web container |
| `docker-compose logs web` | See the web container's output |
