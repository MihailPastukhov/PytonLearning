import json
import os


def select_books(file_path, books_quantity_to_cut):
    book_list = []
    selected_books = []
    remaining_books = []
    if os.path.isfile(file_path):
        json_file = open(file_path, 'r').read()
        json_data = json.loads(json_file)

        for i in json_data['books']:
            book_list.append(i)
        books_quantity = len(book_list)

        try:
            books_quantity_to_cut = int(books_quantity_to_cut)
        except ValueError:
            print('A number must be entered.')

        if books_quantity_to_cut < 0:
            books_quantity_to_cut = 10

        i = 0
        while i < int(books_quantity):
            if i < books_quantity_to_cut:
                selected_books.append(book_list[i])
                i = i + 1
            else:
                remaining_books.append(book_list[i])
                i = i + 1
        selected_books_file_name = file_path + "_res01"
        remaining_books_file_name = file_path + "_res02"
        result_file_path = str(os.path.abspath(selected_books_file_name))
        json.dump(selected_books, open(selected_books_file_name, 'w'), indent=4)
        json.dump(remaining_books, open(remaining_books_file_name, 'w'), indent=4)
        return result_file_path
    else:
        return None


res = select_books(raw_input('Enter file path with filename '), raw_input('Enter books quantity to cut '))
if res:
    print res
else:
    print("No files in this folder.")

