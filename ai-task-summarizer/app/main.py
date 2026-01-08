from fastapi import FastAPI
from app.api.routes import router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Task Summarizer API")
app.include_router(router)
