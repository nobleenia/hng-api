# HNG12 Stage 0 - Public API

This is a simple **public API** built using **Django and Django REST Framework** for the **HNG12 Stage 0 task**.

## 🚀 API Features
- Returns:
  - Your **registered email**.
  - The **current datetime** in **ISO 8601 UTC format**.
  - Your **GitHub repository URL**.
- **Deployed publicly** (on Render.com).
- **Fast response time (<500ms).**

---

## 🔧 Setup Instructions (Run Locally)
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/nobleenia/hng-api.git
cd hng-api
```

### 2️⃣ **Create and Activate a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Start the Django Server**
```bash
python manage.py runserver
```

### 6️⃣ **Test the API**
Open in your browser or run:
```bash
curl http://127.0.0.1:8000/
```

Expected Response:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/nobleenia/hng-api"
}
```

---

## 🌐 **API Documentation**
### **📍 Endpoint**
`GET /`

### **🔹 Response Format**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/nobleenia/hng-api"
}
```

### **🔹 Example Usage**
```bash
curl https://hng-api.onrender.com/
```

---

## 🔗 Python Developers Backlink
Looking to hire Python developers? Check:  
👉 [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

## ✅ **Deployment**
The API is deployed on **Render** and publicly accessible at:  
👉 `https://hng-api-daxd.onrender.com`

---

## 📜 **License**
This project is open-source and available under the **MIT License**.