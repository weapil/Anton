import json

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    def return_book(self, book):
        self.borrowed_books.remove(book)
    def __str__(self):
        borrowed_titles = ", ".join(book.title for book in self.borrowed_books)
        return f"{self.name} (ID: {self.reader_id}), Borrowed: {borrowed_titles}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        self.books.remove(book)
    def register_reader(self, reader):
        self.readers.append(reader)
    def lend_book(self, reader_id, book_title):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if reader and book:
            reader.borrow_book(book)
            self.remove_book(book)
        else:
            print("Book or Reader not found")
    def return_book(self, reader_id, book_title):
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)
        book = next((b for b in reader.borrowed_books if b.title == book_title), None)
        if reader and book:
            reader.return_book(book)
            self.add_book(book)
        else:
            print("Book or Reader not found")
    def find_book(self, title):
        return next((b for b in self.books if b.title == title), None)
    def save_to_file(self, filename):
        data = {
            "books": [{"title": b.title, "author": b.author, "year": b.year, "genre": b.genre} for b in self.books],
            "readers": [{"name": r.name, "reader_id": r.reader_id, "borrowed_books": [b.title for b in r.borrowed_books]} for r in self.readers]
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.books = [Book(**book) for book in data["books"]]
            self.readers = [Reader(reader["name"], reader["reader_id"]) for reader in data["readers"]]
            for reader, reader_data in zip(self.readers, data["readers"]):
                reader.borrowed_books = [self.find_book(title) for title in reader_data["borrowed_books"]]

if __name__ == "__main__":
    library = Library("My Library")
    library.add_book(Book("1984", "Лев Толстой", 1949, "Дистопия"))
    library.add_book(Book("Чудное мгновение", "Александр Пушкин", 1960, "Поэзия"))
    library.register_reader(Reader("Islam", 1))
    library.register_reader(Reader("Nurlan", 2))
    library.lend_book(1, "1984")
    print(library.readers[0])  # Вывод информации о читателе
    library.return_book(1, "1984")
    print(library.readers[0])  # Вывод информации о читателе
    library.save_to_file("library_state.json")
    new_library = Library("New Library")
    new_library.load_from_file("library_state.json")
    print([str(book) for book in new_library.books])  # Вывод всех книг
    print([str(reader) for reader in new_library.readers])  # Вывод всех читателей
