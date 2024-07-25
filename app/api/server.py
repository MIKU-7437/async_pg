from fastapi import FastAPI
from api.routes import router as api_router
from core.config import settings
from db.session import engine
from db.utils import create_db_and_tables
from sqladmin import Admin, ModelView
from starlette.middleware.sessions import SessionMiddleware

# Импорт моделей SQLAlchemy
from models.user import User
from models.category import Category
from models.products import Product

# Создание представлений для моделей
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.title, Category.sub_categories]
    form_columns = ["title", "slug", "description", "is_subcategory", "top_category", "sub_categories"]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.title, Product.category_id]
    form_columns = ["title", "slug", "price", "is_available", "description", "stock", "created_date", "modified_date", "photo", "category"]


def get_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/docs",
    )
    app.include_router(api_router, prefix="/api")

    # Добавление Middleware для сессий (необходимо для sqladmin)
    app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

    return app

app = get_application()

# Настройка SQLAdmin
admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(ProductAdmin)

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables(engine)

@app.get("/", tags=["health"])
async def health():
    return dict(
        name=settings.PROJECT_NAME,
        version=settings.VERSION,
        status="OK",
        message="Visit /docs for more information.",
    )
