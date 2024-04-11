import socket
import threading
from commonFunctions import *


class ElGamal:
    __init__ = None

    @staticmethod
    def generate_keys():
        return 333, 444
    
    @staticmethod
    def encrypt(message):
        return message

    @staticmethod
    def verify(message):
        return False

    @staticmethod
    def decrypt(message):
        return message
        

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
    print("You sent : ",public_key)

    # Receive the public key from the client
    secret_key=int(s.recv(2048).decode("utf-8"))
    print("You received : ",secret_key)

    threading.Thread(target=send_msg, args=(s,)).start()
    threading.Thread(target=receive_msg, args=(s,)).start()
    # send(s)
    # s.close()

def send_msg(c):
    while 1:
        # Send messages from the client
        message = input()
        message = ElGamal.encrypt(message).encode()
        c.sendall(message)

def receive_msg(c):
    while 1:
        # Listen for messages from the client       
        message=c.recv(2048).decode("utf-8")
        if message == "exit":
            print("the connection is closed")
            break
        if ElGamal.verify(message)==False:
            print("Untrusted Connection")
            c.sendall("exit".encode())
            break
        print("You RECEIVED:",ElGamal.decrypt(message))
    c.close()    


if __name__ == "__main__":
    # Start the client
    client()
