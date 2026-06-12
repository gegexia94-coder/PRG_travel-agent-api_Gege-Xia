from travel_agent_api.tools.flights_finder import find_flights
from travel_agent_api.tools.hotels_finder import find_hotels
from travel_agent_api.tools.chain_historical_expert import get_historical_info
from travel_agent_api.tools.chain_travel_plan import create_travel_plan


def run_travel_agent(destination: str) -> str:
    print("[SERVICE] run_travel_agent chiamato")

    flights = find_flights(destination)
    hotels = find_hotels(destination)
    history = get_historical_info(destination)
    plan = create_travel_plan(destination)

    return "\n".join([flights, hotels, history, plan])
