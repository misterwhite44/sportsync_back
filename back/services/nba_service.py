import requests

API_KEY = "17492330-fa6a-4eb7-82a9-88b9ac256843"

BASE_URL = "https://api.balldontlie.io/v1/games"

def get_nba_games():

    headers = {
        "Authorization": API_KEY
    }

    response = requests.get(BASE_URL, headers=headers)

    if response.status_code != 200:
        return {
            "error": "API request failed",
            "status_code": response.status_code,
            "response": response.text
        }

    return response.json()