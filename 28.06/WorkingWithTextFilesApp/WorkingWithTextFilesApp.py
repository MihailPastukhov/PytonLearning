import json


def open_file(file_path, books_quantity_to_cut):
    book_list = []
    selected_books = []
    remaining_books = []
    json_data = open(file_path, 'r').read()

    data = json.loads(json_data)

    for i in data['books']:
        book_list.append(i)
    books_quantity = len(book_list)

    i = 0
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
    json.dump(selected_books, open(file_path + "_res01", 'w'), indent=12)
    json.dump(remaining_books, open(file_path + "_res02", 'w'), indent=12)


open_file(raw_input('Enter file path with filename '), raw_input('Enter books quantity to cut '))
