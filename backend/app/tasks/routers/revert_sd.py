from fastapi import APIRouter

router = APIRouter(prefix="/revert-sd", tags=["Revert SD in the environment"])


@router.post("/run")
async def run_revert_sd():
    return {"status": "ok", "message": "Revert SD is done"}
