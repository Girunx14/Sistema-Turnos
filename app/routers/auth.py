from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioLogin, UsuarioLoginOut

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login", response_model=UsuarioLoginOut)
def login(data: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.username == data.username
    ).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    ##* por ahora comparamos contraseña directa
    ##* mass adelante se puede agregar hashing con bcrypt
    if usuario.password != data.password:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return usuario