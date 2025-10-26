from fastapi import APIRouter

router = APIRouter(prefix="/full-load", tags=["Full load"])

@router.post("/run")
async def run_full_load():
    return {"status": "ok", "message": "Full load has been kicked off."}
