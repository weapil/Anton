import requests
import random
import json

BASE_URL = "https://rickandmortyapi.com/api"
def get_random_character():
    response = requests.get(f"{BASE_URL}/character")
    data = response.json()
    total_characters = data['info']['count']
    random_id = random.randint(1, total_characters)
    response = requests.get(f"{BASE_URL}/character/{random_id}")
    character = response.json()
    print(json.dumps(character, indent=4))
def search_characters_by_name(name):
    response = requests.get(f"{BASE_URL}/character/?name={name}")
    if response.status_code == 200:
        characters = response.json()['results']
        for character in characters:
            print(f"Name: {character['name']}, Status: {character['status']}, Species: {character['species']}")
    else:
        print("Character not found")
def get_all_locations():
    locations = []
    next_page = f"{BASE_URL}/location"
    while next_page:
        response = requests.get(next_page)
        data = response.json()
        locations.extend(data['results'])
        next_page = data['info']['next']
    for location in locations:
        print(f"Location: {location['name']}, Type: {location['type']}, Dimension: {location['dimension']}")
def search_episodes_by_name(name):
    response = requests.get(f"{BASE_URL}/episode/?name={name}")
    if response.status_code == 200:
        episodes = response.json()['results']
        for episode in episodes:
            print(f"Episode: {episode['name']}, Air date: {episode['air_date']}, Episode code: {episode['episode']}")
    else:
        print("Episode not found")

if __name__ == "__main__":
    print("Получение случайного персонажа:")
    get_random_character()
    print("\nПоиск персонажа по имени:")
    search_characters_by_name("Rick")
    print("\nСписок всех локаций:")
    get_all_locations()
    print("\nПоиск эпизодов по названию:")
    search_episodes_by_name("Pilot")
