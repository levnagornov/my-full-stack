from fastapi import APIRouter

router = APIRouter(prefix="/archive-sp-files", tags=["Archive SP files"])


@router.post("/run")
async def run_archive_sp_files():
    return {"status": "ok", "message": "SP files have been archived."}
