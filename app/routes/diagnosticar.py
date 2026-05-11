from fastapi import APIRouter
from app.services.foco import Diagnosticar

router = APIRouter(prefix="/api")

@router.get("/diagnostico")
def diagnostico():
    return Diagnosticar()