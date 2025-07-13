# ✅ ToDo App — Frontend & Backend with GitHub Container Registry Integration

This project is a full-stack emergency response application built with a containerized architecture. It consists of:

- **Frontend**: Static web interface served by an NGINX container.
- **Backend**: Python (FastAPI or Flask) API structured as a Python package in `src/mysite/`.

Docker is used to containerize both services, and GitHub Actions automates the CI pipeline to push images to **GitHub Container Registry (GHCR)**.

---

## 📁 Project Structure

```
myproject/
├── frontend/
│   ├── Dockerfile
│   └── static/
│       └── index.html
├── backend/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── src/
│       └── mysite/
│           ├── __init__.py
│           └── main.py
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── docker.yml
```

---

## 🐳 Docker Setup

### 🔧 Build Images Locally

**Frontend:**

```bash
docker build -t ghcr.io/ob-adams/frontend:latest ./frontend
```

**Backend:**

```bash
docker build -t ghcr.io/ob-adams/backend:latest ./backend
```

### 🚀 Run Locally

**Frontend (NGINX):**

```bash
docker run -d -p 8080:80 ghcr.io/ob-adams/frontend:latest
```

Access via: http://localhost:8080

**Backend (Python API)** — assuming FastAPI or Flask entrypoint in `main.py`:

```bash
docker run -d -p 8000:8000 ghcr.io/ob-adams/backend:latest
```

Access via: http://localhost:8000

---

## 📦 Running with Docker Compose

This project supports Docker Compose to simplify development and orchestration.

### ▶️ Start the Services

Run in detached mode:

```bash
docker-compose up -d
```

Or run in the foreground (shows logs):

```bash
docker-compose up
```

### 🛑 Stop the Services

```bash
docker-compose down
```

### 📂 File Overview

- `docker-compose.yml` – defines the multi-container stack with shared networks/volumes
- `frontend/`, `backend/` – contain service-specific Dockerfiles

### 🐳 Common Commands

| Task                  | Command                           |
| --------------------- | --------------------------------- |
| Build images only     | `docker-compose build`            |
| View logs             | `docker-compose logs -f`          |
| Restart a service     | `docker-compose restart <name>`   |
| Run a one-off command | `docker-compose exec <name> bash` |

---

## ⚙️ GitHub Actions + GHCR

A GitHub Actions workflow is defined to automatically:

1. Build Docker images for both frontend and backend
2. Push them to GHCR at `ghcr.io/ob-adams`

### 🔐 Permissions

The workflow uses the built-in `GITHUB_TOKEN` and `docker/login-action@v3` to authenticate securely.

### 📍 Workflow Location

`.github/workflows/docker.yml`

### ✅ How It Works

- Trigger: Push to `main` branch
- Steps:
  - Lowercase your GitHub username
  - Login to GHCR
  - Build frontend and backend images
  - Push images to:
    - `ghcr.io/ob-adams/frontend:latest`
    - `ghcr.io/ob-adams/backend:latest`

---

## 🧠 Backend Entrypoint Notes

If you're using FastAPI, make sure your `main.py` in `src/mysite/` contains something like:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend is live"}
```

And your `Dockerfile` CMD should point to it like:

```Dockerfile
CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

If using Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is live"
```

And use:

```Dockerfile
CMD ["python", "-m", "mysite.main"]
```

---

## 📦 View and Manage Packages

### 🔗 Package Dashboard

https://github.com/users/ob-adams/packages

### 🛡️ Change Visibility (Public / Private)

1. Go to the image (frontend or backend)
2. Click ⚙️ Package Settings
3. Toggle **Package visibility**

---

## 🧪 Test Pulling Images

From any machine with Docker:

```bash
docker pull ghcr.io/ob-adams/frontend:latest
docker pull ghcr.io/ob-adams/backend:latest
```

If the images are private, authenticate:

```bash
echo YOUR_GITHUB_PAT | docker login ghcr.io -u ob-adams --password-stdin
```

---

## 🌍 Deployment Use Cases

These images can now be used in:

- Kubernetes pods:

```yaml
image: ghcr.io/ob-adams/frontend:latest
```

- CI/CD pipelines
- Fly.io, Railway, Render
- GitHub Codespaces

---

## 💡 Future Improvements

- ✅ Auto-versioning tags (e.g., `v1.0.0`, commit SHA)
- ✅ Combine with `docker-compose.yml`
- ☁️ Deploy to Kubernetes with Helm
- 🔐 Add JWT or OAuth authentication in backend
- 🧭 Add Google Maps API to frontend for real-time tracking

---

## 👨‍💻 Author

- GitHub: [@ob-adams](https://github.com/ob-adams)

---

## 🧠 TL;DR

- This app is split into `frontend/` and `backend/` with separate Dockerfiles
- Backend follows a proper Python package structure under `src/`
- GitHub Actions pushes both images to `ghcr.io/ob-adams`
- You can now use `docker-compose up -d` to run the entire stack locally
- Images can be pulled or deployed anywhere Docker is supported

---

## 📜 License

MIT License. See `LICENSE` file.
