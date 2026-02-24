from sqlalchemy import Column, Integer, String 
from app.database import Base

class TipoArea(Base):
    __tablename__ = "tipo_area"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)