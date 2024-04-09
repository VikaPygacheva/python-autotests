import requests
import pytest

HOST='https://api.pokemonbattle.me/v2'

def test_status_code():
    response=requests.get(url=f'{HOST}/trainers')
    assert response.status_code==200

def test_trainer_id():
    response=requests.get(url=f'{HOST}/trainers', params={"trainer_id": 2215})
    assert response.json()['trainer_name'] == 'Trainer_Vika'  
    