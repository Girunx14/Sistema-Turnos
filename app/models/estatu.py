from sqlalchemy import Column, Integer, String
from app.database import Base

class Estatu(Base):
    __tablename__ = "estatu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)