from fastapi import FastAPI

from api import router
from core import configs, get_db

app = FastAPI(
    title=configs.PROJECT_NAME,
    description=configs.DESCRIPTION,
    version=configs.VERSION,
    openapi_url=f"{configs.API_V1_PREFIX}/openapi.json"
)

app.include_router(router)
