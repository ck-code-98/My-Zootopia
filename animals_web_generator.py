import json


def load_data_from_json(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_data_from_html(file_path):
    """ Loads an HTML file """
    with open(file_path, "r") as original_html:
        return original_html.read()


def write_new_html_file(file_path, content):
    """Writes new HTML file"""
    with open(file_path, "w") as new_html:
        return new_html.write(content)


def extract_animals_data(overall_data):
    """ iterates through all animals and returns a string with specific data """
    output = ""
    for animal in overall_data:
        output += '<li class="cards__item">'
        output += f'Name: {animal["name"]}<br/>\n'
        output += f'Diet: {animal["characteristics"]["diet"]}<br/>\n'
        output += f'Location: {animal["locations"][0]}<br/>\n'
        if "type" in animal["characteristics"]:
            output += f'Type: {animal["characteristics"]["type"]}<br/>\n'
        output += '<br/>\n'
        output += '</li>'
    return output


def main():
    overall_animals_data = load_data_from_json('animals_data.json')
    desired_output = extract_animals_data(overall_animals_data)
    original_html_content = load_data_from_html('animals_template.html')
    updated_html_content = original_html_content.replace("__REPLACE_ANIMALS_INFO__", desired_output)
    write_new_html_file('animals.html', updated_html_content)


if __name__ == "__main__":
    main()