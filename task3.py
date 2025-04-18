import bcrypt
import itertools
import string
import time
import os

FILENAME = "hashed_password.txt"

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
    chars = string.ascii_lowercase
    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(chars, repeat=length):
            guess = ''.join(guess_tuple)
            if check_password(guess, stored_hash):
                print(f"[+] Password cracked using brute force: {guess}")
                return guess
    print("[-] Brute force attack failed.")
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
    
    # author note by carmel:
    # testing this can take a while; i suggest you comment the attacks you dont want to use
    # or else it can take quite a long time to run

    '''
    # intelligent guess attack
    start = time.time()
    cracked_password = intelligent_guess_attack(stored_hash, user_info)
    end = time.time()
    print(f"[*] Total simulation time for intelligent guess attack: {end - start:.2f} seconds")
    '''
    
    # brute force
    start = time.time()
    cracked_password = brute_force_attack(stored_hash)
    end = time.time()
    print(f"[*] Total simulation time for brute force attack: {end - start:.2f} seconds")
    
    '''
    # dictionary attack first
    start = time.time()
    cracked_password = dictionary_attack(stored_hash)
    end = time.time()
    print(f"[*] Total simulation time for dictionary attack: {end - start:.2f} seconds")
    '''
    
    if cracked_password:
        print(f"\n Cracked Password: {cracked_password}")
    else:
        print("\n Password could not be cracked.")

if __name__ == "__main__":
    main()
