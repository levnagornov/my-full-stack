from fastapi import APIRouter

router = APIRouter(prefix="/share-sp-file-on-sharepoint",
                   tags=["Share SP files on SharePoint"])


@router.post("/run")
async def run_share_sp_files_on_sharepoint():
    return {"status": "ok", "message": "The SP files have been shared"}
