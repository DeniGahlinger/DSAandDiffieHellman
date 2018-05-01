#   Implémentation Diffie-Hellman et échanges de clés

import random
from generators import getPrime, getFirstPrimitiveRoot
from functions import fastModularExp

# Global parameters
p = 0 # a prime integer
g = 0 # a primitive root mod p

def generateKeys(p, g):
    """Generate new random Diffie-Helmann Keys from prime p and primitive root g"""
    k = random.randint(0, p) # Secret key
    K = fastModularExp(g, k, p) # Public key
    return (k, K)

def encrypt(M, S, p):
    """Encrypt message M with shared key S and prime p"""
    return fastModularExp(M*S, 1, p)

def decrypt(C, K, k, p):
    """Decrypt cyphermessage C with private key k and sender public key K and prime p"""
    return fastModularExp(C * fastModularExp(K, p-1-k, p), 1, p)

if __name__ == '__main__':
    print("Diffie-Helmann starting...")
    p = getPrime(100000000000,55000000000000)
    g = getFirstPrimitiveRoot(p)
    a, A = generateKeys(p, g)
    b, B = generateKeys(p, g)
    S = fastModularExp(A, b, p) # Shared key
    M = 78 # Message
    C = encrypt(M,S,p)
    M2 = decrypt(C,B,a,p)

    print("\n=== Key Generation ===\n")

    print("\nGlobal keys : ")
    print("  p : " + str(p))
    print("  g : " + str(g))

    print("\nPublic keys : ")
    print("  for Alice A : " + str(A))
    print("  for Bob B : " + str(B))

    print("\nPrivate keys : ")
    print("  for Alice a : " + str(a))
    print("  for Bob b : " + str(b))

    print("\nShared key : ")
    print("  S : " + str(S))

    print("\n=== Message Exchange ===\n")

    print("\nMessage : ")
    print("  M : " + str(M))

    print("\nCypher message : ")
    print("  C : " + str(C))

    print("\nDecrypt message : ")
    print("  M : " + str(M2))
