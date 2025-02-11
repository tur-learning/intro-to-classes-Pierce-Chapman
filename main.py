from classes import Car

# Creating Car Objects
car1 = Car("Toyota", "Camry", 2015, 15000)
car2 = Car("Tesla", "Model 3", 2020, 35000)

# Printing Car Information
car1.print_info()
car2.print_info()

# Updating The Price of car1
car1.change_price(14000)

# Calculating the car's age
car1.calculate_age(2025)
car2.calculate_age(2025)
