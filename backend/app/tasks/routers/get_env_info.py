from fastapi import APIRouter

router = APIRouter(prefix="/get-env-info",
                   tags=["Get environment inforamtion"])


@router.post("/run")
async def run_get_env_info():
    return {"status": "ok", "message": "environment infromation blablabla."}
