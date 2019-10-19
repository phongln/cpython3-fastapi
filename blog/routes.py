from fastapi import APIRouter
from starlette.requests import Request
from .handler import Handler

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/items/{id}")
async def read_item(request: Request, id: str):
    return Handler.read_item(request, id)
