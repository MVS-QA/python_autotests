import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd0e229379087b58ccc7bff2b4d587672'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN
}
Trainer_id = '41750'

'''def test_status_code():
	response = requests.get (url = f'{URL}/pokemons', headers = {'trainer_id' : Trainer_id} )
	assert response.status_code == 200
	if response.status_code != 200 : print("ok")'''


'''def test_part_of_response ():
	response = requests.get (url = f'{URL}/pokemons', headers = {'trainer_id' : Trainer_id} )
	response.json()["data"][0]["name"]=="jj"
	assert response.json()['name'] == "ho oh"'''

'''@pytest.mark.parametrize('key,value',[('name','Бульбазавр'),('trainer_id',Trainer_id),('pokemon_id','371256')])
def test_parametrize (key, value) :
	response_parametrize = requests.get (url = f'{URL}/pokemons', headers = {'trainer_id' : Trainer_id} )
	assert response_parametrize.json()["data"][0][key] == value'''

# Проверка статуса 200 у GET /trainers
'''def test_status_code():
	response = requests.get (url = f'{URL}/trainers', headers = {'trainer_id' : Trainer_id} )
	assert response.status_code == 200
	if response.status_code != 200 : print("ok")'''

'''response = requests.get (url = f'{URL}/trainers', headers = {'trainer_id' : Trainer_id} )
print(respons.text)'''


def test_status_code():
    response = requests.get(url = f'{url}/trainers', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{url}/trainers', params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][0]["trainer_name"] == 'тренер'