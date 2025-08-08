import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '[тут токен тренера]'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN
}

body_registration = {
	"trainer_token" : TOKEN,
	"email" : "alt.c4-bo9ogdg4@yopmail.com",
	"password" : "[Your_Password]",
	"password_re": "[Your_Password]"
}

body_confirmation = {
	"trainer_token": TOKEN
}

body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_change_pokemon_name = {
    "pokemon_id": "371256",
    "name": "New Name",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "371256"
}

#регистрация тренера
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER , json = body_registration)
print(response.text) '''

#подтверждение почты
'''response_confirmation = requests.post ( url = f'{URL}/trainers/confirm_email', headers = HEADER , json = body_confirmation)
print(response_confirmation.text)'''

#создание покемона
response_create_pokemon = requests.post (url = f'{URL}/pokemons', headers = HEADER , json = body_create_pokemon)
print(response_create_pokemon.text)

'''print(response_create_pokemon.status_code)'''

'''message = response_create_pokemon.json()['message']
print(message)'''

#изменение имени покемона
response_change_pokemon_name = requests.put (url = f'{URL}/pokemons', headers = HEADER , json = body_change_pokemon_name)
print(response_change_pokemon_name.text)

#поймать покемона в покебол
respons_pokemon_add_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER , json = body_add_pokeball)

print(respons_pokemon_add_pokeball.text)
