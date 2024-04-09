import socket
import threading
from commonFunctions import *
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
    
    s.sendall(f"Hello, Server!")
    threading.Thread(target=receive, args=(s,)).start()
    send(s)
    s.close()

if __name__ == "__main__":
    # Start the client
    client()
