from fastapi import APIRouter

router = APIRouter(prefix="/recalculation", tags=["Recalculation"])

@router.post("/run")
async def run_recalculation():
    return {"status": "ok", "message": "Recalculation has been started."}
