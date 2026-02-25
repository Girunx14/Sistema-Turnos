from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido_paterno = Column(String(50))
    apellido_materno = Column(String(50))
    fk_area = Column(Integer, ForeignKey("area.id"), nullable=True)

    area = relationship("Area")