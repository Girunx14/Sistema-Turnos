from pydantic import BaseModel

class EstatuBase(BaseModel):
    nombre: str

class EstatuCreate(EstatuBase):
    pass

class EstatuOut(EstatuBase):
    id: int

    class Config:
        from_attributes = True