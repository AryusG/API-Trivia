import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

resource = requests.get("https://opentdb.com/api.php", params=parameters)
resource.raise_for_status()
data = resource.json()
question_data = data['results']
