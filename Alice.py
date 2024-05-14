import socket
import threading
import socket
import threading 
from commonFunctions import *
from DH import *
from Elgamal import *
import sys


def Alice():
    #generate Diffie hellman keys
    q,alpha=readFile()
    Xa=readX(q)
    Ya=publicKey(Xa,alpha,q)

    #generate elgamal keys
    q2,alpha2=readFile_elgamal()
    Xa2 = generate_private_key_elgamal(q2)
    Ya2 = generate_public_key_elgamal(q2, alpha2, Xa2)

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
    
    #exchange elgamal keys
    s.sendall(str(Ya2).encode("utf-8"))
    print("Alice sent Ya2 to Bob : ",Ya2)

    Yb2 = int(s.recv(2048).decode("utf-8"))
    print("Alice received Yb2 from Bob: ",Yb2)

    m=hash_message_elgamal(str(Ya))
    m = m % q2
    s1,s2=sign_elgamal(m,q2,alpha2,Xa2)

    # Send the public key and s1, s2 (signed public key)
    s.sendall(str(Ya).encode("utf-8"))
    print("Alice sent Ya signed to Bob : ",Ya)
    Yb=int(s.recv(2048).decode("utf-8"))
    print("Alice received Yb from Bob: ",Yb)
    s.sendall(str(s1).encode("utf-8"))
    print("Alice sent s1 signed to Bob : ",s1)
    s1_b=int(s.recv(2048).decode("utf-8"))
    print("Alice received s1-b from Bob: ",s1_b)
    s.sendall(str(s2).encode("utf-8"))
    print("Alice sent s12 signed to Bob : ",s2)
    s2_b=int(s.recv(2048).decode("utf-8"))
    print("Alice received s2_b from Bob: ",s2_b)

    mb=hash_message_elgamal(str(Yb))
    mb = mb % q2
    if not verify_elgamal(alpha2,mb,q2,Yb2,s1_b,s2_b):
        print("We've caught you! Terminating connection due to wrong digital signature...")
        s.close()  # Close the socket
        sys.exit()  # Exit the script
    else:
        print("Elgamal verification accepted")

    ka=symmetricKey(Xa,Yb,q)
    print("Alice's symmetric DH key: ",ka)
    key=generate_key_from_password(ka,ka)
    print("key AES Encryption received : ",key)
    threading.Thread(target=send_msg, args=(s,key)).start()
    threading.Thread(target=receive_msg, args=(s,key)).start()

if __name__ == "__main__":
    # Start the client
    Alice()
