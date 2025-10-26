from fastapi import APIRouter

router = APIRouter(prefix="/commit-run", tags=["Commit run"])


@router.post("/run")
async def run_commit_run():
    return {"status": "ok", "message": "Commit run is done"}
