import socket
import threading
import socket
import threading 
from commonFunctions import *
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from DH import *

class ElGamal:
    __init__ = None

    @staticmethod
    def generate_keys():
        return 333, 444
   
    
    @staticmethod
    def verify(message):
        return True



def client():
    q,pr=readFile()
    x=readX(q)
    y=publicKey(x,pr,q)
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
    s.sendall(str(y).encode())
    print("You sent to Bob : ",y)

    # Receive the public key from the client
    public_key_yb=int(s.recv(2048).decode("utf-8"))
    print("You received from Bob: ",public_key_yb)
    ka=symmetricKey(x,public_key_yb,q)
    print("Your symmetric DH key: ",ka)
    key=generate_key_from_password(ka,ka)
    print("key AES Encryption received : ",key)
    threading.Thread(target=send_msg, args=(s,key)).start()
    threading.Thread(target=receive_msg, args=(s,key)).start()
    # s.close()

if __name__ == "__main__":
    # Start the client
    client()
