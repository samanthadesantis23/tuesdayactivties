# Define the Book class
class Book:
    def __init__(self, name, author, genre, year):
        self.name = name  # Name of the book
        self.author = author  # Author of the book
        self.genre = genre  # Genre of the book
        self.year = year  # Year the book was published

# Function to determine the older book
def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f"The older book is {book1.name} by {book1.author}, published in {book1.year}.")
    elif book1.year > book2.year:
        print(f"The older book is {book2.name} by {book2.author}, published in {book2.year}.")
    else:
        print(f"Both books were published in the same year: {book1.year}.")

# Example usage
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

# Call the older_book function
older_book(python, everest)
older_book(python, norma)


