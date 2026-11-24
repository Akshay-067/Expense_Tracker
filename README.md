# Expense Tracker

A simple expense tracking application built using FastAPI, SQLite and React.

## 1. Project and Team

**Project Name:** Expense Tracker

**Technologies:**
- Frontend: React
- Backend: FastAPI (Python)
- Database: SQLite
- Authentication: JWT
- Password Hashing: Argon2
- Deployment: Docker and AWS EC2

**Team Members:**

| Member | Name | Contribution |
|---|---|---|
| Member 1 | Bhuvan | docker |
| Member 2 | Akshay | function |
| Member 3 | Jashan | main |

## 2. Live App

**EC2 Public Link:** [Paste your link here]

## 3. How to Run It

### Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

API documentation:

`http://127.0.0.1:8001/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker build -t expense-tracker .
docker run -p 8001:8001 expense-tracker
```

## 4. API Contract

| ID | Method | Path | Request Body | Status |
|---|---|---|---|---|
| A1 | POST | /auth/register | username, email, password | 201 |
| A2 | POST | /auth/login | email, password | 200 |
| A3 | POST | /auth/refresh | refresh_token | 200 |
| E1 | GET | /expenses | JWT token | 200 |
| E2 | POST | /expenses | title, amount, category, expense_date | 201 |

### Error Rules

| Error | Status Code |
|---|---|
| Email already exists | 409 |
| Incorrect login details | 401 |
| Invalid or expired token | 401 |
| Missing required fields | 422 |
| Invalid email | 422 |
| Invalid expense amount | 422 |

## 5. Database

Database name: `expenses.db`

**Users Table**

| Column |
|---|
| id |
| username |
| email |
| hashed_password |
| created_at |

**Expenses Table**

| Column |
|---|
| id |
| user_id |
| title |
| amount |
| category |
| expense_date |
| created_at |

## 6. Screenshots

Add the following screenshots:

1. Registration page

3. Login page<img width="1600" height="899" alt="WhatsApp Image 2026-11-23 at 4 25 18 PM" src="https://github.com/user-attachments/assets/59b7e99d-578e-4840-91b7-7a786293567c" />


5. Expense dashboard<img <img width="677" height="472" alt="image" src="https://github.com/user-attachments/assets/59b8e366-647d-42fd-9a4e-6215846161f1" />
  


6. Error message<img width="1735" height="152" alt="image" src="https://github.com/user-attachments/assets/d0d70e29-13f4-45a5-90b2-c1a6ffa000e1" />


8. Working API endpoint in `/docs`<img width="1847" height="652" alt="image" src="https://github.com/user-attachments/assets/ebaf55b1-359b-4def-afd0-44937e73edca" />


10. Successful GitHub Actions run<img width="1280" height="659" alt="WhatsApp Image 2026-11-23 at 4 34 57 PM" src="https://github.com/user-attachments/assets/52e1564a-99d2-49b0-a43b-3123a72d054f" />


## 7. Known Issues



