import hashlib
import getpass

# dictionary to store the passwords
password_manager = {}

# create account function
def create_account():
    # get the username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    # hash the password
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    # store the username and password in the password manager
    password_manager[username] = hash_password
    print("Account created successfully!")


# login function
def login():
    # get the username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    # hash the password
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    # check if the username is in the password manager
    if username in password_manager:
        # check if the password is correct
        if password_manager[username] == hash_password:
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")

# main function
def main():
    while True:
        choice = input("Enter '1' to create an account, '2' to login, or '3' to exit: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

# call the main function
if __name__ == "__main__":
    main()