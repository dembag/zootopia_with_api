import requests


API_KEY = 'BI4DCEMuOr7qMbwrAUPx9f4UsUmde1GqCh64PRJs'


def fetch_data(animal_name):
    """Gets animal data from API based on search string.
        returns: animals_data."""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    animals_data = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    animals_data = animals_data.json()
    return animals_data