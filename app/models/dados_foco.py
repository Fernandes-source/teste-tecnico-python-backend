from pydantic import BaseModel, Field

class RegistroFoco(BaseModel):
    nivel_foco: int = Field(..., gt=1, lt=5)
    tempo_minutos: int
    comentario: str