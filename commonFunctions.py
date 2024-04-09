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
        