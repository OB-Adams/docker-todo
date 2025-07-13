# ✅ ToDo App — Frontend, Backend & MongoDB with GHCR + Docker Hub

This project is a full-stack emergency response application built with a containerized architecture. It consists of:

- **Frontend**: Static web interface served by an NGINX container
- **Backend**: Python API (FastAPI or Flask) in `src/mysite/`
- **Database**: MongoDB container with persistent volume for data storage

It supports container image hosting via both:

- 🐳 **Docker Hub** (`obobob/todo-frontend`, `obobob/todo-backend`)
- 🐙 **GitHub Container Registry (GHCR)** (auto-pushed via GitHub Actions)

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

## 📦 Docker Compose Setup

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

## 🗃️ MongoDB with Persistent Storage

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

To access shell:

```bash
docker exec -it mysite-mongodb mongosh
```

---

## 🚀 Manual Docker Build & Run

### Build Locally

```bash
docker build -t obobob/todo-frontend:latest ./frontend
docker build -t obobob/todo-backend:latest ./backend
```

### Run Locally

```bash
docker run -d -p 8080:80 obobob/todo-frontend:latest
docker run -d -p 8000:8000 obobob/todo-backend:latest
```

---

## 🐳 Docker Hub

- Frontend: [`obobob/todo-frontend`](https://hub.docker.com/r/obobob/todo-frontend)
- Backend: [`obobob/todo-backend`](https://hub.docker.com/r/obobob/todo-backend)

### Pull Images

```bash
docker pull obobob/todo-frontend:latest
docker pull obobob/todo-backend:latest
```

### Push Images (manual)

```bash
docker push obobob/todo-frontend:latest
docker push obobob/todo-backend:latest
```

---

## 🐙 GitHub Container Registry (GHCR)

Your GitHub Actions workflow auto-builds and publishes Docker images to:

- `ghcr.io/ob-adams/frontend:latest`
- `ghcr.io/ob-adams/backend:latest`

### Pull from GHCR

```bash
docker pull ghcr.io/ob-adams/frontend:latest
docker pull ghcr.io/ob-adams/backend:latest
```

### Private Access

```bash
echo <YOUR_TOKEN> | docker login ghcr.io -u ob-adams --password-stdin
```

### Make Public (optional)

1. Go to: [https://github.com/users/ob-adams/packages](https://github.com/users/ob-adams/packages)
2. Click the image → ⚙️ → Change visibility to **Public**

---

## ⚙️ GitHub Actions Workflow

`.github/workflows/docker.yml`

This builds images on `push` to `main`:

```yaml
docker build -t ghcr.io/<owner>/frontend ./frontend
docker build -t ghcr.io/<owner>/backend ./backend
docker push ghcr.io/<owner>/frontend
docker push ghcr.io/<owner>/backend
```

No secrets needed — uses `${{ secrets.GITHUB_TOKEN }}` for auth.

---

## 🧪 API Testing

FastAPI Swagger UI:

```bash
http://localhost:8000/docs
```

Example:

```json
POST /todos
{
  "content": "Buy milk"
}
```

---

## 🧠 Entrypoint Examples

**FastAPI:**

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend is running"}
```

**Docker CMD:**

```Dockerfile
CMD ["uvicorn", "mysite.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🔧 Useful Commands

| Task                | Command                                |
| ------------------- | -------------------------------------- |
| Build only          | `docker compose build`                 |
| View logs           | `docker compose logs -f`               |
| Exec into container | `docker compose exec -it backend bash` |
| Restart service     | `docker compose restart backend`       |

---

## 🧭 Roadmap

- [ ] Add JWT/OAuth2 authentication
- [ ] Add Google Maps API integration
- [ ] Enable auto-versioning (`v1.0.0`, Git SHA)
- [ ] Helm charts for Kubernetes
- [x] GHCR workflow
- [x] Docker Hub integration

---

## 👨‍💻 Author

- GitHub: [@ob-adams](https://github.com/ob-adams)

---

## 🧠 TL;DR

- 🐳 Built with Docker + Compose
- 📦 MongoDB volume for data persistence
- 🚀 GHCR (auto) + Docker Hub (manual)
- 🔁 GitHub Actions handles CI/CD
- 🔥 Deployable to any container platform

---

## 📜 License

MIT — See `LICENSE`
