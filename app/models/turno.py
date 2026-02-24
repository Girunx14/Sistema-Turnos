from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Turno(Base):
    __tablename__ = "turno"

    id = Column(Integer, primary_key=True, autoincrement=True)
    folio = Column(String(10), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    fecha_hora_atendida = Column(DateTime)
    fk_usuario = Column(Integer, ForeignKey("usuario.id"))
    fk_area_asignada = Column(Integer, ForeignKey("area.id"))
    fk_estatu = Column(Integer, ForeignKey("estatu.id"), nullable=False)
    fk_genero = Column(Integer, ForeignKey("genero.id"))

    usuario = relationship("Usuario")
    area = relationship("Area")
    estatu = relationship("Estatu")
    genero = relationship("Genero")