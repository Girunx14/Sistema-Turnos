from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.estatu import Estatu
from app.schemas.estatu import EstatuCreate, EstatuOut

router = APIRouter(prefix="/estatu", tags=["Estatus"])

@router.get("/", response_model=list[EstatuOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Estatu).all()

@router.get("/{id}", response_model=EstatuOut)
def obtener(id: int, db: Session = Depends(get_db)):
    estatu = db.query(Estatu).filter(Estatu.id == id).first()
    if not estatu:
        raise HTTPException(status_code=404, detail="No encontrado")
    return estatu

@router.post("/", response_model=EstatuOut)
def crear(data: EstatuCreate, db: Session = Depends(get_db)):
    nuevo = Estatu(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo