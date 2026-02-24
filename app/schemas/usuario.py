from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    username: str
    nombre: str
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    password: str  # Solo se recibe al crear

class UsuarioOut(UsuarioBase):
    id: int
    # Nota: password NO aparece aquí, nunca se devuelve

    class Config:
        from_attributes = True