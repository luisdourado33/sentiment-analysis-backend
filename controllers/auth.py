from database.main import firebase
import urllib.request
from urllib.error import HTTPError

from application_types.auth import LoginProps
from application_types.auth import SignUpProps

async def signup(signup_data: SignUpProps):
  try:
    auth = firebase.auth()
    db = firebase.database()

    new_account = auth.create_user_with_email_and_password(
      signup_data.email,
      signup_data.password
    )

    print(new_account)

    # Insert params into 'users' table
    new_user = {
      "local_id": new_account['localId'],
      "email": new_account['email'],
      "firstName": signup_data.firstName,
      "lastName": signup_data.lastName,
    }

    db.child("users").push(new_user)

    return { "status": 200, "user": new_user }
  except HTTPError as error:
    return { "status": 400, "message": "Houve um erro na requisição.", "error": error.response }

async def signin(login_data: LoginProps):
  try:
    auth = firebase.auth()
    db = firebase.database()

    authentication = auth.sign_in_with_email_and_password(
      login_data.email,
      login_data.password,
    )

    user_data = db.child("users").order_by_child("local_id").equal_to(authentication["localId"]).get()[0]
    print(user_data)
    return user_data

    user = {
      "local_id": authentication["localId"],
      "firstName": user_data["firstName"],
      "lastName": user_data["lastName"],
      "email": user_data["email"],
    }

    return { "status": 200, "user": user }
  except HTTPError as error:
    print("houve um erro")
    return { "status": 400, "message": "Houve um erro ao fazer login" }

def get_all():
  db = firebase.database()
  users = db.child('users').order_by_child("firstName").equal_to("Luís").get()

  return users