import json


def open_file():
    json_data = open('books', 'r').read()

    data = json.loads(json_data)
    print(data)


open_file()





