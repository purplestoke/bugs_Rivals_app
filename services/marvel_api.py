import requests
from dotenv import load_dotenv
import os

load_dotenv()

class RivalsApi:

    def __init__(self):
        self.base_url = "https://mrapi.org/api/"
        self.headers = {"Authorization": f"Bearer {os.getenv("RIVALS_API_KEY")}"}

    # RETURNS id FOR USERNAME
    def get_player_id(self, player_name):
        url = self.base_url + f'player-id/{player_name}'

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return e
    
    # RETURNS PLAYER CAREER DATA GIVEN id
    def get_player(self, player_id):
        url = self.base_url + f'player/{player_id}'

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e

    # RETURNS PLAYERS RECENT MATCHES 
    def get_matches(self, player_id):
        url = self.base_url + f"player-match/{player_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return e
        
    def get_hero(self, hero_name):
        url = self.base_url + f"hero/{hero_name}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return e


