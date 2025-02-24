from fastapi import FastAPI
import requests

app = FastAPI()
TBA_API_KEY = "58D3IIujjkD0vRjUdkwStGCmMzcG6pLD4mttPo7XIBnwUWmigT7EpJLVsVDpcULQ"
HEADERS = {"X-TBA-Auth-Key": TBA_API_KEY}
TBA_BASE_URL = "https://www.thebluealliance.com/api/v3"

@app.get("/event/{event_key}/scores")
def get_event_scores(event_key: str):
    url = f"{TBA_BASE_URL}/event/{event_key}/matches"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}

@app.get("/team/{team_key}/scores/{year}")
def get_team_scores(team_key: str, year: int):
    url = f"{TBA_BASE_URL}/team/{team_key}/matches/{year}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}
