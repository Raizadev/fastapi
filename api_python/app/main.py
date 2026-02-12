from fastapi import FastAPI
from .database import engine, Base
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API FastAPI Exemplo",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API FastAPI a funcionar 🚀"}
