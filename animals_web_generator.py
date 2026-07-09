import data_fetcher


def get_animal_to_search():
    """
    Gets the user to enter an animal to search for
    :return: animal
    """
    user_animal = input("Please enter an animal: ")
    return user_animal


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
    print("Website was successfully written to the file animals.html.")


def create_search_error_message(user_animal):
    """ Creates a message that tells the user the search string
        they entered is not in the database."""
    animal_card = ""
    animal_card += '<li class="cards__item">'
    animal_card += f'<div class="card__title">{user_animal}</div>\n'
    animal_card += '<p class="card__text">'
    animal_card += (f"The animal <strong>{user_animal}</strong> does not exist "
                    f"in the database.<br/>\n")
    animal_card += '</p>'
    animal_card += '</li>'
    return animal_card

def main():
    animal_name = get_animal_to_search()
    animals_data = data_fetcher.fetch_data(animal_name)
    if not animals_data:
        animals_data_string = create_search_error_message(animal_name)
    else:
        animals_data_string = create_animals_data_string(animals_data)
    animals_template_html = read_animals_template_content()
    animals_template_html = animals_template_html.replace("__REPLACE_ANIMALS_INFO__",
                                                          animals_data_string)
    write_animals_content(animals_template_html)


if __name__ == '__main__':
    main()