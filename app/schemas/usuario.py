from pydantic import BaseModel
from typing import Optional
from app.schemas.area import AreaOut

class UsuarioBase(BaseModel):
    username: str
    nombre: str
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    fk_area: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioOut(UsuarioBase):
    id: int
    area: Optional[AreaOut] = None

    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    username: str
    password: str

class UsuarioLoginOut(BaseModel):
    id: int
    username: str
    nombre: str
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    area: Optional[AreaOut] = None

    class Config:
        from_attributes = True