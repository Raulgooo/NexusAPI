from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from tokens import get_token
from requests_utils import get_cursos, get_tareas, get_user
from typing import Dict
from starlette.responses import RedirectResponse


class User(BaseModel):  #User class
    user: str
    password: str

class TokenRequest(BaseModel):
    user: str
    
token_cache: Dict[str, str] = {}

app = FastAPI(title="NexusAPI", version="0.1.0")

@app.get("/")
async def menu():
    return RedirectResponse(url="/docs")

@app.post("/login") #Endpoint  login
async def login(user: User):
    try:
        token = get_token(user.user, user.password)
        token_cache[user.user] = token
        return {"user": user.user, "token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")


@app.post("/cursos")
async def cursos(req: TokenRequest):
    token = token_cache.get(req.user)
    if not token:
        raise HTTPException(status_code=401, detail=f"Login failed: {str(e)}")
    return get_cursos(token)
    
@app.post("/calendario")
async def calendario(req: TokenRequest):
    token = token_cache.get(req.user)
    if not token:
        raise HTTPException(status_code=401, detail="Token Invalido o no ha iniciado sesion.")
    return get_tareas(token)


@app.post("/user")
async def user(req: TokenRequest):
    token = token_cache.get(req.user)
    if not token:
        raise HTTPException(status_code=401, detail="Token Invalido o no ha iniciado sesion.")
    return get_user(token)
