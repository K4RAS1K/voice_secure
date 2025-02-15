import random

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def generateKeys():
    p, q = generate_prime()
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0   
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break
    d = mod_inverse(e, phi)

    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(m, e, n):
    return power(m, e, n)

def decrypt(c, d, n):
    return power(c, d, n)
    
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
def generate_prime():
    p = 4
    q = 4
    while (not (is_prime(q) & is_prime(p))):
        p = random.randint(1000, 9999)
        q = random.randint(1000, 9999)
    return p, q

if __name__ == "__main__":
    e, d, n = generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    message = "Hi broooo"
    print(f"Original Message: {message}")

    hex_list = [ord(x) for x in message]

    C = [] 

    for i, mess in enumerate(hex_list):
        encrypted_message = encrypt(mess, e, n) 
        C.append(encrypted_message)  
        print(f"Encrypted Message {i}: {encrypted_message}") 

    for i, encrypted_message in enumerate(C):
        decrypted = decrypt(encrypted_message, d, n)
        print(f"Decrypted Message {i}: {chr(decrypted)}") 