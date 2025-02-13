import random
import math

class RSA():
    def __init__(self):
        e,d,N = self.__RSA_keys()
        self.open_keys = [e,N] 
        self.close_keys = [d,N] 
    
    def secure_message():
         

    def __RSA_keys(self):
        p = random.randint(10000, 99999)
        q = random.randint(10000, 99999)
        N = p * q
        fi = (p - 1) * (q - 1)
        d = random.randint(1, fi)
        arg1,arg2 = self.__Euclid_alg(d, fi)
        e = int(fi - math.fabs(min(arg1, arg2)))
        print((e * d) % fi)
        if((e * d) % fi != 1):
                print("ERROR!!!")
                e,d,N = self.__RSA_keys()
        return e, d, N

    def __Euclid_alg(self,a, b):
        x1 = 0
        x2 = 1
        y1 = 1
        y2 = 0
        while(b>0):
            q = a // b
            r = a - q * b
            x = x2 - q * x1
            y = y2 - q * y1
            a = b 
            b = r 
            x2 = x1 
            x1 = x 
            y2 = y1 
            y1 = y 
        return x2, y2


if __name__ == "__main__":
    my_rsa = RSA()
    print(f"\nОткрытый ключ:{my_rsa.open_keys}\n"+
        f"Закрытый ключ:{my_rsa.close_keys}")