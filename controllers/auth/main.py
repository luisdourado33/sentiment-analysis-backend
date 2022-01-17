from database.main import firebase
from urllib.error import HTTPError

from app_types.main import LoginProps, SignUpProps

async def signin(login_data: LoginProps):
    try:
        auth = firebase.auth()
        db = firebase.database()

        authentication = auth.sign_in_with_email_and_password(
            login_data.email, login_data.password)

        user_data = db.child("users").order_by_child("local_id").equal_to(
            authentication["localId"]).get()[0].item[1]

        if user_data is not None:
            user = {
                "local_id": authentication["localId"],
                "firstName": user_data["firstName"],
                "lastName": user_data["lastName"],
                "email": user_data["email"],
            }

        return {"status": 200, "user": user}
    except HTTPError as error:
        return {"status": 400, "error": "Houve um erro ao fazer login."}


async def signup(signup_data: SignUpProps):
    try:
        auth = firebase.auth()
        db = firebase.database()

        new_account = auth.create_user_with_email_and_password(
            signup_data.email, signup_data.password)

        if new_account is not None:
            new_user = {
                "local_id": new_account['localId'],
                "email": new_account['email'],
                "firstName": signup_data.firstName,
                "lastName": signup_data.lastName,
            }

            db.child("users").push(new_user)

        return {"status": 200, "user": new_user}
    except HTTPError as error:
        return {"status": 400, "message": "Houve um erro ao criar a conta."}


async def signout():
    # foo
    return
