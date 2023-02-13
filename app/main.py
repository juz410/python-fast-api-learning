#uvicorn app.main:app --reload
from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post,user,auth,vote
from .database import engine
from .config import Settings
from pydantic import BaseModel
import random


# Since already got alembic, so no need use this to create any table
# models.Base.metadata.create_all(bind=engine)
class Post(BaseModel):
    title: str
    content: str

class Test(BaseModel):
    username: str
    password: str

class OTP(BaseModel):
    OTPNumber: int
    OTPTime: datetime
    username: str


class OTPPost(BaseModel):
    OTPNumber: str
    username: str

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


@app.get("/test")
def test():
    data : Test = {
        "username": "juz410",
        "password": "test"
    }

    return data


@app.post("/test")
def test(data : Test):
    print(data)

    return (f"{data}, this is return from backend")

@app.get("/otp/{id}")
def otp(id:str):

    six_digit_otp = random.randint(0,999999)
    otp_time_now = datetime.now().strftime('%m-%d-%y %H:%M:%S')
    username = id

    data : OTP = {
        "OTPNumber" : six_digit_otp,
        "OTPTime" : otp_time_now,
        "username" : username
    }

    file = open('otp.txt','a')
    file.write(f"{username}|{str(six_digit_otp)}|{str(otp_time_now)}\n")
    file.close()
    return data


@app.post("/otpcheck")
def otp_check(OTP: OTPPost):
    print(OTP)
    OTPNumberExist = False
    OTPNumberValid = False
    file = open("otp.txt",'r')
    for i in file:
        data = i.split('|')
        data[2] = data[2].strip()
        if(data[0] == OTP.username and data[1] == OTP.OTPNumber):
            OTPNumberExist = True
            OTPNumber = OTP.OTPNumber
            break
    file.close()
    if(not OTPNumberExist):
        return "OTP NUMBER NOT EXISTEDAA"
    
    OTPDefaultTime = datetime.strptime(data[2],'%m-%d-%y %H:%M:%S')
    print(OTPDefaultTime)
    OTPAllowTime = OTPDefaultTime + timedelta(minutes=1)
    if(OTPAllowTime <= datetime.now()):
        return "EXPIRED OTP"
     
    
    
    return True

def delete_line():
    pass
