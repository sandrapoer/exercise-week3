# QUESTION NR 1
def count_vowels(text):
    if type(text) == str:
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for letter in text.lower():
            if letter in vowels:
                count += 1
        return count
    else:
        return 42

# QUESTION NR 2
def hamming(text1,text2):
    if len(text1) != len(text2):
        return 0
    hamming_distance = 0
    for i in range(0,len(text1),1):
        if text1[i] != text2[i]:
            hamming_distance += 1
    return hamming_distance

# QUESTION NR 3
class Vehicle():
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors
    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Doors: {self.doors}"

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers
    def __str__(self):
        return f"Color: {self.color}, Fuel Type: {self.fuel_type}, Passengers: {self.passengers}"

# QUESTION NR 4
class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __str__(self):
        return f"{self.name}, {self.author}"

# QUESTION NR 5
class Bookshelf():
    def __init__(self):
        self.book_list = []
    def add_book_list(self, books):
        for element in books:
            if type(element) == Book:
                self.book_list.append(element)

    def books_by_author(self, author):
        if not self.book_list:      #if list leer = false; not ändert boolean von true to false
            return []
        name_list = []
        for book in self.book_list:
            if book.author == author:
                name_list.append(book.name)
        return name_list

    def get_books(self):
        if not self.book_list:
            return []
        name_list = []
        for book in self.book_list:
            name_list.append(book.name)
        return name_list

    def clear_shelf(self):
        self.book_list.clear()

