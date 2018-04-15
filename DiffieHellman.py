import random
import math

p = 0
g = 0

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

def getPrime():
    #TODO
    return 353
    
def getPrimitiveRoot():
    #TODO
    return 3
    
def generateKeys(p,g):
    k = random.randint(0,p)
    K = fastModularExp(g,k,p)
    return (k,K)
    
def calculateSharedKey(K,k,p):
    return fastModularExp(K,k,p)
    
def encrypt(M,S,p):
    return fastModularExp(M*S,1,p)
    
def decrypt(C,K,k,p):
    return fastModularExp(C * fastModularExp(K,p-1-k,p),1,p)
    
if __name__ == '__main__':   
    print("Diffie-Helmann starting...")
    p = getPrime()
    g = getPrimitiveRoot()
    a,A = generateKeys(p,g)
    b,B = generateKeys(p,g)
    S = calculateSharedKey(A,b,p)
    print("S : " + str(S))
    M = 19
    C = encrypt(M,S,p)
    print("C : " + str(C))
    M = decrypt(C,B,a,p)
    print("M : " + str(M))
    