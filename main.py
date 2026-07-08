import requests
import json

API_KEY = 'BI4DCEMuOr7qMbwrAUPx9f4UsUmde1GqCh64PRJs'
def load_data(file_path):
    """ Loads JSON file. """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_animal(name):
    """Gets animal data from API based on search string.
        returns: animals_data."""
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    animals_data = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    animals_data = animals_data.json()
    return animals_data


def create_animals_data_string(animal_data):
    """ Iterates through the data and creates cards containing:
        name,
        diet,
        first location from locations list,
        type
        :return animals_string
    """
    animals_string = ''
    for animal in animal_data:
        animals_string += serialise_animal(animal)
    return animals_string


def serialise_animal(animal):
    """ Creates the HTML string for an animal card."""
    animal_name = animal.get('name')
    animal_diet = animal.get('characteristics', None).get('diet', None)
    animal_location = animal.get('locations', None)[0]
    animal_type = animal.get('characteristics', None).get('type', None)

    # Write html string
    animal_card = ""
    animal_card += '<li class="cards__item">'
    animal_card += f'<div class="card__title">{animal_name}</div>\n'
    animal_card += '<p class="card__text">'
    if animal_diet:
        animal_card += f"<strong>Diet:</strong> {animal_diet.capitalize()}<br/>\n"
    if animal_location:
        animal_card += f"<strong>Location:</strong> {animal_location}<br/>\n"
    if animal_type:
        animal_card += f"<strong>Type:</strong> {animal_type.capitalize()}<br/>\n"
    animal_card += '</p>'
    animal_card += '</li>'
    return animal_card


def read_animals_template_content():
    """ Gets the content from 'animals_template.html'."""
    with open("animals_template.html", "r") as html_file:
        return html_file.read()


def write_animals_content(animals_html):
    """ Writes the updated content to 'animals_template.html'."""
    with open("animals.html", "w") as html_file:
        html_file.write(animals_html)


def main():
    # animals_data = load_data("animals_data.json")
    animals_data = search_animal('Fox')
    animals_data_string = create_animals_data_string(animals_data)
    animals_template_html = read_animals_template_content()
    animals_template_html = animals_template_html.replace("__REPLACE_ANIMALS_INFO__",
                                                          animals_data_string)
    write_animals_content(animals_template_html)

    for animal in animals_data:
        print(animal)






if __name__ == '__main__':
    main()