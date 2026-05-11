from fastapi import APIRouter
from app.models.dados_foco import RegistroFoco
from app.services.foco import acrescentar_registros, mostrar_registros

router = APIRouter(prefix="/api")

@router.post("/registro_foco")
def criar_registro(dados: RegistroFoco):
    acrescentar_registros(dados)
    return {"msg": "Registro salvo"}


@router.get("/registro_foco")
def mostar():
    return mostrar_registros()