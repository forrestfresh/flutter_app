from fastapi import FastAPI, Header
from tinydb import TinyDB, Query
from typing import Dict, Optional
import jwt

app = FastAPI()
db = TinyDB("db.json")

'''
client secret: password123'''


@app.get("/health")
async def root():
    return {"ay": "ok"}


@app.get("/todos")
async def say_hello(Authorization: Optional[str] = Header(None)):
    """
    Get all todos
    """
    splits = Authorization.split()
    token = splits[1]
    the_jwt = jwt.decode(token, options={"verify_signature": False})
    all_results = db.all()
    results = list(filter(lambda res: res.get("sub") == the_jwt.get("sub"), all_results))
    return results


@app.post("/todo")
async def say_hello(body: Dict):
    """
    Create a new todo
    """
    return 200


@app.put("/todo")
async def say_hello(name: str):
    """
    Update a todo
    """
    return {"message": f"Hello {name}"}


@app.put("/todo")
async def say_hello(name: str):
    """
    Delete a todo
    """
    return {"message": f"Hello {name}"}
