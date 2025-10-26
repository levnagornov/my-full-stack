from fastapi import APIRouter

router = APIRouter(prefix="/vpp-run", tags=["VPP run"])

@router.post("/run")
async def run_vpp_run():
    return {"status": "ok", "message": "VPP run is done"}
