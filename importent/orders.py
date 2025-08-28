from re import match
car_list = []

def show_menu():
    print("1) Add car")
    print("2. Find By Plate")
    print("3. Show cars")
    print("4) Exit")
    option = input("Enter your choice: ")
    print("-"*25)
    return option

def car_name_validator(name):
    if match(r"^[a-zA-Z\s]{3,30}$", name):
        return True
    else:
        return False

def car_moudle_validator(moudle):
    if match(r"^[a-zA-Z\s\d]{3,30}$", moudle):
        return True
    else:
        return False

def car_plate_validator(plate):
    if match(r"^[\d][\d][\w][\d][\d][\d]\_iran[\d][\d]$", plate):
        return True
    else:
        return False

def car_color_validator(color):  # تصحیح: color بجای name
    if color == "white":
        return True
    elif color == "red":
        return True
    elif color == "blue":
        return True
    elif color == "black":
        return True
    else:
        return False

def car_check_validator(plate):
    for car in car_list:
        if car["plate"] == plate:  # تصحیح: car["plate"] بجای plate
            return False
    return True  # تصحیح: خارج از حلقه

def get_car():
    print("\n--- Add cars ---")
    
    # تصحیح: همه خطوط داخل تابع
    name = input("Name car: ")
    module = input("Module: ")  # تصحیح: module بجای moudle
    plate = input("Enter The Plate: ")  # تصحیح: string بجای int
    color = input("Color: ")
    
    # تصحیح: خط شکسته و فراخوانی تابع
    if (car_name_validator(name) and 
        car_moudle_validator(module) and 
        car_plate_validator(plate) and 
        car_color_validator(color) and 
        car_check_validator(plate)):
        
        # تصحیح: dictionary درست
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
    
    for car in car_list:
        if car["plate"] == search_plate:
            print(f"Found: {car['name']} {car['module']}")
            print(f"Plate: {car['plate']}")
            print(f"Color: {car['color']}")
            return
    
    print("Car not found!")

def show_cars():
    print("\n--- All Cars ---")
    if len(car_list) == 0:
        print("No cars available!")
        return
    
    for i, car in enumerate(car_list, 1):
        print(f"\n{i}. {car['name']} {car['module']}")
        print(f"   Plate: {car['plate']}")
        print(f"   Color: {car['color']}")
        print("-" * 30)