from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.genero import Genero
from app.schemas.genero import GeneroCreate, GeneroOut

router = APIRouter(prefix="/genero", tags=["Género"])

@router.get("/", response_model=list[GeneroOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Genero).all()

@router.post("/", response_model=GeneroOut)
def crear(data: GeneroCreate, db: Session = Depends(get_db)):
    nuevo = Genero(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo