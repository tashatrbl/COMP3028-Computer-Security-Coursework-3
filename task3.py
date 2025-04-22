import bcrypt
import itertools
import string
import time
import os
import subprocess

FILENAME = "hashed_password.txt"

# run with JTR
# cd john/run
# python3 task3.py

# how to run:
# set the password using task1.py
# run task3.py after

# loading the file with the hashed password
def load_hash():
    with open(FILENAME, "rb") as f:
        return f.read()

# function to verify a guess against the bcrypt hash; since task 1 uses bcrypt
def check_password(guess, stored_hash):
    return bcrypt.checkpw(guess.encode(), stored_hash)

# dictionary attack
def dictionary_attack(stored_hash):
    print("\n[*] Starting Dictionary Attack...")
    try:
        # common_passwords has been adapted from this document:
        # https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
        # only 1000 lines in here because 10k is too long for simulation
        
        with open("common_passwords.txt", "r") as f:
            for line in f:
                pwd = line.strip()
                if check_password(pwd, stored_hash):
                    print(f"[+] Password cracked using dictionary attack: {pwd}")
                    return pwd
    except FileNotFoundError:
        print("[-] Dictionary file not found.")
    print("[-] Dictionary attack failed.")
    return None

# intelligent guess attack
def intelligent_guess_attack(stored_hash, user_info):
    print("\n[*] Starting Intelligent Guess Attack...")
    guesses = [
        user_info['name'],
        user_info['name'] + "123",
        user_info['birthyear'],
        user_info['name'] + user_info['birthyear'],
        user_info['pet'],
        user_info['pet'] + "123",
    ]
    for guess in guesses:
        if check_password(guess, stored_hash):
            print(f"[+] Password cracked using intelligent guess: {guess}")
            return guess
    print("[-] Intelligent guess attack failed.")
    return None

# brute force 
# for simulation purposes, i made set the max length to 3 - can change
# if testing this, use passwords with only 3 characters or whatever number you chose
# or else it will always fail
def brute_force_attack(stored_hash, max_length= 4):
    print("\n[*] Starting Brute Force Attack ...")
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(chars, repeat=length):
            guess = ''.join(guess_tuple)
            if check_password(guess, stored_hash):
                print(f"[+] Password cracked using brute force: {guess}")
                return guess
    print("[-] Brute force attack failed.")
    return None
    
# john the ripper
def write_john_input(stored_hash):
    with open("jtr.txt", "w", newline="\n") as f:
        f.write(f"user:{stored_hash.decode()}\n")
        
    with open("jtr.txt", "r") as f:
        content = f.read()
        print(f"File length (in characters): {len(content)}")

def john_the_ripper_attack():
    print("\n[*] Starting John the Ripper Attack...")

    # Run john on the input file
    try:
        subprocess.run(["../john", 
       "--format=bcrypt", 
       "--wordlist=common_passwords.txt",
       "jtr.txt"], check=True)

        # Now get the cracked password
        result = subprocess.run(["../john", 
        "--show", 
        "jtr.txt"], 
        capture_output=True, 
        text=True)
        output = result.stdout.strip()
        
        # The format is: user:password
        if ":" in output:
            cracked = output.split(":")[1].splitlines()[0]
            print(f"[+] Password cracked using John the Ripper: {cracked}")
            return cracked
        else:
            print("[-] John the Ripper did not crack the password.")
            return None
    except FileNotFoundError:
        print("[-] John the Ripper is not installed or not in PATH.")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running John the Ripper: {e}")
        return None


def main():
    if not os.path.exists(FILENAME):
        print("❌ Error: hashed_password.txt not found.")
        return

    stored_hash = load_hash()

    # for intelligent attack, we will simply simulate the user info
    # realistically, this info would have been found through online presence or personal knowledge
    user_info = {
        "name": "carmel",
        "birthyear": "2004",
        "pet": "beans"
    }


    cracked_password = None
   
    while True:
        print("\n=== Which tool would you like to use? ===")
        print("1. Intelligent Guess Attack")
        print("2. Brute Force Attack")
        print("3. Dictionary Attack")
        print("4. John the Ripper Attack")
        print("5. Exit")
        
        choice = input("Choose a number: ")
        if choice == "1":
            # intelligent guess attack
            start = time.time()
            cracked_password = intelligent_guess_attack(stored_hash, user_info)
            end = time.time()
            print(f"[*] Total simulation time for intelligent guess attack: {end - start:.2f} seconds")
        elif choice == "2":
            # brute force
            start = time.time()
            cracked_password = brute_force_attack(stored_hash)
            end = time.time()
            print(f"[*] Total simulation time for brute force attack: {end - start:.2f} seconds")
        
        elif choice == "3":
            # dictionary attack
            start = time.time()
            cracked_password = dictionary_attack(stored_hash)
            end = time.time()
            print(f"[*] Total simulation time for dictionary attack: {end - start:.2f} seconds")
        
        elif choice == "4":
            # john the ripper
            write_john_input(stored_hash)
            start = time.time()
            cracked_password = john_the_ripper_attack()
            end = time.time()
            print(f"[*] Total simulation time for John the Ripper attack: {end - start:.2f} seconds")
        
        elif choice == "5":
            print("Exiting. Bye 👋")
            break

        else:
            print("❌ Incorrect selection. Try again.")

    	   
    if cracked_password:
        print(f"\n Cracked Password: {cracked_password}")
    else:
        print("\n Password could not be cracked.")

if __name__ == "__main__":
    main()