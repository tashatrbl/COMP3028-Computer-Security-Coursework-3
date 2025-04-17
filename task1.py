import bcrypt
import os

FILENAME = "hashed_password.txt"

# Hashes a password with a new salt
def hash_password(plain_password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_password.encode(), salt)

# Verifies a password against stored hash
def verify_password(plain_password, stored_hash):
    return bcrypt.checkpw(plain_password.encode(), stored_hash)

# Save hashed password
def save_hash(hashed_password):
    with open(FILENAME, "w") as f:
        f.write(hashed_password.decode())

# Load hashed password
def load_hash():
    with open(FILENAME, "r") as f:
        return f.read().encode()

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Create new password")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            password = input("Set your password: ")
            hashed = hash_password(password)
            save_hash(hashed)
            print("✅ New password created.")

        elif choice == "2":
            if not os.path.exists(FILENAME):
                print("❌ No saved password found. Please create one first.")
                continue

            stored_hash = load_hash()
            while True:
                login_password = input("Enter your password (or type 'back' to return to menu): ")
                if login_password.lower() == 'back':
                    break
                if verify_password(login_password, stored_hash):
                    print("✅ Login successful!")
                    break
                else:
                    print("❌ Incorrect password. Try again or type 'back' to cancel.")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
