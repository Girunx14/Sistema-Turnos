from sqlalchemy import Column, Integer, String
from app.database import Base

class Genero(Base):
    __tablename__ = "genero"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)