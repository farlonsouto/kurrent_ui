# Kurrent OCR Web UI 📜

A lightweight, modern web interface for the **Kurrent OCR Engine**. This project provides a user-friendly way to upload 18th-century German handwritten records and receive high-accuracy transcriptions powered by the **TrOCR** architecture.

## 🚀 Overview

This repository serves as the frontend component of a decoupled microservices architecture. It communicates via REST API with the(https://github.com).

### Key Features
- **Asynchronous Processing:** Handles image uploads and transcription requests without blocking.
- **Production Ready:** Fully containerized using Docker for consistent deployment.
- **Modern Stack:** Built with Streamlit for rapid, data-centric interface development.

---

## 🛠️ Tech Stack

- **Interface:** [Streamlit](https://streamlit.io)
- **API Communication:** Python `Requests`
- **Environment Management:** Conda / YAML
- **Containerization:** Docker & Docker Compose

---

## 🏃 Quick Start

### Option 1: Using Docker (Recommended)
Ensure the backend is running at `http://localhost:8000`, then run:

```bash
docker-compose up --build

