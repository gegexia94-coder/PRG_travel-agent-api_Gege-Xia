from serpapi import GoogleSearch

from travel_agent_api.config import Config


def find_flights(destination: str) -> str:
    print("[TOOL] flights_finder chiamato")

    query = (
        f"voli economici per {destination} "
        "skyscanner google flights kayak"
    )

    params = {
        "engine": "google",
        "q": query,
        "api_key": Config.SERPAPI_API_KEY,
    }

    results = GoogleSearch(params).get_dict()
    items = results.get("organic_results", [])[:3]

    if not items:
        return "Non ho trovato informazioni utili sui voli."

    lines = ["Voli o risorse utili trovate:"]
    for item in items:
        title = item.get("title", "Titolo non disponibile")
        link = item.get("link", "")
        lines.append(f"- {title}: {link}")

    return "\n".join(lines)
