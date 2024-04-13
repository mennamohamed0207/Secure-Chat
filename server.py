import socket
import threading 
from commonFunctions import *
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad



class ElGamal:
    __init__ = None

    @staticmethod
    def generate_keys():
        return 333, 444
    
    @staticmethod
    def generate_key_from_password():
        # Generate a key from a password
        salt = get_random_bytes(16)
        key = salt
        print(key)
        return key
    
    @staticmethod
    def verify(message):
        return True


def server():
    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to listen on
    port = 21042

    # Create a socket object
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except:
        print("binding error")
        return
    
    
    # Bind the socket to the host and port

    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(2)


    # Accept an incoming connection
    c, address = s.accept()

    
    # Generate a public and private key
    public_key, private_key = ElGamal.generate_keys()
    key=ElGamal.generate_key_from_password()
    # Receive the secret key from the server
    secret_key=int(c.recv(2048).decode("utf-8").split("\n")[0])
    print("You received public key from Alice: ",secret_key)

    # Send the public key to the client
    c.sendall(str(public_key).encode())
    print("You sent public key to Alice: ",public_key)

    send_key(c,key)
    threading.Thread(target=send_msg, args=(c,key)).start()
    threading.Thread(target=receive_msg, args=(c,key)).start()
    # c.close()




if __name__ == "__main__":
    # Start the server
    server()
