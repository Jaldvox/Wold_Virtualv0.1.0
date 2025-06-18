from cryptography.fernet import Fernet

def generate_key():
    """Generates a new encryption key."""
    return Fernet.generate_key()

def encrypt_data(data: bytes, key: bytes) -> bytes:
    """Encrypts the given data using the provided key."""
    fernet = Fernet(key)
    return fernet.encrypt(data)

def decrypt_data(encrypted_data: bytes, key: bytes) -> bytes:
    """Decrypts the given encrypted data using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data)