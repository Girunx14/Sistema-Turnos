from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.usuario import UsuarioOut
from app.schemas.area import AreaOut
from app.schemas.estatu import EstatuOut
from app.schemas.genero import GeneroOut

class TurnoBase(BaseModel):
    fk_area_asignada: Optional[int] = None

class TurnoCreate(TurnoBase):
    pass

class TurnoAtender(BaseModel):
    fk_genero: Optional[int] = None  # El ejecutivo registra el género al atender

class TurnoOut(BaseModel):
    id: int
    folio: str
    fecha_hora: datetime
    fecha_hora_atendida: Optional[datetime] = None
    usuario: Optional[UsuarioOut] = None
    area: Optional[AreaOut] = None
    estatu: EstatuOut
    genero: Optional[GeneroOut] = None

    class Config:
        from_attributes = True