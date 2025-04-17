import random
import string
import time
import getpass

# In-memory “user database”
USER_DB = {
    'alice': {
        'password': 'password',
    },
    "bob": {
        "password": "BobSecurePassword$",
    }
}

# Generates a random numerical OTP of a specified length.
def generate_otp(length=6):
    """Generate a numeric OTP of given length."""
    return ''.join(random.choices(string.digits, k=length))

# Simulate sending OTP to the user (in this case, OTP is printed in terminal)
def send_otp_to_user(username, otp):
    print(f"[Simulated delivery] OTP for {username}: {otp}")

def authenticate(username):
    # Something user knows: password
    stored = USER_DB.get(username)
    if not stored:
        print("Unknown user.")
        return False

    pwd = getpass.getpass("Enter your password: ")
    if pwd != stored['password']:
        print("Password incorrect.")
        return False

    # Something user has: OTP
    otp = generate_otp()
    send_otp_to_user(username, otp)

    # In real systems, OTP expires quickly, and hence, this simulates a short window
    start = time.time()
    entered = input("Enter the OTP you received: ")
    if time.time() - start > 60:
        print("OTP expired.")
        return False

    if entered != otp:
        print("OTP incorrect.")
        return False

    return True

def main():
    print("=== Welcome to MFA Demo ===")
    user = input("Username: ")
    if authenticate(user):
        print("Authentication successful. Access granted.")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
