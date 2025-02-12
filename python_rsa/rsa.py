import random
import math

def RSA(p, q):
    N = p * q
    fi = (p - 1) * (q - 1)
    e = random.randint(1, fi)
    arg1,arg2 = Euclid_alg(fi,e)
    d = int(fi - math.fabs(min(arg1,arg2)))
    return e, d, N

def Euclid_alg(a, b):
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    while(b>0):
        q = int(a / b)
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
    p = int(input("\np: "))
    q = int(input("\nq: "))
    e, d, N = RSA(p,q)
    print(f"\nОткрытый ключ:{e},{N}\n"+
        f"Закрытый ключ:{d},{N}")