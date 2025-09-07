from user_moudels import *

while True:
    show_menu()
    choice = input('Choose option (1-4): ')
        
    if choice == '1':
        add_user()
    elif choice == '2':
        login_check()
    elif choice == '3':
        show_users()
    elif choice == '4':
        print('Exiting program...')
        break
    else:
        print('Invalid choice! Please enter 1-4.')