from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

if not os.path.exists("key.key"):
    print("Key file not found. Generating a new one...")
    write_key()

master_pwd = input("What is your master password: ")
key = load_key()  
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            user, pas = line.rstrip().split("|")
            try:
                decrypted_password = fer.decrypt(pas.encode()).decode()
                print(f"Username: {user}, Password: {decrypted_password}")
            except Exception as e:
                print(f"Error decrypting password for {user}: {e}")

def create():
    username = input("Username: ")
    password = input("Password: ")
    
    with open('passwords.txt', 'a') as file:
        encrypted_password = fer.encrypt(password.encode()).decode()  
        file.write(username + "|" + encrypted_password + "\n")
        
    print("Password added successfully")

while True:
    pwd = input("Do you want to a)create or b)view password and username? or enter 'q' to quit: ").lower()
    if pwd == "q":
        break
    elif pwd == "a":
        create()
    elif pwd == "b":
        view()
    else:
        print("Invalid input!")
