# import requests
from pip._vendor import requests

class Pokemon:
    def __init__(self, name, ability, height, id_, weight):
        self.name = name
        self.abilities = ability
        self.height = height
        self.id = id_
        self.weight = weight
    
    def __repr__(self):
        return f'< Pokemon: {self.name.title()}, Height: {self.height}, ID: {self.id}, Ability: {self.abilities}, Weight: {self.weight} >'


class Get_info:
    def __init__(self, pokemon_choice):
        self.pokemon = pokemon_choice

        api_link = f'https://pokeapi.co/api/v2/pokemon/{pokemon_choice}'
        name_data = requests.get(api_link).json()['name']
        ability_data = requests.get(api_link).json()['abilities'][0]['ability']['name']
        height_data = requests.get(api_link).json()['height']
        id_data = requests.get(api_link).json()['id']
        weight_data = requests.get(api_link).json()['weight']
        self.pokemon_list = []

        p = Pokemon(
            name = name_data,
            ability = ability_data,
            height = height_data,
            id_ = id_data,
            weight = weight_data
        )
        self.pokemon_list.append(p)

    @classmethod
    def run(cls):
        pokemon_choice = input("Which pokemon are you looking for?")
        return cls(pokemon_choice)

# Get_info.run()
pokemon = Get_info.run()
print(pokemon.pokemon_list)