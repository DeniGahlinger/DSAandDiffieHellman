#   Implémentation de DSA avec créations des clés, signature de messages et
#   vérification de celui-ci

import random
from generators import getPrime, getQandZinDSA
from functions import fastModularExp, extendedEuclide

def generateKeys():
    """Generate keys for DSA"""
    # La generation de nombre premiers n'est fiable qu'avec des nombres plus
    # petits que 2^64 à cause de la fonction isprime(). Cette fonction, d'après
    # la documentation assure un nombre premier jusqu'à 2^64 puis n'en fait plus
    # qu'assumer leurs primalités pour des nombres plus gros.
    p = getPrime(18446744073708551616,18446744073709551616)
    q, z = getQandZinDSA(p)

    # On recherche h tel que h^z mod p != 1
    h = random.randint(0, p)
    while fastModularExp(h, z, p) == 1:
        h = random.randint(0, p)

    g = fastModularExp(h, z, p)
    x = random.randint(0, q)
    y = fastModularExp(g, x, p)

    print("\nPublic key : \n")

    print("p : " + str(p))
    print("q : " + str(q))
    print("g : " + str(g))
    print("y : " + str(y))

    print("\nPrivate key : \n")

    print("x : " + str(x))
    print("z : " + str(z))
    print("h : " + str(h))

    return (p, q, g, x, y)

def signMessage(M, p, q, g, x):
    """Sign message with DSA"""
    k = random.randint(2,q)
    uK = extendedEuclide(k, q) % q
    print("uK : " + str(uK))
    r = fastModularExp(g, k, p) % q
    print("r : " + str(r))
    s = (M + x * r) * uK % q
    print("s : " + str(s))
    return (r, s)

def verification(M, p, q, g, y, r, s):
    """Verify DSA signature"""
    w = extendedEuclide(s, q) % q
    print("w : " + str(w))
    u1 = (M * w) % q
    print("u1 : " + str(u1))
    u2 = (r * w) % q
    print("u2 : " + str(u2))
    v = ((fastModularExp(y, u2, p)*fastModularExp(g, u1, p)) % p) % q
    print("v : " + str(v))

    if(v == r):
        return True
    return False

if __name__ == '__main__':
    print("DSA starting...")
    p, q, g, x, y = generateKeys()
    M = 12345
    r, s = signMessage(M, p, q, g, x)
    isValid = verification(M, p, q, g, y, r, s)
    print("Does message have a valid signature? " + str(isValid))
