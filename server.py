from blog import blog_app
from admin import admin_app
from starlette.staticfiles import StaticFiles

main = blog_app.app

main.mount("/assets/blog", StaticFiles(directory="./assets/blog"),
           name="blog-assets")
main.mount("/assets/admin", StaticFiles(directory="./assets/admin"),
           name="admin-assets")


main.mount("/admin", admin_app.app)
