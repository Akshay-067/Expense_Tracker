from sqlalchemy import Integer, String, Boolean, Column, DateTime, create_engine, inspect, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime,timedelta,timezone
import jwt 
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph=PasswordHasher()
DB_PATH = "library.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRY=7*24*60
SECRET_KEY ="SECRET067"
ALGORITHM = "HS256"
    
class customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    created_at = Column(Integer)

class expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("customers.id"))
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    expense_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)


Base.metadata.create_all(engine)

def get_expenses(user_id):
    session = Session(engine)
    query = session.query(expense).filter(expense.user_id == user_id)

    response = []

    for item in query.all():
        response.append({
            "id": item.id,
            "title": item.title,
            "amount": item.amount,
            "category": item.category,
            "expense_date": item.expense_date,
            "created_at": item.created_at
        })

    session.close()
    return response

def add_expense(user_id, title, amount, category, ):
    session = Session(engine)
    new_expense = expense(user_id=user_id, title=title, amount=amount, category=category, expense_date=datetime.now(),created_at=datetime.now())
    session.add(new_expense)
    session.commit()
    response = {
        "id": new_expense.id,
        "title": new_expense.title,
        "amount": new_expense.amount,
        "category": new_expense.category,
        "expense_date": new_expense.expense_date,
        "created_at": new_expense.created_at
    }
    session.close()
    return response 


def verify_login(username, password):
    session=Session(engine)
    user=session.query(User).filter_by(user_name=username).first()
    if user is None:
        session.close()
        return False
    try:
        ph.verify(user.password,password)
    except VerifyMismatchError:
        session.close()
        return False
    session.close()
    access_token=create_token(username=username,token_type="access")
    refresh_token=create_token(username=username,token_type="refresh")
    return {"access_token":access_token,"refresh_token":refresh_token}
        
    
    
def create_token(username,token_type):
    time=ACCESS_TOKEN_EXPIRE_MINUTES
    if token_type == "refresh":
        time=REFRESH_TOKEN_EXPIRY
    payload = {
        "username": username,
        "token_type": token_type,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=time)

    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token( token, token_type):
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return False   
    if payload["token_type"] == token_type:
        return payload["username"]
    return False

def register_user(user_name:str,password:str):
    session = Session(engine)
    user_exists=session.query(User).filter_by(user_name=user_name).first()
    if user_exists is not None:
        session.close()
        return False
    session.add(User(user_name=user_name,password=ph.hash(password)))
    session.commit()
    session.close()
    return True