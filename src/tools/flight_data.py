from typing import Dict, List

FLIGHTS: List[Dict[str, str]] = [
    {
        "id": "VN101",
        "carrier": "VietnamAirlines",
        "origin": "HAN",
        "destination": "SGN",
        "depart": "2026-06-12T07:30",
        "arrive": "2026-06-12T09:40",
        "duration_minutes": "130",
        "cabin": "economy",
        "base_price": "2100000",
    },
    {
        "id": "VJ201",
        "carrier": "VietJet",
        "origin": "HAN",
        "destination": "SGN",
        "depart": "2026-06-12T06:20",
        "arrive": "2026-06-12T08:30",
        "duration_minutes": "130",
        "cabin": "economy",
        "base_price": "1650000",
    },
    {
        "id": "QH301",
        "carrier": "BambooAirways",
        "origin": "HAN",
        "destination": "SGN",
        "depart": "2026-06-12T10:10",
        "arrive": "2026-06-12T12:25",
        "duration_minutes": "135",
        "cabin": "economy",
        "base_price": "1850000",
    },
    {
        "id": "VN111",
        "carrier": "VietnamAirlines",
        "origin": "HAN",
        "destination": "DAD",
        "depart": "2026-06-12T08:05",
        "arrive": "2026-06-12T09:25",
        "duration_minutes": "80",
        "cabin": "economy",
        "base_price": "1250000",
    },
    {
        "id": "VN401",
        "carrier": "VietnamAirlines",
        "origin": "SGN",
        "destination": "HAN",
        "depart": "2026-06-13T19:30",
        "arrive": "2026-06-13T21:40",
        "duration_minutes": "130",
        "cabin": "economy",
        "base_price": "2150000",
    },
    {
        "id": "QH501",
        "carrier": "BambooAirways",
        "origin": "SGN",
        "destination": "HAN",
        "depart": "2026-06-13T14:00",
        "arrive": "2026-06-13T16:10",
        "duration_minutes": "130",
        "cabin": "economy",
        "base_price": "1750000",
    },
    {
        "id": "VN701",
        "carrier": "VietnamAirlines",
        "origin": "HAN",
        "destination": "SGN",
        "depart": "2026-06-12T18:15",
        "arrive": "2026-06-12T20:25",
        "duration_minutes": "130",
        "cabin": "business",
        "base_price": "5200000",
    },
    {
        "id": "VJ801",
        "carrier": "VietJet",
        "origin": "HAN",
        "destination": "SGN",
        "depart": "2026-06-12T20:30",
        "arrive": "2026-06-12T22:40",
        "duration_minutes": "130",
        "cabin": "economy",
        "base_price": "1500000",
    },
]

FARE_RULES: Dict[str, Dict[str, str]] = {
    "VN101": {
        "refundable": "yes",
        "change_fee": "300000",
        "baggage_allowance_kg": "20",
    },
    "VJ201": {
        "refundable": "no",
        "change_fee": "450000",
        "baggage_allowance_kg": "7",
    },
    "QH301": {
        "refundable": "partial",
        "change_fee": "350000",
        "baggage_allowance_kg": "20",
    },
    "VN111": {
        "refundable": "yes",
        "change_fee": "250000",
        "baggage_allowance_kg": "20",
    },
    "VN401": {
        "refundable": "yes",
        "change_fee": "300000",
        "baggage_allowance_kg": "20",
    },
    "QH501": {
        "refundable": "partial",
        "change_fee": "350000",
        "baggage_allowance_kg": "20",
    },
    "VN701": {
        "refundable": "yes",
        "change_fee": "0",
        "baggage_allowance_kg": "30",
    },
    "VJ801": {
        "refundable": "no",
        "change_fee": "450000",
        "baggage_allowance_kg": "7",
    },
}

SEAT_INVENTORY: Dict[str, Dict[str, str]] = {
    "VN101": {"economy": "6", "business": "0"},
    "VJ201": {"economy": "12", "business": "0"},
    "QH301": {"economy": "4", "business": "0"},
    "VN111": {"economy": "8", "business": "0"},
    "VN401": {"economy": "7", "business": "0"},
    "QH501": {"economy": "5", "business": "0"},
    "VN701": {"economy": "0", "business": "3"},
    "VJ801": {"economy": "9", "business": "0"},
}

ADD_ON_PRICING: Dict[str, str] = {
    "baggage_20kg": "300000",
    "baggage_30kg": "450000",
    "priority_boarding": "120000",
}

TAX_RATE = "0.1"
