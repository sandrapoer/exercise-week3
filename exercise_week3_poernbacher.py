# QUESTION NR 1
def count_vowels(text):
    if type(text) == int:
        return 42
    else:
        return len(text)

# QUESTION NR 2
def hamming(text1, text2):
    if len(text1) not len(text2):
        return 0

    hamming_distance = 0

    return hamming_distance

# QUESTION NR 3
class Vehicle():
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def doors(self, doors):
        self.doors = doors

    def __str__(self):
        return f"Color: {color}, Fuel Type: {fuel_type}, Doors: {doors}"

class Bus(Vehicle):
    def passengers(self, passengers):
        self.passengers = passengers

    def __str__(self):
        f"Color: {color}, Fuel Type: {fuel_type}, Doors: {doors}, Passengers: {passengers}"


# QUESTION NR 4
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return print(f"{name}, {author}")

# QUESTION NR 5
class BookShelf():
    def __init__(self):
        pass

    def add_book_list(self, books):
        self.books = books

    def books_by_author(self, author):
        self.author = author
        return

    def get_books(self):
        return

    def clear_shelf(self):
