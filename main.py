import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'de3231dc707d69903a0e0e05a7d1fa5c'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}


BODY_CREATE = {
    "name": "капитошка",
    "photo_id": 33}
BODY_UPDATE = {
    "pokemon_id": "367693",
    "name": "New Name",
    "photo_id": 2
}
BODY_IN_POKEBALL = { "pokemon_id": "367693"}



response_create = requests.post(url= f'{URL}pokemons', headers= HEADER, json = BODY_CREATE)
print(response_create.text)

response_update = requests.put(url= f'{URL}pokemons', headers= HEADER, json = BODY_UPDATE)
print(response_update.text)

response_add_pokeball = requests.post(url= f'{URL}trainers/add_pokeball', headers= HEADER, json = BODY_IN_POKEBALL)
print(response_add_pokeball.text)