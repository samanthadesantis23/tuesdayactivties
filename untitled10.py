# Define the Book class
class Book:
    def __init__(self, name, author, genre, year):
        self.name = name  # Name of the book
        self.author = author  # Author of the book
        self.genre = genre  # Genre of the book
        self.year = year  # Year the book was published

# Function to filter books by genre
def books_of_genre(books: list, genre: str) -> list:
    # Use a list comprehension to filter books that match the specified genre
    return [book for book in books if book.genre == genre]

# Example usage
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)
the_snowman = Book("The Snowman", "Jo Nesbø", "crime", 2007)

# Create a list of books
books = [python, everest, norma, the_snowman]

# Print books in the "crime" genre
print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")
