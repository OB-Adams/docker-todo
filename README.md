# ✅ ToDo App — Frontend, Backend & MongoDB with GitHub Container Registry Integration

This project is a full-stack emergency response application built with a containerized architecture. It consists of:

- **Frontend**: Static web interface served by an NGINX container
- **Backend**: Python API (FastAPI or Flask) in `src/mysite/`
- **Database**: MongoDB container with persistent volume for data storage

Docker Compose manages the services, and GitHub Actions pushes images to **GitHub Container Registry (GHCR)**.

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

### 🚀 Run Locally (Standalone)

**Frontend:**

```bash
docker run -d -p 8080:80 ghcr.io/ob-adams/frontend:latest
```

→ Access: http://localhost:8080

**Backend:**

```bash
docker run -d -p 8000:8000 ghcr.io/ob-adams/backend:latest
```

→ Access: http://localhost:8000

---

## 🗃️ MongoDB with Persistent Storage

MongoDB is included in `docker-compose.yml` and uses a **named volume** to persist data:

```yaml
services:
  mongodb:
    image: mongo:8.0-rc-noble
    container_name: mysite-mongodb
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

Access shell:

```bash
docker exec -it mysite-mongodb mongosh
```

---

## 📦 Running with Docker Compose

### ▶️ Start All Services

```bash
docker-compose up -d
```

### 🛑 Stop Services

```bash
docker-compose down
```

### 🧼 Cleanup Volumes

```bash
docker-compose down -v
```

---

## ⚙️ GitHub Actions + GHCR

This repo uses GitHub Actions to:

- Build backend & frontend images
- Push them to:
  - `ghcr.io/ob-adams/frontend:latest`
  - `ghcr.io/ob-adams/backend:latest`

### 📍 Workflow File

`.github/workflows/docker.yml`

### 🔐 Auth

Uses `GITHUB_TOKEN` + `docker/login-action@v3` for secure access.

---

## 🧪 API Testing

FastAPI interactive docs:

```
http://localhost:8000/docs
```

Sample `POST /todos`:

```json
{
  "content": "Buy milk"
}
```

---

## 📥 Pull from GHCR Remotely

```bash
docker pull ghcr.io/ob-adams/frontend:latest
docker pull ghcr.io/ob-adams/backend:latest
```

For private images:

```bash
echo <YOUR_TOKEN> | docker login ghcr.io -u ob-adams --password-stdin
```

---

## 📤 Push to GitHub

```bash
git add .
git commit -m "Add MongoDB with persistent Docker volume"
git push origin main
```

---

## 🌐 Deployment Options

- ✅ Kubernetes
- ✅ GitHub Codespaces
- ✅ Render, Railway, Fly.io
- ✅ Any CI/CD pipeline

---

## 🧠 Backend Entrypoint Tips

**FastAPI:**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend is running"}
```

**Dockerfile CMD:**

```Dockerfile
CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Flask:**

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask"
```

---

## 📦 Useful Docker Commands

| Task                | Command                            |
| ------------------- | ---------------------------------- |
| Build only          | `docker-compose build`             |
| View logs           | `docker-compose logs -f`           |
| Exec into container | `docker-compose exec backend bash` |
| Restart service     | `docker-compose restart backend`   |

---

## 🔒 Package Visibility

To make GHCR images public:

1. Visit: https://github.com/users/ob-adams/packages
2. Click ⚙️ on package
3. Set **Package visibility** to public

---

## 🧭 Future Roadmap

- [ ] Add JWT/OAuth2 authentication
- [ ] Add Google Maps API for frontend
- [ ] Enable auto-versioning (`v1.0.0`, commit SHAs)
- [ ] Helm charts for Kubernetes
- [x] MongoDB with Docker volumes

---

## 👨‍💻 Author

- GitHub: [@ob-adams](https://github.com/ob-adams)

---

## 🧠 TL;DR

- 💻 Split into `frontend/` (NGINX) and `backend/` (FastAPI)
- 🗃️ MongoDB included with persistent volume
- 🐳 Docker Compose manages all services
- 🏗️ CI/CD with GitHub Actions → GHCR
- 🔗 All components now work together and are deployable anywhere

---

## 📜 License

MIT License. See `LICENSE` file.
