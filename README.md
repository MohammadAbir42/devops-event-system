# DevOps Event System

A DevOps-focused backend system demonstrating real-world practices including **layered architecture**, **event-driven design**, and **observability**.

---

## 🚀 Features

- **Layered FastAPI architecture** (Controller → Service → Repository → Model)
- **Event-driven design** for tracking system activity
- **Prometheus metrics integration** for monitoring
- **Grafana dashboards** for visualization
- **Docker-based local environment**
- **Nginx reverse proxy setup**
- **CI/CD pipeline with GitHub Actions**
- **DevLog** for documenting progress and decisions

---

## 🧩 Architecture Overview
# DevOps Event System

A DevOps-focused backend system demonstrating real-world practices including **layered architecture**, **event-driven design**, and **observability**.

---

## 🚀 Features

- **Layered FastAPI architecture** (Controller → Service → Repository → Model)
- **Event-driven design** for tracking system activity
- **Prometheus metrics integration** for monitoring
- **Grafana dashboards** for visualization
- **Docker-based local environment**
- **Nginx reverse proxy setup**
- **CI/CD pipeline with GitHub Actions**
- **DevLog** for documenting progress and decisions

---

## 🧩 Architecture Overview
Frontend → Python API → Database
↘ Prometheus → Grafana
Node.js Alert Service → Optional analytics

---

## 📂 Project Structure

- `python-api/`: FastAPI backend
- `nodejs-alert-service/`: Node.js alert/analytics service
- `nginx/`: Reverse proxy configuration
- `prometheus/`: Prometheus configuration
- `grafana/`: Grafana dashboards
- `DevLog/`: Development logs and design decisions
- `README.md`: Project description
- `.gitignore`: Ignored files

---

## 📊 Observability

- Metrics exposed via `/metrics` endpoint  
- Prometheus scrapes the metrics regularly  
- Grafana visualizes system behavior

---

## ⚙️ Local Setup

1. Clone repo:

```bash
git clone https://github.com/<your-username>/devops-event-system.git
cd devops-event-system
```

2. Create virtual environment (Python):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Python API locally:

```bash
uvicorn python-api.main:app --reload
```

5. Access Swagger docs:

```bash
http://127.0.0.1:8000/docs
```

## 📝 DevLog

See `/DevLog` for daily development progress, design decisions, and trade-offs.

- [0001: Kickstarting DevOps Practice Project](./DevLog/0001_kickstart_project.md)

---

## 🎯 Purpose

- Practice DevOps concepts in a local environment
- Create a **reusable backend template**
- Demonstrate **real-world architecture** to recruiters

---

## 🔮 Future Improvements

- Add Kubernetes deployment
- Cloud deployment (AWS)
- Advanced alerting system
- Enhanced metrics analytics