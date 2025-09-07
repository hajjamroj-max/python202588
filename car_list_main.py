from car_list_moudles import *
while True:
    option = show_menu()
    
    if option == "1":
        get_car()
    elif option == "2":
        find_by_plate()
    elif option == "3":
        show_cars()
    elif option == "4":
        break
    else:
        print("Invalid!")
    
    input("Enter...")