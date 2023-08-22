import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
trainer_id = 1969

def test_status_code_200():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : trainer_id})
    assert response.status_code == 200

def test_correct_trainer_name():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : trainer_id})
    assert response.json()['trainer_name'] == 'Zack'