# Sentiment Analysis - API
#
# This is the main file, where
# API is started with uvicorn package.
# To start: uvicorn main:app --reload
#
# Created by: Luís Dourado (luisdourado33)

from fastapi import FastAPI
from dotenv import dotenv_values
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values(".env")

# Types
from app_types.main import LoginProps, SignUpProps, PostNewVoteProps

# Controllers
from controllers.auth.main import signin, signup
from controllers.tweepy.main import get_by_keyword, get_tweets_pre, populate, post_vote_new
from controllers.spacy.main import get_spacy_ex

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


# Routes for authentication
@app.get("/")
def index():
    return {"status": 200, "message": "API is online. Docs in /docs"}


# Login route
@app.post("/auth/login")
async def make_login(login_data: LoginProps):
    response = await signin(login_data)
    return response


# SignUp route
@app.post("/auth/signup")
async def create_account(signup_data: SignUpProps):
    response = await signup(signup_data)
    return response


# Tweepy routes
@app.get("/tweepy/get_tweets/{keyword}")
async def get_tweets_by_keyword(keyword: str):
  response = await get_by_keyword(keyword)
  return response

@app.post("/tweepy/populate/{keyword}")
async def populate_database_by_keyword(keyword: str):
  response = await populate(keyword)
  return response

@app.get("/tweepy/pre_tweets")
async def get_pre_tweets():
    response = await get_tweets_pre()
    return response



@app.post("/tweepy/post_tweets/new")
async def post_new_vote(vote_data: PostNewVoteProps):
    response = await post_vote_new(vote_data)
    return response

# spaCy
@app.get("/spacy/example")
def get_spacy_example():
    response = get_spacy_ex()
    return response