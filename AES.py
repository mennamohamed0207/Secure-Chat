from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def generate_key_from_password(password):
    # Generate a key from a password
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)
    return key

def encrypt(message, key):
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad the message to ensure it's a multiple of the block size
    padded_message = pad(message.encode('utf-8'), AES.block_size)

    # Encrypt the padded message
    cipher_text = cipher.encrypt(padded_message)
    return cipher_text

def decrypt(cipher_text, key):
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the cipher text
    decrypted_message = cipher.decrypt(cipher_text)

    # Unpad the decrypted message
    unpadded_message = unpad(decrypted_message, AES.block_size)

    return unpadded_message.decode('utf-8')

# Example usage
password = "secretpassword"
key = generate_key_from_password(password)
message = "Hello, AES!"
encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)
