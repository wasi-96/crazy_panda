from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command.Try again!")

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Enter the name of the book you want to add:')
    author = input('Enter the author of the book you wanna add:')

    database.add_book(name, author)


def list_book():
    books = database.get_all_books()
    for book in books:
        print(f"{book['name']} by {book['author']}, read: {book['read']}")


def prompt_read_book():
    name = input('Enter name of book you finished reading: ')

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of book you wanna delete:')

    database.delete_book(name)


menu()
