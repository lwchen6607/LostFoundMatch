from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LostFoundMatch Teaching Mock")

class MatchRequest(BaseModel):
    category: str
    color: str
    location: str

mock_results = {
    ("EARBUDS", "WHITE", "LIBRARY"): [
        {"found_item_id": 12, "score": 95},
        {"found_item_id": 18, "score": 80}
    ],
    ("PHONE", "BLACK", "CLASSROOM"): [
        {"found_item_id": 21, "score": 90},
        {"found_item_id": 25, "score": 70}
    ],
    ("WALLET", "BROWN", "CAFETERIA"): [
        {"found_item_id": 31, "score": 85}
    ],
    ("BAG", "BLUE", "GYM"): [
        {"found_item_id": 41, "score": 92},
        {"found_item_id": 44, "score": 75}
    ]
}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "LostFoundMatch Teaching Mock"
    }


@app.post("/matches")
def match_items(request: MatchRequest):
    key = (
        request.category.upper(),
        request.color.upper(),
        request.location.upper()
    )
    
    candidates = mock_results.get(key, [])
    
    return {
        "message": "This is a teaching mock response.",
        "received": request.model_dump(),
        "candidates": candidates
    }
