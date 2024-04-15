# def primeChecker(q):
#     if q < 1:
#         return -1
#     elif q > 1:
#         if q == 2:
#             return 1
#         for i in range(2, q):
#             if q % i == 0:
#                 return -1
#             return 1
 
 
# def prChecker(pr, q):
#     for i in range(1, q):
#         if (pow(pr,i)%q==1 and i!=q-1):
#             return -1
#     return 1


# while 1:
#     q = int(input(f"enter prime number  : "))
#     if primeChecker(q) == -1:
#         print(f"not a prime number, try again")
#         continue
#     break

# while 1:
#     pr = int(input(f"enter the primative root of {q}  : "))
#     if prChecker(pr, q) == -1:
#         print(f"not a primative root, try again")
#         continue
#     break


with open("publickeys.txt", "r") as file:
    keys = file.read().split()
    q = int(keys[0])
    pr = int(keys[1])

def publicKey(x,pr,q):
    y=pow(pr,x)%q #alic public key
    return y

def symmetricKey(x,y,q):
    k=pow(y,x)%q #symmetric private key
    return k

ya=publicKey(4,pr,q)
yb=publicKey(3,pr,q)
ka=symmetricKey(4,yb,q)
kb=symmetricKey(3,ya,q)
print("Ka: %s"%ka)
print("Kb: %s"%kb)
    
    

