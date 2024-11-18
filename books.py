# Book 1
book_object1 = {
    "ID": 1,
    "Title": "The Great Gatsby",
    "Author": "F. Scott Fitzgerald",
    "Genre": "Fiction",
    "Published Year": 1925,
    "ISBN": "978-0743273565",
    "Stock": 20,
    "Price": 15.99
}

# Book 2
book_object2 = {
    "ID": 2,
    "Title": "To Kill a Mockingbird",
    "Author": "Harper Lee",
    "Genre": "Fiction",
    "Published Year": 1960,
    "ISBN": "978-0060935467",
    "Stock": 35,
    "Price": 10.99
}

# Book 3
book_object3 = {
    "ID": 3,
    "Title": "1984",
    "Author": "George Orwell",
    "Genre": "Dystopian",
    "Published Year": 1949,
    "ISBN": "978-0451524935",
    "Stock": 40,
    "Price": 9.99
}

# Book 4
book_object4 = {
    "ID": 4,
    "Title": "The Catcher in the Rye",
    "Author": "J.D. Salinger",
    "Genre": "Fiction",
    "Published Year": 1951,
    "ISBN": "978-0316769488",
    "Stock": 25,
    "Price": 8.99
}

# Book 5
book_object5 = {
    "ID": 5,
    "Title": "A Brief History of Time",
    "Author": "Stephen Hawking",
    "Genre": "Non-fiction",
    "Published Year": 1988,
    "ISBN": "978-0553380163",
    "Stock": 10,
    "Price": 18.99
}

# List of Books
books = [book_object1, book_object2, book_object3, book_object4, book_object5]

# Iterate through the list of books and print details
for book in books:
    print(f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, "
          f"Genre: {book['Genre']}, Published Year: {book['Published Year']}, "
          f"ISBN: {book['ISBN']}, Stock: {book['Stock']}, Price: {book['Price']}")
