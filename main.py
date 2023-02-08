# pip3 install fastapi
# pip3 install uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse("index.html", {"request":request, "id":id})

@app.get("/hello/{name}")
def hello(name):
    return {"hello":name}

@app.get("/items/{item_id}") # path parameter
def show_item(item_id:int):
    return {"item_id":item_id}


@app.get("/class/")
def show_class(class_id:int, class_name:str): # query parameter
    return {"class_id":class_id, "class_name":class_name}

@app.get("/calc/")
def calc(fn:str, op:str, sn:str):
    result = eval(fn + op + sn)
    return {"result":result}

@app.get("/signup/", response_class="HTMLResponse")
def signupview(request:Request):
    return templates.TemplateResponse("signup.html", {"request":request})


@app.post("/signup/")
def signup(userId:str, userPw:str):
    with open("user", "a") as db:
        db.write(f"{userId} {userPw}\n")
    return {"msg":"signup success"}

@app.post("/login/")
def login(userId:str, userPw:str):
    with open("user", "r") as db:
        for info in db.readlines():
            dbUserId, dbUserPw = info.split()
            if dbUserId == userId and dbUserPw == userPw:
                return {"msg":"login success"}
    return {"msg":"login fail"}


