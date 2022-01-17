from fastapi import FastAPI
from lemmatization.main import nlp
from fastapi.middleware.cors import CORSMiddleware

# Controllers
from twitterApi import search
from controllers.auth import signin
from controllers.auth import signup
from controllers.auth import signout

# Types
from application_types.auth import LoginProps
from application_types.auth import SignUpProps
from application_types.auth import SignOutProps

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/")
async def root():
    return {
        "status": 200,
        "message": "API is running and its documentation is available on /docs"
    }


@app.post("/login")
async def handleLogin(login_data: LoginProps):
    response = await signin(login_data)
    return response


@app.post("/signup")
async def handleSignUp(signup_data: SignUpProps):
    response = await signup(signup_data)
    return response


@app.post("/signout")
async def handleSignOut(signout_data: SignOutProps):
    response = await signout(signout_data)
    return response


# Tweepy Routes
@app.get("/search")
def handleSearch():
    return search()

# spaCy Routes
@app.get("/spacy/example")
def handleExample():
    sentences = ["Olá, mundo!", "A vida é bela!", "Não gosto de bananas."]
    doc = nlp(sentences[0])

    results = []
    for token in doc:
        results.append({ "text": token.text, "pos_": token.pos_, "dep_": token.dep_ })

    return results