@app.post("/register")
def register_user(user_name= Body(), password=Body()):
    if functions.register_user(user_name=user_name,password=password):
        return{"message":"user registered successfully"}
    raise HTTPException(status_code=400, detail="user already exists")