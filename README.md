# 🚢 Titanic Data Pipeline: ETL to Dashboard
**A lightweight Proof-of-Concept (PoC) for end-to-end data engineering.**

This project serves as a technical exercise in building a complete data lifecycle. It demonstrates the ability to extract raw public data, transform it using Python, serve it via a RESTful API, and visualize results on a real-time dashboard.

## 🏗️ The Architecture
The project follows a standard 3-tier data architecture:
1.  **Data Layer (ETL):** A Python script (`etl_script.py`) that extracts the Titanic dataset from a public source, performs data cleaning (handling nulls and mapping), and loads it into a local **SQLite** database.
2.  **Service Layer (API):** A **FastAPI** backend (`api.py`) that executes SQL queries against the SQLite database to calculate survival metrics on-the-fly.
3.  **Presentation Layer (UI):** A **Streamlit** dashboard (`dashboard.py`) that consumes the API endpoints to display interactive charts.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas
* **Database:** SQLite (SQL-based persistence)
* **Backend:** FastAPI & Uvicorn
* **Frontend:** Streamlit
* **Communication:** REST API (JSON)

## 🚀 Quick Start

**1. Install Dependencies**
```bash
pip install -r requirements.txt