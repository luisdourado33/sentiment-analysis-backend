from dotenv import dotenv_values
import pyrebase

environment = dotenv_values(".env")

config = {
    "apiKey": environment['FIREBASE_API_KEY'],
    "authDomain": environment['FIREBASE_AUTH_DOMAIN'],
    "databaseURL": environment['FIREBASE_DATABASE_URL'],
    "storageBucket": environment['FIREBASE_STORAGE_BUCKET']
}

firebase = pyrebase.initialize_app(config)