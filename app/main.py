from fastapi import FastAPI
from app.database import engine
from app.models import *

app = FastAPI(title="Sistema de Turnos", version="1.0")

@app.get("/")
def root():
    return {"mensaje": "API de Sistema de Turnos funcionando ✅"}