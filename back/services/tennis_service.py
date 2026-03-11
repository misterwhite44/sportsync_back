import requests

BASE_URL = "https://tennisapi1.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": "8bbf36cec0msh0a193a46bf94a36p1c0c0fjsna1cc3034358b",
    "X-RapidAPI-Host": "tennisapi1.p.rapidapi.com"
}

def get_player_rankings():
    """Récupère le classement des joueurs (ATP/WTA)"""
    url = f"{BASE_URL}/playerRankings"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return {
            "error": "API request failed",
            "status_code": response.status_code,
            "response": response.text
        }

    return response.json()


def get_upcoming_matches():
    """Récupère les prochains matchs"""
    url = f"{BASE_URL}/upcomingPlayerMatches"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return {
            "error": "API request failed",
            "status_code": response.status_code,
            "response": response.text
        }

    return response.json()


def get_previous_matches():
    """Récupère les matchs passés"""
    url = f"{BASE_URL}/previousPlayerMatches"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return {
            "error": "API request failed",
            "status_code": response.status_code,
            "response": response.text
        }

    return response.json()


def get_calendar(month, year):
    """Récupère le calendrier des tournois pour un mois donné"""
    url = f"{BASE_URL}/tennisCalendarForMonth"
    params = {"month": month, "year": year}
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        return {
            "error": "API request failed",
            "status_code": response.status_code,
            "response": response.text
        }

    return response.json()