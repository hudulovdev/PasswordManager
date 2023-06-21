PASSWORDS_FILE = "passwords.txt"

def save_passwords(passwords):
    with open(PASSWORDS_FILE, "w") as file:
        for website, (username, password) in passwords.items():
            file.write(f"{website},{username},{password}\n")
    print("Passwords saved successfully!")

def load_passwords():
    try:
        with open(PASSWORDS_FILE, "r") as file:
            passwords = {}
            for line in file:
                website, username, password = line.strip().split(",")
                passwords[website] = (username, password)
        print("Passwords loaded successfully!")
        return passwords
    except FileNotFoundError:
        print("No passwords found. Starting with an empty database.")
        return {}

def add_password(passwords):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = (username, password)
    print("Password added successfully!")
    save_passwords(passwords)

def retrieve_password(passwords):
    website = input("Enter website: ")
    if website in passwords:
        username, password = passwords[website]
        print("Username:", username)
        print("Password:", password)
    else:
        print("Password not found!")

def delete_password(passwords):
    website = input("Enter website: ")
    if website in passwords:
        del passwords[website]
        print("Password deleted successfully!")
        save_passwords(passwords)
    else:
        print("Password not found!")

def display_menu():
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Delete Password")
    print("4. Quit")

# Load passwords from file when the program starts
passwords = load_passwords()

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_password(passwords)
    elif choice == '2':
        retrieve_password(passwords)
    elif choice == '3':
        delete_password(passwords)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Save passwords to file before quitting
save_passwords(passwords)

print("Goodbye!")
