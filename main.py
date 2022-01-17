from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.main import firebase

# Controllers
from controllers.auth import get_all, signin
from controllers.auth import signup

# Types
from application_types.auth import LoginProps
from application_types.auth import SignUpProps

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
@app.get("/")
async def root():
  return { "status": 200, "message": "API is running and its documentation is available on /docs" }

@app.post("/login")
async def handleLogin(login_data: LoginProps):
  response = await signin(login_data)
  return response

@app.post("/signup")
async def handleSignUp(signup_data: SignUpProps):
  response = await signup(signup_data)
  return response

@app.get("/getAll")
def handleGetAll():
  return get_all()