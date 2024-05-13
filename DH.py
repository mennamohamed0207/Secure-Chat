import random
    
    
def readFile():
    with open("publickeys.txt", "r") as file:
        keys = file.read().split()
        q = int(keys[0])
        pr = int(keys[1])
    return q,pr

def publicKey(x,pr,q):
    y=pow(pr,x)%q #alice public key
    return y

def symmetricKey(x,y,q):
    k=pow(y,x)%q #symmetric private key
    return k
def readX(q):
    x = random.randint(1, q-1)
    return x
    
#main to test DH algorithm individually
# ya=publicKey(4,pr,q)
# yb=publicKey(3,pr,q)
# ka=symmetricKey(4,yb,q)
# kb=symmetricKey(3,ya,q)
# print("Ka: %s"%ka)
# print("Kb: %s"%kb)
    
    

