import random

class RSA():
    def generateKeys(self):
        p, q = self.__generate_prime()
        
        n = p * q
        phi = (p - 1) * (q - 1)

        e = 0   
        for e in range(2, phi):
            if self.__gcd(e, phi) == 1:
                break
        d = self.__mod_inverse(e, phi)
        public_key = [e, n]
        private_key = [d, n]
        return public_key, private_key
        
    def encrypt(self, char_list, public_key):
        C = []
        for i, mess in enumerate(char_list):
            encrypted_message = self.__power(mess, public_key[0], public_key[1])
            C.append(encrypted_message)  
        return C

    def decrypt(self,char_list, private_key):
        C = []
        for i, mess in enumerate(char_list):
            decrypt_message = self.__power(mess,  private_key[0], private_key[1])
            C.append(decrypt_message)  
        return C

    def __power(self,base, expo, m):
        res = 1
        base = base % m
        while expo > 0:
            if expo & 1:
                res = (res * base) % m
            base = (base * base) % m
            expo = expo // 2
        return res

    def __mod_inverse(self, e, phi):
        for d in range(2, phi):
            if (e * d) % phi == 1:
                return d
        return -1

    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
        
    def __is_prime(self, a):
        if a % 2 == 0:
            return a == 2
        d = 3
        while d * d <= a and a % d != 0:
            d += 2
        return d * d > a

    def __generate_prime(self):
        p = 4
        q = 4
        while (not (self.__is_prime(q) & self.__is_prime(p))):
            p = random.randint(1000, 9999)
            q = random.randint(1000, 9999)
        return p, q