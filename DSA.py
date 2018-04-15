import random
import math

def extendedEuclide(x,q):
    s = 0
    old_s = 1
    
    t = 1
    old_t = 0
    
    r = q
    old_r = x
    
    while r != 0:
        quotien = old_r//r
        old_r, r = r, old_r - quotien * r
        old_s, s = s, old_s - quotien * s
        old_t, t = t, old_t - quotien * t
    return old_s
    

def calculateQandZ(p):
    #TODO
    return (101,78)

def fastModularExp(a,e,n):
    """Fast and nonnbijevwnk"""
    
    c=1
    a = a % n
    
    while(e > 0):
        if((e%2) == 1):
            c = (c * a) % n
        e = math.floor(e/2)
        a = (a * a) % n
    
    return c

def primeNumberGenerator(min,max):
    #TODO
    return 7879
    
def generateKeys():
    p = primeNumberGenerator(100,10000)
    q, z = calculateQandZ(p)
    h = random.randint(0,p)
    while fastModularExp(h,z,p) == 1:
        h = random.randint(0,p)
    g = fastModularExp(h,z,p)
    x = random.randint(0,q)
    y = fastModularExp(g,x,p)
    
    print("p : " + str(p))
    print("q : " + str(q))
    print("z : " + str(z))
    print("h : " + str(h))
    print("g : " + str(g))
    print("x : " + str(x))
    print("y : " + str(y))
    return (p,q,g,x,y)
    
def signMessage(M,p,q,g,x):
    k = random.randint(2,q)
    uK = extendedEuclide(k, q) % q
    print("uK : " + str(uK))
    r = fastModularExp(g,k,p) % q
    print("r : " + str(r))
    s = (M + x * r) * uK % q
    print("s : " + str(s))
    return (r,s)
    
def verification(M,p,q,g,y,r,s):
    w = extendedEuclide(s, q) % q
    print("w : " + str(w))
    u1 = (M * w) % q
    print("u1 : " + str(u1))
    u2 = (r * w) % q
    print("u2 : " + str(u2))
    v = ((fastModularExp(y,u2,p)*fastModularExp(g,u1,p)) % p) % q
    print("v : " + str(v))
    
    if(v == r):
        return True
    return False
    
if __name__ == '__main__': 
    print("DSA starting...")
    p,q,g,x,y = generateKeys()
    M = 12345
    r,s = signMessage(M,p,q,g,x)
    isValid = verification(M,p,q,g,y,r,s)
    print("has message a valid signature : " + str(isValid))
    
    
    

