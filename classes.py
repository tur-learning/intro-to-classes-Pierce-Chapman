class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def print_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year}) - ${self.price}")
    
    def change_price(self, new_price): 
        self.price = new_price 
        print(f"Updated price: ${self.price}")

    def calculate_age(self, current_year):
        age = current_year - self.year
        print(f"This {self.brand} {self.model} is {age} years old.")