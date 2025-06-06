from beanie import Document
from pydantic import EmailStr
from typing import Optional

class User(Document):
    email : EmailStr
    password: str
    
class settings:
    name = "users"