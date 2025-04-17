import pyotp
import getpass
import hashlib

# Simulated user database using external application
# https://www.qr-code-generator.com/
users = {
    "alice": {
        "password_hash": hashlib.sha256("SecurePass123!".encode()).hexdigest(),
        "otp_secret": pyotp.random_base32()
    }
}

# allows for user registration
def register_user():
    username = input("Enter new username: ")
    password = getpass.getpass("Enter password: ")
    otp_secret = pyotp.random_base32()
    
    users[username] = {
        "password_hash": hashlib.sha256(password.encode()).hexdigest(),
        "otp_secret": otp_secret
    }
    print(f"\nMFA Setup Complete!\nScan this QR code in Google Authenticator:\n{pyotp.totp.TOTP(otp_secret).provisioning_uri(name=username, issuer_name='SecureCorp')}")

# Existing user (such as the user shown in simulated user database, 'alice')
def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    otp_input = input("OTP Code: ")
    
    user = users.get(username)
    if not user:
        print("Login failed")
        return
    
    # Verify password
    if hashlib.sha256(password.encode()).hexdigest() != user["password_hash"]:
        print("Login failed")
        return
    
    # Verify OTP
    totp = pyotp.TOTP(user["otp_secret"])
    if not totp.verify(otp_input):
        print("Login failed")
        return
    
    print("Login successful!")

if __name__ == "__main__":
    register_user()
    print("\n--- Login Test ---")
    login()
