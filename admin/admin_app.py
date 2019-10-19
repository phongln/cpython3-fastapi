from fastapi import FastAPI
from .routes import router

app = FastAPI(openapi_prefix="/admin")
app.include_router(router)

