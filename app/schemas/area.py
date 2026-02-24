from pydantic import BaseModel
from app.schemas.tipo_area import TipoAreaOut

class AreaBase(BaseModel):
    nombre: str
    fk_tipo_area: int

class AreaCreate(AreaBase):
    pass

class AreaOut(BaseModel):
    id: int
    nombre: str
    tipo_area: TipoAreaOut

    class Config:
        from_attributes = True