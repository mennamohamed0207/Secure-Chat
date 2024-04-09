import socket
import threading
def receive(client):
    # Listen for messages from the client
    while 1:
        received_list=client.recv(2048).decode("utf-8").split("\n")
        print(received_list)
def send(client):
    # Send messages from the client
    while 1:
        message = input()
        client.sendall(str.encode("\n".join(message)))
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
    
    s.sendall(b"Hello, Server!")
    threading.Thread(target=receive, args=(s,)).start()
    send(s)
    s.close()

if __name__ == "__main__":
    # Start the client
    client()
