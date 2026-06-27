# Password generator program by @Skavam on GitHub

import random 
from colorama import Fore

def main():
    print("Welcome to the Password Generator")
    length = float(input("Enter the desired password length: "))

    if length <= 0:
        print(f"{Fore.RED}Please enter a valid positive number for the password length.{Fore.RESET}")
        return
    
    password = generate_password(int(length))
    print(f"Generated Password: {Fore.GREEN}{password}{Fore.RESET}")

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]';,/<>?{}|`~"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    main()
