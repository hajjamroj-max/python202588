# Users list
users = [
    {'id': 1, 'username': 'admin', 'password': '123', 'isLocked': False},
    {'id': 2, 'username': 'user1', 'password': 'pass1', 'isLocked': False},
    {'id': 3, 'username': 'locked_user', 'password': 'pass2', 'isLocked': True}
]

# Show menu
def show_menu():
    print('\n=== MAIN MENU ===')
    print('1. Add User')
    print('2. Login Check')
    print('3. Show Users')
    print('4. Exit')
    print('================')

# Add User
def add_user():
    username = input('Enter username: ')
    
    # Check if username exists
    existing_users = []
    for user in users:
        if user['username'] == username:
            existing_users.append(user)
    
    if existing_users:
        print('Username already exists!')
        return
    
    password = input('Enter password: ')
    lock_status = input('Lock user? (y/n): ')
    
    # Create new ID
    max_id = 0
    for user in users:
        if user['id'] > max_id:
            max_id = user['id']
    new_id = max_id + 1
    
    new_user = {
        'id': new_id,
        'username': username,
        'password': password,
        'isLocked': lock_status.lower() == 'y'
    }
    
    users.append(new_user)
    print('User added successfully!')

# Login Check
def login_check():
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    # Find user
    found_user = None
    for user in users:
        if user['username'] == username:
            found_user = user
            break
    
    if found_user is None:
        print('User not found')
    else:
        if found_user['isLocked']:
            print('User is locked')
        elif found_user['password'] == password:
            print('Login successful')
        else:
            print('Wrong password')

# Show Users
def show_users():
    print('\n=== USER LIST ===')
    
    if not users:
        print('No users found')
        return
    
    # Sort users by username
    sorted_users = sorted(users, key=lambda user: user['username'])
    
    print('Active Users:')
    active_users = []
    for user in sorted_users:
        if not user['isLocked']:
            active_users.append(user)
    
    for i, user in enumerate(active_users):
        print(f"{i+1}. ID: {user['id']} | Username: {user['username']}")
    
    print('\nLocked Users:')
    locked_users = []
    for user in sorted_users:
        if user['isLocked']:
            locked_users.append(user)
    
    for i, user in enumerate(locked_users):
        print(f"{i+1}. ID: {user['id']} | Username: {user['username']}")
    
    # Calculate statistics
    active_count = len(active_users)
    locked_count = len(locked_users)
    total_count = len(users)
    
    print(f'\nTotal: {total_count} users ({active_count} active, {locked_count} locked)')
    print('=================')

# Main program
def run_program():
    print('Welcome to User Management System!')
    


# Start program
run_program()