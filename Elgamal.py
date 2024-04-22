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
        
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def readFile():
    with open("publickeys.txt", "r") as file:
        keys = file.read().split()
        q = int(keys[0])
        alpha = int(keys[1])
    return q,alpha

def generate_private_key(q):
    Xa = random.randint(1, q-1)
    return Xa

def generate_public_key(q, alpha):
    Ya = pow(alpha, Xa,q)
    return Ya

def hash_message(M):
    return int(hashlib.sha1(M.encode()).hexdigest(), 16)

def sign(m, q, alpha,Xa):
    k = generate_k(q)
    s1 = pow(alpha, k, q)
    k_inv=mod_inverse(k,q-1);
    s2 = k_inv * (m-Xa*s1) % (q-1)
    return (s1, s2)

def verify(alpha,m,q,Ya,s1,s2):
    v1=pow(alpha,m,q)
    v2= (pow(Ya,s1)*pow(s1,s2)) %q
    return v1==v2


q,alpha=readFile();
Xa=generate_private_key(q);
Ya=generate_public_key(q,alpha);
M="hello"
m=hash_message(M)
m = m % q
# m=14
s1,s2=sign(m,q,alpha,Xa)
result=verify(alpha,m,q,Ya,s1,s2)
# print(" q ",q," alpha ",alpha," Xa ",Xa," Ya ",Ya," s1 ",s1," s2 ",s2," result ",v1,v2)
print("result ",result)

