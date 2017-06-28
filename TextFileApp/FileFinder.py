import json
import os


def select_books(file_path, books_quantity_to_cut):
    book_list = []
    selected_books = []
    remaining_books = []
    if os.path.isfile(file_path):
        json_data = open(file_path, 'r').read()
        data = json.loads(json_data)
        for i in data['books']:
            book_list.append(i)
        books_quantity = len(book_list)
        i = 0
        if books_quantity > 0:
            while i < int(books_quantity):
                if i < int(books_quantity_to_cut):
                    selected_books.append(book_list[i])
                    i = i + 1
                else:
                    remaining_books.append(book_list[i])
                    i = i + 1
            print selected_books
            print '\n'
            print remaining_books
            selected_books_file_name = file_path + "_res01"
            remaining_books_file_name = file_path + "_res02"
            result_file_path = os.path.abspath(selected_books_file_name)
            json.dump(selected_books, open(selected_books_file_name, 'w'), indent=12)
            json.dump(remaining_books, open(remaining_books_file_name, 'w'), indent=12)
            return result_file_path
        else:
            return None
    else:
        print("No files in this folder.")

res = select_books(raw_input('Enter file path with filename '), raw_input('Enter books quantity to cut '))
