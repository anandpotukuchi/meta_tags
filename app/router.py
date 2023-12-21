from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_meta_tags():
    pass