from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.api.v1.logs import router as logs_router
from app.api.v1.incidents import router as incident_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)

app.include_router(
    logs_router,
    prefix="/api/v1"
)

app.include_router(
    incident_router,
    prefix="/api/v1",
    tags=["Incidents"]
)