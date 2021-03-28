import uvicorn

from fastapi import FastAPI
from project_name import db
from project_name.db import engine
from project_name.example.endpoints import router as url_router
from project_name.example.models import Example

app = FastAPI()

app.include_router(url_router)

Example
db.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
