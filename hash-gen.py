import hashlib
import getpass

# Prompt for the password without echoing characters on screen
password = getpass.getpass("Enter your password: ")

# Generate the SHA-256 hash (64-character hexadecimal string)
password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

print("\nSHA-256 Hash:")
print(password_hash)
