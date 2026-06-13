# Travel Agent API

L'obiettivo del progetto è creare un assistente di viaggio che riceve una richiesta da una chat web e restituisce una risposta utile con:

- informazioni su voli o trasporti
- risorse per hotel e soggiorno
- elementi storico-culturali
- piano di viaggio sintetico

## Obiettivo del progetto

L'utente scrive una richiesta, per esempio:

```text

Voglio andare a Parigi da Venezia per 3 giorni

Il frontend Laravel invia questo messaggio al backend FastAPI.

Il backend elabora la richiesta usando:

tool di ricerca esterna tramite SerpApi
chain LangChain con OpenAI
un service centrale che coordina i vari passaggi

Alla fine il backend restituisce una risposta unica, formattata in Markdown, che il frontend mostra nella chat.

Flusso generale dell'applicazione:

Browser
→ Laravel Livewire
→ POST /chat/travel-agent
→ FastAPI Router
→ Agent Service
→ Tool voli
→ Tool hotel
→ Chain storico-culturale
→ Chain piano viaggio
→ Risposta finale
→ Laravel mostra la risposta nella chat

Tecnologie usate:

Backend
Python
FastAPI
Uvicorn
Poetry
Pydantic
python-dotenv
LangChain
OpenAI
SerpApi
Frontend fornito
Laravel
Livewire
Vite
Bootstrap / CSS del progetto
