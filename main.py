import os
import shutil
import random
import string
import socket

# Sign in
def sign_in():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        with open("users.txt", "r") as f:
            data = f.read()
            if f"{username},{password}" in data:
                print("Welcome!")
                break
            else:
                print("Invalid username or password. Please try again.")

# Sign up
def sign_up():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        password_confirm = input("Confirm Password: ")
        if password != password_confirm:
            print("Passwords do not match. Please try again.")
        else:
            with open("users.txt", "a") as f:
                f.write(f"{username},{password}\n")
            print("User created!")
            break

# Generate random filename
def random_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + ".txt"

# Create text file
def create_file():
    filename = input("Enter filename: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    with open(filename, "w") as f:
        text = input("Enter text: ")
        f.write(text)
    print(f"{filename} created.")

# Copy text file to server
def copy_to_server():
    filename = input("Enter filename to copy to server: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        shutil.copyfile(filename, os.path.join(os.getcwd(), "server", filename))
        print(f"{filename} copied to server.")
    except FileNotFoundError:
        print("File not found.")

# List available text files on server
def list_server_files():
    if not os.path.exists("server"):
        os.mkdir("server")
    files = os.listdir("server")
    if len(files) == 0:
        print("No files in server directory")
    else:
        print("Server files:")
        for f in files:
            print(f)

# Read text file from server
def read_from_server():
    filename = input("Enter filename to read from server: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    try:
        with open(os.path.join(os.getcwd(), "server", filename), "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

# Show available commands
def show_commands():
    print("""
1. Create a text file
2. Copy a text file to server
3. List available text files on server(SMB)
4. Read a text file from server
5. Show available commands
6. Exit
""")

# Main program loop
def main():
    sign_in()
    while True:
        choice = input("Enter choice: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            copy_to_server()
        elif choice == "3":
            list_server_files()
        elif choice == "4":
            read_from_server()
        elif choice == "5":
            show_commands()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    sign_up()
    main()
