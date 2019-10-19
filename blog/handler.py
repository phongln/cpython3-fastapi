from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="./blog/templates")


class Handler():
    def read_item(request: Request, id: str):
        return templates.TemplateResponse("item.html", {"request": request, "id": id})
