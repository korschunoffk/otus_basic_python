import json
from fastapi import APIRouter, Response

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("")
def ping_get():
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
    )


@router.post("")
def ping_post():
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
    )
