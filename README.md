# DevOps Event System

A DevOps-focused backend system implementing production-inspired practices including **layered architecture**, **event-driven design**, and **observability**.

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
Node.js Alert Service → Handles alerting and analytics processing

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

- Application exposes metrics via `/metrics` endpoint  
- Prometheus scrapes and stores time-series data  
- Grafana dashboards provide real-time system observability and insights

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

- Apply DevOps practices in a local, production-like environment 
- Build a reusable and extensible backend service foundation  
- Implement real-world architecture patterns including service isolation, observability, and reverse proxying  

---

## 🔮 Future Improvements

- Introduce container orchestration using Kubernetes 
- Deploy infrastructure on AWS (ECS/EKS + CI/CD integration)
- Implement alerting with threshold-based and event-driven triggers 
- Expand observability with distributed tracing and log aggregation  

---

## 🧠 Design Goals

- Maintain clear separation of concerns using layered architecture
- Ensure observability across services
- Keep the system modular and extensible
- Simulate production-like DevOps workflows locally 