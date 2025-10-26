from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session

router = APIRouter(prefix="/dry-run", tags=["Dry run"])

@router.post("/run")
async def run_dry_run():
    return {"status": "ok", "message": "Dry run is done"}

# @router.post("/run")
# async def run_dry_run(
#     file: UploadFile = File(...),
#     remove_empty: bool = Form(True),
#     session: AsyncSession = Depends(get_session)
# ):
#     task = TaskRun(task_name="cleanup", status="completed", params={"remove_empty": remove_empty}, result={"message": "Dry run is done"})
#     session.add(task)
#     await session.commit()
#     return {"status": "ok", "message": "Dry run is done"}
