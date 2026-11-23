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

3. Login page

5. Expense dashboard

6. Error message

8. Working API endpoint in `/docs`

10. Successful GitHub Actions run

## 7. Known Issues

- [Mention any issues in the application.]
- [Mention features that need improvement.]

