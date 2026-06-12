from serpapi import GoogleSearch

from travel_agent_api.config import Config


def find_hotels(destination: str) -> str:
    print("[TOOL] hotels_finder chiamato")

    query = (
        f"hotel consigliati a {destination} "
        "booking tripadvisor expedia centro recensioni"
    )

    params = {
        "engine": "google",
        "q": query,
        "api_key": Config.SERPAPI_API_KEY,
    }

    results = GoogleSearch(params).get_dict()
    items = results.get("organic_results", [])[:5]

    if not items:
        return "Non ho trovato hotel utili per questa richiesta."

    lines = ["Hotel o risorse utili trovate:"]
    for item in items[:3]:
        title = item.get("title", "Titolo non disponibile")
        link = item.get("link", "")
        lines.append(f"- {title}: {link}")

    return "\n".join(lines)
