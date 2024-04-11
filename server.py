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


    # Receive the secret key from the server
    secret_key=int(c.recv(2048).decode("utf-8").split("\n")[0])
    print("You received : ",secret_key)

    # Send the public key to the client
    c.sendall(str(public_key).encode())
    print("You sent : ",public_key)


    threading.Thread(target=send_msg, args=(c,)).start()
    threading.Thread(target=receive_msg, args=(c,)).start()
    # send(c)
    # c.close()

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
    # Start the server
    server()
