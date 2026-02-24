from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioOut

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.get("/", response_model=list[UsuarioOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/{id}", response_model=UsuarioOut)
def obtener(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    return usuario

@router.post("/", response_model=UsuarioOut)
def crear(data: UsuarioCreate, db: Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.username == data.username).first()
    if existe:
        raise HTTPException(status_code=400, detail="El username ya existe")
    nuevo = Usuario(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id}", response_model=UsuarioOut)
def actualizar(id: int, data: UsuarioCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.model_dump().items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario

@router.delete("/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Eliminado correctamente"}