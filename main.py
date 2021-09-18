from pprint import pprint
import requests
import json


session = requests.Session()

def get_country_list():
    with open(r"countries.json", encoding="utf-8") as read_file:
        json_data = json.load(read_file)
    return [country['name']['common'] for country in json_data]

def get_link(my_string):
    params = {'action': 'opensearch', 'search': my_string, 'limit': '1'}
    response = session.get('https://commons.wikimedia.org/w/api.php', params = params)
    try:
        if response.json()[3]:
            return response.json()[3][0]
    except json.decoder.JSONDecodeError:
        print('Неожиданный ответ от API Wikipaedia')
        return None

class WikiIterator:
    def __init__(self):
        self.country_list = get_country_list()

    def __iter__(self):
        return self

    def __next__(self):
        if self.country_list:
            country = self.country_list.pop(0)
            new_country = f"{country} - {get_link(country)}"
            return new_country
        else:
            raise StopIteration


if __name__ == '__main__':
    for i in WikiIterator():
        with open('output.txt', 'a', newline='\n', encoding='utf8') as write_file:
            write_file.writelines(i + '\n')
