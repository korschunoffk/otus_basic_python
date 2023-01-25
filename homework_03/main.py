import json

from fastapi import FastAPI, Response
from views.ping import router as ping_router

app = FastAPI()
app.include_router(ping_router)

@app.get("/")
def read_root():
    return Response(
        content=json.dumps({"hello": "root"}),
        media_type="application/json",
    )

