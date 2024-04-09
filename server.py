import socket
import threading 
from commonFunctions import *
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
    threading.Thread(target=receive, args=(c,)).start()
    send(c)
    c.close()


if __name__ == "__main__":
    # Start the server
    server()