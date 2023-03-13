from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/login")
def root():
    return {"message": "this is login endpoint"}

@app.get("/add")
def root():
    a=15
    b=15
    c=20
    return {"message": str(a+b+c)}