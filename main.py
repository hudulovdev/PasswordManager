passwords = {}  # Dictionary to store passwords

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = (username, password)
    print("Password added successfully!")

def retrieve_password():
    website = input("Enter website: ")
    if website in passwords:
        username, password = passwords[website]
        print("Username:", username)
        print("Password:", password)
    else:
        print("Password not found!")

def delete_password():
    website = input("Enter website: ")
    if website in passwords:
        del passwords[website]
        print("Password deleted successfully!")
    else:
        print("Password not found!")

def display_menu():
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Quit")

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_password()
    elif choice == '2':
        retrieve_password()
    elif choice == '3':
        delete_password()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
