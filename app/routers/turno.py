from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.turno import Turno
from app.models.contador import Contador
from app.models.area import Area
from app.schemas.turno import TurnoCreate, TurnoOut
from datetime import datetime

router = APIRouter(prefix="/turno", tags=["Turno"])

@router.get("/", response_model=list[TurnoOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Turno).all()

@router.get("/{id}", response_model=TurnoOut)
def obtener(id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="No encontrado")
    return turno

@router.post("/", response_model=TurnoOut)
def crear(data: TurnoCreate, db: Session = Depends(get_db)):
    # Obtener el tipo de área para generar el folio
    area = db.query(Area).filter(Area.id == data.fk_area_asignada).first()
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada")

    hoy = datetime.now().date()

    # Buscar o crear el contador del día para ese tipo de área
    contador = db.query(Contador).filter(
        Contador.fk_tipo_area == area.fk_tipo_area,
        Contador.fecha == hoy
    ).first()

    if not contador:
        contador = Contador(consecutivo=1, fecha=hoy, fk_tipo_area=area.fk_tipo_area)
        db.add(contador)
    else:
        contador.consecutivo += 1

    db.flush()  # Para obtener el consecutivo actualizado

    # Generar folio: prefijo del tipo de área + consecutivo con ceros
    prefijo = area.tipo_area.nombre[:2].upper()
    folio = f"{prefijo}{str(contador.consecutivo).zfill(3)}"

    nuevo_turno = Turno(
        folio=folio,
        fecha_hora=datetime.now(),
        fk_area_asignada=data.fk_area_asignada,
        fk_estatu=1,  # 1 = En espera (asegúrate de tener este estatus en tu BD)
        fk_genero=data.fk_genero
    )

    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    return nuevo_turno

@router.put("/{id}/atender", response_model=TurnoOut)
def atender(id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="No encontrado")
    turno.fk_estatu = 2  # 2 = Atendido
    turno.fecha_hora_atendida = datetime.now()
    db.commit()
    db.refresh(turno)
    return turno

@router.put("/{id}/cancelar", response_model=TurnoOut)
def cancelar(id: int, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="No encontrado")
    turno.fk_estatu = 3  # 3 = Cancelado
    db.commit()
    db.refresh(turno)
    return turno