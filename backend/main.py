from fastapi import FastAPI, HTTPException,Header,Body
from fastapi.middleware.cors import CORSMiddleware
import functions    
from pydantic import BaseModel

app = FastAPI()


@app.post("/login")
def login(username= Body(), password= Body()):
    token = functions.verify_login(username=username, password=password)
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return token

@app.post("/refresh")
def refresh_token(refresh_token=Header(None)):
    username=functions.verify_token(token=refresh_token, token_type="refresh")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")
    access_token = functions.create_token(username=username, token_type="access")
    return {"access_token": access_token}
