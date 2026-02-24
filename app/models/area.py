from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Area(Base):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    fk_tipo_area = Column(Integer, ForeignKey("tipo_area.id"), nullable=False)

    tipo_area = relationship("TipoArea")