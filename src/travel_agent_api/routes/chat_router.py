from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/travel-agent")
def travel_agent_chat(payload: dict):
    print("[API] Richiesta ricevuta su /chat/travel-agent")
    print("[API] Payload ricevuto:", payload)

    return [
        {"role": "assistant", "content": "Ciao, sono il Travel Agent AI. API backend attiva."}
    ]
