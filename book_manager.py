import json
import os

class PersonalLibraryManager:
    def __init__(self, library_file='library.json'):
        self.library_file = library_file
        self.load_library()

    def load_library(self):
        if not os.path.exists(self.library_file):
            self.library = {}
        else:
            with open(self.library_file, 'r') as file:
                self.library = json.load(file)

    def save_library(self):
        with open(self.library_file, 'w') as file:
            json.dump(self.library, file, indent=4)

    def add_book(self, title, author):
        self.library[title] = {'author': author, 'read': False}
        self.save_library()

    def mark_as_read(self, title):
        if title in self.library:
            self.library[title]['read'] = True
            self.save_library()
        else:
            print(f"The book '{title}' was not found in your library.")

    def get_suggestions(self):
        unread_books = [book for book, details in self.library.items() if not details['read']]
        if unread_books:
            print("Here are some books you might want to read next:")
            for book in unread_books:
                print(book)
        else:
            print("You've read all the books in your library. Time to add some more!")

    def show_library(self):
        print("Your Library:")
        for title, details in self.library.items():
            read_status = 'Read' if details['read'] else 'Unread'
            print(f"{title} by {details['author']} - {read_status}")

# Example usage
if __name__ == "__main__":
    manager = PersonalLibraryManager()

    # Interactive command line interface to add/read books etc.
    # Implement CLI interactions based on your requirements here.
