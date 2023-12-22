from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Function to generate AES key for encryption
def generate_aes_key():
    password = b'tiago'  # Replace with your own secret password
    salt = b'1234'  # Replace with your own salt value

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=16,  # 16 bytes for AES-128
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = kdf.derive(password)
    return key

# Function to generate HMAC-SHA256 key for authentication
def generate_hmac_key():
    password = b'ogait'  # Replace with your own secret password
    salt = b'4321'  # Replace with your own salt value

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for HMAC-SHA256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = kdf.derive(password)
    return key

# Generate AES key for encryption
encryption_key = generate_aes_key()

# Generate HMAC-SHA256 key for authentication
auth_key = generate_hmac_key()

# Save keys to file
with open('pw', 'wb') as file:
    file.write(encryption_key)
    file.write(auth_key)

print("Keys generated and saved to 'pw' file.")
