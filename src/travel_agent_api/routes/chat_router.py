from fastapi import APIRouter

from travel_agent_api.services.agent_service import run_travel_agent

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/travel-agent")
def travel_agent_chat(payload: dict):
    print("[API] Richiesta ricevuta su /chat/travel-agent")
    print("[API] Payload ricevuto:", payload)

    messages = payload.get("messages", [])
    user_message = messages[-1].get("content", "") if messages else ""

    answer = run_travel_agent(user_message)

    return [
        *messages,
        {"type": "ai", "content": answer},
    ]
