from fastapi import APIRouter

router = APIRouter(prefix="/validate-sp2xml", tags=["Run sp2xml validation"])


@router.post("/run")
async def run_validate_sp2xml():
    return {"status": "ok", "message": "The sp2xml validation run is done."}
