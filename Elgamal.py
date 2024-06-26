import hashlib
import random
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)

def mod_inverse(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m
    
def generate_k(q):
    while True:
        k = random.randint(1, q-1)
        if gcd(k, q-1) == 1:
            return k 
    # return 5   
        
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def readFile_elgamal():
    with open("keys_elgamal.txt", "r") as file:
        keys = file.read().split()
        q = int(keys[0])
        alpha = int(keys[1])
    return q,alpha

def generate_private_key_elgamal(q):
    Xa2 = random.randint(1, q-1)
    return Xa2
    # return 16

def generate_public_key_elgamal(q, alpha,Xa2):
    Ya2 = pow(alpha, Xa2,q)
    return Ya2

def hash_message_elgamal(M):
    # print("in hashhh",M)
    return int(hashlib.sha1(M.encode()).hexdigest(),16)

def sign_elgamal(m, q, alpha,Xa2):
    k = generate_k(q)
    s1 = pow(alpha, k, q)
    k_inv=mod_inverse(k,q-1);
    s2 = (k_inv * (m-Xa2*s1)) % (q-1)
    return s1, s2

def verify_elgamal(alpha, m, q, Ya2, s1, s2):
    v1 = pow(alpha, m, q)
    v2 = (pow(Ya2, s1, q) * pow(s1, s2, q)) % q

    return v1== v2

#main to test el gamal algorithm individually
# q,alpha=readFile_elgamal() #global keys for elgamal
# Xa2=generate_private_key_elgamal(q) 
# Ya2=generate_public_key_elgamal(q,alpha,Xa2)
# M="hello"
# m=hash_message_elgamal(M)
# m = m % q
# # m=14
# s1,s2=sign_elgamal(m,q,alpha,Xa2)
# result=verify_elgamal(alpha,m,q,Ya2,s1,s2)
# # print(" q ",q," alpha ",alpha," Xa2 ",Xa2," Ya2 ",Ya2," s1 ",s1," s2 ",s2," result ",v1,v2)
# print("result ",result)

