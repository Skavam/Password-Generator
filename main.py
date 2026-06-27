# Password generator program by @Skavam on GitHub

import random 

def main():
    print("Welcome to the Password Generator")
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]';,/<>?{}|`~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    main()