from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Contador(Base):
    __tablename__ = "contador"

    id = Column(Integer, primary_key=True, autoincrement=True)
    consecutivo = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    fk_tipo_area = Column(Integer, ForeignKey("tipo_area.id"), nullable=False)

    tipo_area = relationship("TipoArea")