from rsa import RSA

if __name__ == "__main__":
    my_rsa = RSA()
    e, d, n = my_rsa.generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    message = "Hi broooo"
    print(f"Original Message: {message}")

    hex_list = [ord(x) for x in message]
    print(hex_list)
    C = my_rsa.encrypt(hex_list, e, n) 
    print(C)
    D = my_rsa.decrypt(C, d, n) 
    print(D) 