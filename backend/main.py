from fastapi import FastAPI, HTTPException, Header, Body
import functions
from datetime import date

app = FastAPI()

@app.post("/register")
def register_user(user_name=Body(), password=Body()):
    if functions.register_user(user_name=user_name, password=password):
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=409, detail="User already exists")

@app.post("/login")
def login(username=Body(), password=Body()):
    token = functions.verify_login(username=username, password=password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return token

@app.post("/refresh")
def refresh_token(refresh_token=Header(None)):
    username = functions.verify_token(token=refresh_token, token_type="refresh")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
    access_token = functions.create_token(username=username, token_type="access")
    return {"access_token": access_token}

@app.get("/expenses")
def get_expenses(user_id: int, token=Header(None)):
    username = functions.verify_token(token=token, token_type="access")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired access token")
    return functions.get_expenses(user_id=user_id)

@app.post("/expenses")
def add_expense(user_id: int, title: str, amount: float, category: str, expense_date: date, token=Header(None)):
    username = functions.verify_token(token=token, token_type="access")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired access token")
    if amount <= 0:
        raise HTTPException(status_code=422, detail="Amount must be greater than zero")
    return functions.add_expense(user_id=user_id,title=title,amount=amount,category=category,expense_date=expense_date)