from fastapi import FastAPI, Request
from app.harvest import extract_insight

app = FastAPI()

@app.post("/harvest")
async def harvest_from_chaos(request: Request):
    data = await request.json()
    result = extract_insight(data["chaos"], source="api")
    return {"insight": result}