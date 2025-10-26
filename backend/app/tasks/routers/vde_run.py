from fastapi import APIRouter

router = APIRouter(prefix="/vde-run", tags=["VDE run"])


@router.post("/run")
async def run_vde_run():
    return {"status": "ok", "message": "VDE run is done"}
