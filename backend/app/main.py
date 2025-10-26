from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.auth import routes as auth_routes
from app.users import routes as user_routes
from app.tasks.routers import tasks as task_routes
from app.tasks.routers import dry_run as dry_run_routes
from app.tasks.routers import commit_run as commit_run_routes
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.database import engine, Base



@asynccontextmanager
async def lifespan(app: FastAPI):
    # after startup
    # create tables if not exist (simple approach for dev)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # after shutwodn

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI JWT + Redis + Postgres", lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Start including routers...")

app.include_router(auth_routes.router)
app.include_router(user_routes.router)
app.include_router(task_routes.router)
app.include_router(dry_run_routes.router)
app.include_router(commit_run_routes.router)

logger.info("Routers included.")
