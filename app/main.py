from fastapi import FastAPI
from app.routes import diagnosticar, registro_foco

app = FastAPI()

app.include_router(diagnosticar.router)
app.include_router(registro_foco.router)