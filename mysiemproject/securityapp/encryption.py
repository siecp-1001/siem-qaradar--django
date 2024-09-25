from cryptography.fernet import Fernet

# Generate and store your key securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_log(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_log(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()
