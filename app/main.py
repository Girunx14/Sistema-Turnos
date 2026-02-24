from fastapi import FastAPI

app = FastAPI(title="Sistema de Turnos", version="1.0")

@app.get("/")
def root():
    return {"mensaje": "API de Sistema de Turnos funcionando ✅"}