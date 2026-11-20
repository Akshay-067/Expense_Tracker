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


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)


Base.metadata.create_all(engine)


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
