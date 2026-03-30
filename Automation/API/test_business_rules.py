import requests
from datetime import date
import pytest

URL="https://qae-assignment-tau.vercel.app"
USER="candidate-3d0b2f5a"

### Simply test to verify matches filter
def test_get_all_matches():
    response = requests.get(
        f"{URL}/api/matches",
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()
    assert data is not None


### Security verification by providing incorrect user_id
def test_get_all_matches_not_authorized():
    incorrect_user="ABC"
    response = requests.get(
        f"{URL}/api/matches",
        headers={
            "accept": "application/json",
            "x-user-id": incorrect_user,
        },
    )

    assert response.status_code == 401
    assert "application/json" in response.headers.get("Content-Type", "")


### Verification of bet type by checking 'competition' variable
def test_matches_type():
    response = requests.get(
        f"{URL}/api/matches",
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()
    comptetition_name = {item["competition"] for item in data}
    assert {'MLS', 'Championship', 'Scottish Premiership', 'La Liga', 'Serie A', 'Bundesliga', 'Premier League', 'Ligue 1', 'Primeira Liga', 'Eredivisie'}.issubset(comptetition_name)


### Checking if date in resposne is in the future
@pytest.mark.xfail(reason="BUG-02")
def test_future_date_of_matches():
    response = requests.get(
        f"{URL}/api/matches",
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()
    dates = [item["kickoffDate"] for item in data]
    today = date.today().isoformat()

    for d in dates:
        assert d > today


### Checking successful bet reponse, I didn't include all fields due to lack of time
@pytest.mark.xfail(reason="BUG-04")
def test_successful_bet():
    matchId = "premier-league-manutd-chelsea"
    stake = 1
    response = requests.post(
        f"{URL}/api/place-bet",
        json={
            "matchId": matchId,
            "selection": "HOME",
            "stake": stake,
            "additionalProp1": {}
        },
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )
    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")

    data = response.json()
    assert data["message"] == "Bet placed successfully"
    assert data["matchId"] == matchId
    assert data["stake"] == stake
    assert data["currency"] == "EUR"


### Testing bet that is smaller than 1 EUR and higher than 100 EUR (details in documentation)
def test_incorrect_bet_value():
    matchId = "premier-league-manutd-chelsea"
    stake = 0.5
    response = requests.post(
        f"{URL}/api/place-bet",
        json={
            "matchId": matchId,
            "selection": "HOME",
            "stake": stake,
            "additionalProp1": {}
        },
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )
    assert response.status_code == 422
    assert "application/json" in response.headers.get("Content-Type", "")

    matchId = "premier-league-manutd-chelsea"
    stake = 100.05
    response = requests.post(
        f"{URL}/api/place-bet",
        json={
            "matchId": matchId,
            "selection": "HOME",
            "stake": stake,
            "additionalProp1": {}
        },
        headers={
            "accept": "application/json",
            "x-user-id": USER,
        },
    )
    assert response.status_code == 422
    assert "application/json" in response.headers.get("Content-Type", "")