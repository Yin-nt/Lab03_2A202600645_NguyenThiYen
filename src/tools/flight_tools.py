from typing import Any, Dict, List

from src.tools.flight_data import (
    FLIGHTS,
    FARE_RULES,
    SEAT_INVENTORY,
    ADD_ON_PRICING,
    TAX_RATE,
)


def _to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _to_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def search_flights(
    origin: str,
    destination: str,
    date: str,
    cabin: str = "economy",
    budget: str = "0",
    carrier: str = "",
) -> Dict[str, Any]:
    results: List[Dict[str, str]] = []
    budget_value = _to_int(budget, 0)

    for flight in FLIGHTS:
        if flight["origin"] != origin:
            continue
        if flight["destination"] != destination:
            continue
        if not flight["depart"].startswith(date):
            continue
        if flight["cabin"] != cabin:
            continue
        if carrier and flight["carrier"] != carrier:
            continue
        price = _to_int(flight["base_price"], 0)
        if budget_value and price > budget_value:
            continue
        results.append(flight)

    return {
        "count": len(results),
        "flights": results,
        "filters": {
            "origin": origin,
            "destination": destination,
            "date": date,
            "cabin": cabin,
            "budget": budget,
            "carrier": carrier,
        },
    }


def get_fare_rules(flight_id: str) -> Dict[str, Any]:
    rules = FARE_RULES.get(flight_id)
    if not rules:
        return {"error": "fare_rules_not_found", "flight_id": flight_id}
    return {"flight_id": flight_id, "rules": rules}


def check_seat_availability(flight_id: str, passenger_count: str) -> Dict[str, Any]:
    inventory = SEAT_INVENTORY.get(flight_id)
    if not inventory:
        return {"error": "seat_inventory_not_found", "flight_id": flight_id}
    requested = _to_int(passenger_count, 1)
    available = _to_int(inventory.get("economy", "0"), 0) + _to_int(
        inventory.get("business", "0"), 0
    )
    return {
        "flight_id": flight_id,
        "requested": requested,
        "available_total": available,
        "is_available": available >= requested,
    }


def calculate_total_price(
    flight_id: str,
    passenger_count: str,
    add_ons: List[str],
) -> Dict[str, Any]:
    flight = next((item for item in FLIGHTS if item["id"] == flight_id), None)
    if not flight:
        return {"error": "flight_not_found", "flight_id": flight_id}

    base_price = _to_int(flight["base_price"], 0)
    pax = _to_int(passenger_count, 1)
    add_on_total = 0
    for add_on in add_ons:
        add_on_total += _to_int(ADD_ON_PRICING.get(add_on, "0"), 0)

    subtotal = (base_price + add_on_total) * pax
    tax = subtotal * _to_float(TAX_RATE, 0.1)
    total = subtotal + tax

    return {
        "flight_id": flight_id,
        "passenger_count": pax,
        "base_price": base_price,
        "add_on_total": add_on_total,
        "tax": int(tax),
        "total": int(total),
    }


def create_booking(
    flight_id: str,
    passenger_info: Dict[str, Any],
    add_ons: List[str],
) -> Dict[str, Any]:
    if flight_id not in FARE_RULES:
        return {"error": "flight_not_found", "flight_id": flight_id}

    booking_id = f"BK-{flight_id}-{passenger_info.get('last_name', 'GUEST')}"
    return {
        "booking_id": booking_id,
        "flight_id": flight_id,
        "status": "confirmed",
        "passenger_info": passenger_info,
        "add_ons": add_ons,
    }


tool_specs = [
    {
        "name": "search_flights",
        "description": (
            "Find flights by origin, destination, date (YYYY-MM-DD), cabin, budget, and optional carrier. "
            "Returns a list of matching flights with ids and base prices."
        ),
        "parameters": {
            "origin": "IATA code, e.g. HAN",
            "destination": "IATA code, e.g. SGN",
            "date": "YYYY-MM-DD",
            "cabin": "economy or business",
            "budget": "max price in VND, 0 for no limit",
            "carrier": "optional carrier name",
        },
    },
    {
        "name": "get_fare_rules",
        "description": (
            "Get fare rules for a flight, including refundability, change fee, and baggage allowance."
        ),
        "parameters": {"flight_id": "flight id"},
    },
    {
        "name": "check_seat_availability",
        "description": "Check if enough seats remain for the requested passenger count.",
        "parameters": {"flight_id": "flight id", "passenger_count": "number of passengers"},
    },
    {
        "name": "calculate_total_price",
        "description": "Calculate total price with taxes and add-ons for the passenger count.",
        "parameters": {
            "flight_id": "flight id",
            "passenger_count": "number of passengers",
            "add_ons": "list of add-on ids",
        },
    },
    {
        "name": "create_booking",
        "description": "Create a booking and return a booking id with confirmation status.",
        "parameters": {
            "flight_id": "flight id",
            "passenger_info": "dict with passenger details",
            "add_ons": "list of add-on ids",
        },
    },
]


tool_functions = {
    "search_flights": search_flights,
    "get_fare_rules": get_fare_rules,
    "check_seat_availability": check_seat_availability,
    "calculate_total_price": calculate_total_price,
    "create_booking": create_booking,
}
