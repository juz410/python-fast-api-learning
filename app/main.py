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




@app.post("/text_file_post")
def text_file_post(post: Post):
    print(post)
    file = open("test.txt","a")
    file.write(post.title + "|" + post.content+"\n")
    file.close()
    return post


@app.get("/text_file_get")
def text_file_get():
    file = open("test.txt")
    post = []
    for i in file:
        post_content =  (i.strip()).split('|')
        post.append(
            {
                "title" : post_content[0],
                "content" : post_content[1]
            }
        )
    file.close()
    return {"post: " : post}



