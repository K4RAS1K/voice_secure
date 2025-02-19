from rsa import RSA
from reed_solomon_code import reed_solomon_example

if __name__ == "__main__":
    my_rsa = RSA()
    public_key, private_key = my_rsa.generateKeys()

    print(f"\nPublic Key (e, n): ({public_key})")
    print(f"Private Key (d, n): ({private_key})")

    message = "Hello, World!!!"
    print(f"Original Message: {message}")
    hex_list = [ord(x) for x in message]
    print(hex_list)
    reed_solomon_example(hex_list)
    C = my_rsa.encrypt(hex_list, public_key) 
    print(C)
    D = my_rsa.decrypt(C, private_key) 
    print(D) 
    result_string = ''.join([chr(hex_value) for hex_value in D])
    print(f"Result Message: {result_string}") 