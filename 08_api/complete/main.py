from fastapi import FastAPI
from .routers import user_router, todo_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(todo_router.router)
