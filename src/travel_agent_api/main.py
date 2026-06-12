from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from travel_agent_api.routes.chat_router import router as chat_router

app = FastAPI(title="Travel Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Travel Agent API attiva"}
