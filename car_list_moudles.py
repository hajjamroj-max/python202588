# orders.py - Car management with functional programming
from re import match
from functools import reduce

car_list = []

def show_menu():
    print("1) Add car")
    print("2. Find By Plate")
    print("3. Show cars")
    print("4. Exit")
    option = input("Enter your choice: ")
    print("-"*25)
    return option

# Validation functions
def car_name_validator(name):
    return match(r"^[a-zA-Z\s]{3,30}$", name) is not None

def car_module_validator(module):
    return match(r"^[a-zA-Z\s\d]{3,30}$", module) is not None

def car_plate_validator(plate):
    return match(r"^[\d][\d][\w][\d][\d][\d]\_iran[\d][\d]$", plate) is not None

def car_color_validator(color):
    valid_colors = ["white", "red", "blue", "black"]
    return color in valid_colors    

def car_check_validator(plate):
    for car in car_list:
        if car["plate"] == plate:
            return False
    return True

# Helper functions for functional programming
def get_car_name(car):
    """Extract car name for sorting"""
    return car["name"]

def format_car_info(car):
    """Format car information for display"""
    return f"{car['name']} {car['module']} - Plate: {car['plate']} - Color: {car['color']}"

def count_cars(total, car):
    """Count cars for reduce"""
    return total + 1

def get_car():
    print("\n--- Add cars ---")
    
    name = input("Name car: ")
    module = input("Module: ")
    plate = input("Enter The Plate: ")
    color = input("Color: ")
    
    if (car_name_validator(name) and 
        car_module_validator(module) and 
        car_plate_validator(plate) and 
        car_color_validator(color) and 
        car_check_validator(plate)):
        
        car = {
            "name": name,
            "module": module,
            "plate": plate,
            "color": color
        }
        car_list.append(car)
        print("Info: car added successfully")
        return car
    else:
        print("Error: Invalid Data!")
        return None

def find_by_plate():
    print("\n--- Find By Plate ---")
    if len(car_list) == 0:
        print("No cars available!")
        return
    
    search_plate = input("Enter plate to search: ")
    
    # Using filter to find cars with matching plate
    found_cars = [car for car in car_list if search_plate in car["plate"]]
    
    if len(found_cars) > 0:
        print("Found cars:")
        counter = 1
        for car in found_cars:
            print(f"{counter}. {format_car_info(car)}")
            counter = counter + 1
    else:
        print("No cars found!")

def show_cars():
    print("\n--- All Cars ---")
    if len(car_list) == 0:
        print("No cars available!")
        return
    
    counter = 1
    for car in car_list:
        print(f"{counter}. {format_car_info(car)}")
        counter = counter + 1
    
    # Using reduce to count total cars
    total_cars = reduce(count_cars, car_list, 0)
    print(f"\nTotal cars: {total_cars}")

# تابع مدیریت منو
def handle_menu_choice(choice):
    if choice == "1":
        get_car()
    elif choice == "2":
        find_by_plate()
    elif choice == "3":
        show_cars()
    elif choice == "4":
        print("Goodbye!")
        return False  # برای خروج از برنامه
    else:
        print("Invalid choice!")
    return True  # ادامه برنامه

# حلقه اصلی برنامه
def main():
    while True:
        choice = show_menu()
        if not handle_menu_choice(choice):
            break

# اجرای برنامه
if __name__ == "__main__":
    main()