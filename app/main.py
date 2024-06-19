from fastapi import FastAPI
from app.database import engine, Base
from app.routers import atletas_router


app = FastAPI(title='Atletas API')

Base.metadata.create_all(bind=engine)

app.include_router(atletas_router.router, prefix='/api')