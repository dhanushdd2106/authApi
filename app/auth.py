from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv

load_dotenv()

sec = os.getenv("SECRET_KEY") 

SECURITY_KEY = sec
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_TIME = 30

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain:str,hashed:str)->bool:
    return pwd_context.verify(plain,hashed)

def create_access_token(data:dict,expires_delta: timedelta=None):
    to_encode = data.copy()
    expire = datetime.utcnow + (expires_delta or timedelta(minutes = ACCESS_TOKEN_EXPIRY_TIME))
    to_encode.update({"exp":expire})
    
    return jwt.encode(to_encode,SECURITY_KEY,algorithm=ALGORITHM)
    
    
def decode_access_token(token:str):
    try:
        jwt.decode(token,SECURITY_KEY,algorithms=[ALGORITHM])
    except JWTError:
        return None