from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_area import TipoArea
from app.schemas.tipo_area import TipoAreaCreate, TipoAreaOut

router = APIRouter(prefix="/tipo-area", tags=["Tipo de Área"])

@router.get("/", response_model=list[TipoAreaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(TipoArea).all()

@router.get("/{id}", response_model=TipoAreaOut)
def obtener(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoArea).filter(TipoArea.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="No encontrado")
    return tipo

@router.post("/", response_model=TipoAreaOut)
def crear(data: TipoAreaCreate, db: Session = Depends(get_db)):
    nuevo = TipoArea(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id}", response_model=TipoAreaOut)
def actualizar(id: int, data: TipoAreaCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoArea).filter(TipoArea.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="No encontrado")
    tipo.nombre = data.nombre
    db.commit()
    db.refresh(tipo)
    return tipo

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoArea).filter(TipoArea.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="No encontrado")
    db.delete(tipo)
    db.commit()
    return {"mensaje": "Eliminado correctamente"}