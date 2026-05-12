from pydantic import BaseModel, Field

class RegistroFoco(BaseModel):
    nivel_foco: int = Field(..., gt=0, lt=6)
    tempo_minutos: int
    comentario: str