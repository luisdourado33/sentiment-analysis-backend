from typing import Optional
from pydantic import BaseModel

# Login Types
class LoginProps(BaseModel):
  email: str
  password: str

# SignUp Types
class SignUpProps(BaseModel):
  firstName: str
  lastName: str
  email: str
  password: str