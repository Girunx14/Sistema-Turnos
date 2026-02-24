from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.contador import Contador
from app.schemas.contador import ContadorOut

router = APIRouter(prefix="/contador", tags=["Contador"])

@router.get("/", response_model=list[ContadorOut])
def listar(db: Session = Depends(get_db)):
    return db.query(Contador).all()