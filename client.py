import socket
import threading
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
    def verify(message):
        return True



def client():
    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to connect to
    port = 21042

    # Create a socket object
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Connect to the server
    try:
        s.connect((host, port))
    except:
        print("Server not found")
        return
    
    # Generate a public and private key
    public_key, private_key = ElGamal.generate_keys()

    # Send the public key to the server
    s.sendall(str(public_key).encode())
    print("You sent to Bob : ",public_key)

    # Receive the public key from the client
    secret_key=int(s.recv(2048).decode("utf-8"))
    print("You received from Bob: ",secret_key)
    key=s.recv(2048)
    print("key Encryption received : ",key)
    print("from the client the type",type(key))
    print("from the client the size",len(key))
    threading.Thread(target=send_msg, args=(s,key)).start()
    threading.Thread(target=receive_msg, args=(s,key)).start()
    # s.close()

if __name__ == "__main__":
    # Start the client
    client()
