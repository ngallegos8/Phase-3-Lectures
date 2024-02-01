class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_books(self, book):
        for b in book:
            if type(b) is Book:
                self.books.append(b)
            else:
                raise Exception("Must be a book")



class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.Library = None


if __name__ == "__main__":
    dpl = Library("Denver Public Library", "Denver")
    star_wars = Book("Revenge of the Sith", "John", "Sci-Fi")
    harry_potter = Book("Prisoner of Azkaban", "Rowling", "Fantasy")
    dpl.add_books([star_wars, harry_potter])
    star_wars.Library = dpl
    harry_potter.Library = dpl

print(dpl.books)
print(star_wars.Library)
print(harry_potter.Library.name)
