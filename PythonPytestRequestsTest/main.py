import requests

host = 'https://api.pokemonbattle.me:9104'
token = 'bd68dbd0b2f8e89d9df4c46e0a84e030'

create_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(create_pokemon.text)

change_pokemon_name_and_picture = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6095",
    "name": "generate",
    "photo": "generate"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(change_pokemon_name_and_picture.text)

catch_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "6095"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(catch_pokemon.text)