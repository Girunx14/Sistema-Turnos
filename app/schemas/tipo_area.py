from pydantic import BaseModel

class TipoAreaBase(BaseModel):
    nombre: str

class TipoAreaCreate(TipoAreaBase):
    pass

class TipoAreaOut(TipoAreaBase):
    id: int

    class Config:
        from_attributes = True