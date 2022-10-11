#uvicorn app.main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post,user,auth,vote
from .database import engine
from .config import Settings
from pydantic import BaseModel


# Since already got alembic, so no need use this to create any table
# models.Base.metadata.create_all(bind=engine)
class Post(BaseModel):
    title: str
    content: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def hello_world():
    return {"message": "Hello Desmond"}




@app.post("/testing_api")
def testing_api(post: Post):
    print(post)
    file = open("test.txt","a")
    file.write(post.title + "|" + post.content+"\n")
    return post






