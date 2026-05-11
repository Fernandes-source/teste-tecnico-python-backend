from pydantic import BaseModel

class RegistroFoco(BaseModel):
    nivel_foco: int
    tempo_minutos: int
    comentario: str