import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'de3231dc707d69903a0e0e05a7d1fa5c'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
TRAINER_ID = '37589'

def test_status_code():
   response = requests.get(url=f'{URL}trainers', params = {'trainer_id': TRAINER_ID})
   assert response.status_code == 200

def test_in_text():
   response = requests.get(url=f'{URL}trainers', params = {'trainer_id': TRAINER_ID})  
   assert response.json()["data"][0]['trainer_name'] == 'Artem'