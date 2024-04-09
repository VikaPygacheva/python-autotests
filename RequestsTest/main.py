import requests


response=requests.post(url='https://api.pokemonbattle.me/v2/pokemons',
                       json={"name": "generate",
                             "photo": "generate"
                             },
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': 'dcfe23cabb7d2481928eebf1b04cf1c0'
                                },
                       timeout=3
                       ) 

print(response.text)

response=requests.put(url='https://api.pokemonbattle.me/v2/pokemons',
                       json={"pokemon_id": "17003",
                             "name": "generate",
                             "photo": "generate"
                             },
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': 'dcfe23cabb7d2481928eebf1b04cf1c0'
                                },
                       timeout=3
                       )

print(response.text)

response=requests.post(url='https://api.pokemonbattle.me/v2/trainers/add_pokeball',
                       json={"pokemon_id": "17003"},
                       headers= {
                                 'Content-Type': 'application/json',
                                 'trainer_token': 'dcfe23cabb7d2481928eebf1b04cf1c0'
                                },
                       timeout=3
                       )

print(response.text)
