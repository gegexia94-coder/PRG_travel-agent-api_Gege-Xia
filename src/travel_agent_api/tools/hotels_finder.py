from serpapi import GoogleSearch

from travel_agent_api.config import Config


def find_hotels(destination: str) -> str:
    print("[TOOL] hotels_finder chiamato")

    params = {
        "engine": "google",
        "q": f"migliori hotel per {destination}",
        "api_key": Config.SERPAPI_API_KEY,
    }

    results = GoogleSearch(params).get_dict()
    items = results.get("organic_results", [])[:3]

    if not items:
        return "Non ho trovato hotel utili per questa richiesta."

    lines = ["Hotel o risorse utili trovate:"]
    for item in items:
        title = item.get("title", "Titolo non disponibile")
        link = item.get("link", "")
        lines.append(f"- {title}: {link}")

    return "\n".join(lines)
