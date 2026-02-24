from pydantic import BaseModel
from datetime import date
from app.schemas.tipo_area import TipoAreaOut

class ContadorBase(BaseModel):
    consecutivo: int
    fecha: date
    fk_tipo_area: int

class ContadorCreate(ContadorBase):
    pass

class ContadorOut(BaseModel):
    id: int
    consecutivo: int
    fecha: date
    tipo_area: TipoAreaOut

    class Config:
        from_attributes = True