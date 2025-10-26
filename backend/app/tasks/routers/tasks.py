from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from app.core.database import get_session


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
async def get_tasks(session: AsyncSession = Depends(get_session)) -> dict[str, Any]:
    return {
        "tasks": [
            {"id": "dry-run", "name": "Dry run SD", "endpoint": "/dry-run/run"},
            {"id": "commit-run", "name": "Commit run SD",
                "endpoint": "/commit-run/run"},
            {"id": "full-load", "name": "Full load of SP",
                "endpoint": "/full-load/run"},
            {"id": "recalculation", "name": "Recalculation",
                "endpoint": "/recalculation/run"},
            {"id": "validate-sp2xml", "name": "Validate SP files with sp2xml",
                "endpoint": "/validate-sp2xml/run"},
            {"id": "vpp-run", "name": "123", "VPP run": "/vpp-run/run"},
            {"id": "vde-run", "name": "123", "VDE run": "/vde-run/run"},
            {"id": "revert-sd", "name": "123",
                "Revert SD to the original state": "/revert-sd/run"},
            {"id": "get-env-info", "name": "123",
                "Environment information": "/get-env-info/run"},
            {"id": "archive-sp-files", "name": "Archive SP files",
                "endpoint": "/archive-sp-files/run"},
            {"id": "share-sp-file-on-sharepoint", "name": "Share SP files on SharePoint",
                "endpoint": "/share-sp-file-on-sharepoint/run"},
        ]
    }
