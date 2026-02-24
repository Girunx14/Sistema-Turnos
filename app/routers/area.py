from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.area import Area
from app.schemas.area import AreaCreate, AreaOut

router = APIRouter(prefix="/area", tags=["Área"])

@router.get("/", response_model=list[AreaOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Area).all()

@router.get("/{id}", response_model=AreaOut)
def obtener(id: int, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == id).first()
    if not area:
        raise HTTPException(status_code=404, detail="No encontrado")
    return area

@router.post("/", response_model=AreaOut)
def crear(data: AreaCreate, db: Session = Depends(get_db)):
    nueva = Area(**data.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/{id}", response_model=AreaOut)
def actualizar(id: int, data: AreaCreate, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == id).first()
    if not area:
        raise HTTPException(status_code=404, detail="No encontrado")
    area.nombre = data.nombre
    area.fk_tipo_area = data.fk_tipo_area
    db.commit()
    db.refresh(area)
    return area

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    area = db.query(Area).filter(Area.id == id).first()
    if not area:
        raise HTTPException(status_code=404, detail="No encontrado")
    db.delete(area)
    db.commit()
    return {"mensaje": "Eliminado correctamente"}