from fastapi import FastAPI
from app.database import engine
from app.models import *
from app.routers import tipo_area, area, estatu, genero, usuario, turno, contador

app = FastAPI(title="Sistema de Turnos", version="1.0")

app.include_router(tipo_area.router)
app.include_router(area.router)
app.include_router(estatu.router)
app.include_router(genero.router)
app.include_router(usuario.router)
app.include_router(turno.router)
app.include_router(contador.router)

@app.get("/")
def root():
    return {"mensaje": "API de Sistema de Turnos funcionando ✅"}