from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad,unpad
import hashlib

def send_msg(c,key):
    while 1:
        # Send messages from the client
        message = input()
        message_encrypted = encrypt(message,key)
        c.sendall(message_encrypted)
        if message =="exit":
            print("Chat is closed")
            c.close()

def receive_msg(c,key):
    while 1:
        # Listen for messages from the client
        message=c.recv(2048)
        message_decrypted=decrypt(message,key)
        # if decrypt(message,key) =="exit":
        #     print("Chat is closed")
        #     c.close()
        print("You RECEIVED:",message_decrypted) 
       
    c.close() 

def recieve_key(c):
    return c.recv(2048)

def send_key(c,key):
    c.sendall(key)
    
def encrypt(message, key):
      # Create an AES cipher object
      cipher = AES.new(key, AES.MODE_ECB)
      # Pad the message to ensure it's a multiple of the block size
      padded_message = pad(message.encode('utf-8'), AES.block_size)
      # Encrypt the padded message
      cipher_text = cipher.encrypt(padded_message)
      return cipher_text
  
  
def decrypt(cipher_text,key):
        # Create an AES cipher object
        cipher = AES.new(key, AES.MODE_ECB)  
        # Decrypt data
        decrypted_text = cipher.decrypt(cipher_text)
        unpadded_data = unpad(decrypted_text, AES.block_size)
        return unpadded_data.decode('utf-8')
    
def generate_key_from_password(password,salt):
       # Generate a key from a password
    password_str = str(password)
    key = hashlib.sha256(password_str.encode()).digest()
    return key