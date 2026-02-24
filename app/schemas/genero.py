from pydantic import BaseModel

class GeneroBase(BaseModel):
    id: int
    nombre: str

class GeneroCreate(GeneroBase):
    pass

class GeneroOut(GeneroBase):

    class Config:
        from_attributes = True