from fastapi import FastAPI
from core.config import settings

## initialising the object
app = FastAPI(title=settings.PROJECT_TITLE , version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    return {"msg":"Hello World bring it on"}