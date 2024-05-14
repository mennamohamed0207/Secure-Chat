
from DH import *
from Elgamal import *
import sys

import socket
import threading 
from commonFunctions import generate_key_from_password,send_msg,receive_msg




def Bob():
    #generate Diffie hellman keys
    q,alpha=readFile()
    Xb=readX(q)
    Yb=publicKey(Xb,alpha,q)

    #generate elgamal keys
    q2,alpha2=readFile_elgamal()
    Xb2 = generate_private_key_elgamal(q2)
    Yb2 = generate_public_key_elgamal(q2, alpha2, Xb2)

    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to listen on
    port = 21042

    # Create a socket object
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
    # Bind the socket to the host and port
        s.bind((host, port))
    except:
        print("binding error")
        return
    
    

    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(2)


    # Accept an incoming connection
    c, address = s.accept()

    #exchange elgamal keys
    Ya2 = int(c.recv(2048).decode("utf-8"))
    print("Bob received Ya2 from Alice: ",Ya2)
    c.sendall(str(Yb2).encode("utf-8"))
    print("Bob sent Yb2 to Alice : ",Yb2)

    m=hash_message_elgamal(str(Yb))
    m = m % q2
    s1,s2=sign_elgamal(m,q2,alpha2,Xb2)

    # Receive the secret key from the server
    Ya=int(c.recv(2048).decode("utf-8"))
    print("Bob received Ya from Alice: ",Ya)
    c.sendall(str(Yb).encode("utf-8"))
    print("Bob sent your Yb public key signed to Alice : ",Yb)
    s1_a=int(c.recv(2048).decode("utf-8"))
    print("Bob received s1_a from Alice: ",s1_a)
    c.sendall(str(s1).encode("utf-8"))
    print("Bob sent your s1 public key signed to Alice : ",s1)
    s2_a=int(c.recv(2048).decode("utf-8"))
    print("Bob received s2_a from Alice: ",s2_a)
    c.sendall(str(s2).encode("utf-8"))
    print("Bob sent your s2 public key signed to Alice : ",s2)

    ma=hash_message_elgamal(str(Ya))
    ma = ma % q2
    if not verify_elgamal(alpha2,ma,q2,Ya2,s1_a,s2_a):
        print("We've caught you! Terminating connection due to wrong digital signature...")
        s.close()  # Close the socket
        sys.exit()  # Exit the script
    else:
        print("Elgamal verification accepted")

    kb=symmetricKey(Xb,Ya,q)
    print("Your symmetric DH key: ",kb)
    key=generate_key_from_password(kb,kb)
    print("Your AES encryption key: ",key)

    threading.Thread(target=send_msg, args=(c,key)).start()
    threading.Thread(target=receive_msg, args=(c,key)).start()


if __name__ == "__main__":
    # Start the server
    Bob()
