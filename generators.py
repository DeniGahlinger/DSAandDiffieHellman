# sympy est une bibliothèque python ayant des outils de generation et calculs de nombre premiers

from sympy import prime, sieve, ntheory
import random

#   la fonction getPime() utilise randprime de sympy. 
#   Cette fonction choisi au hasard une valeur entre deux bornes 
#   puis incrémente de façon optimisé jusqu'au prime suivant. 
#   Elle utilise donc la fonction isprime().

def getPrime(min, max):
    """Return prime between two numbers"""
    print("sieve max max max max : " + str(sieve._list[-1]))
    print(str(sieve._list))
    return ntheory.generate.randprime(min, max)

#   Pour trouver Q premier et Z tel que Q * Z = p-1, 
#   nous listons les facteurs premier de p-1. 
#   Ensuite, il suffit d'en prendre un au hasart pour Q,
#   et de diviser p-1 avec Q pour trouver Z. On retourne finalement Z et Q
    
def getQandZinDSA(p):
    """Return Q and Z with Q prime and Q * Z = p-1."""
    factors = ntheory.factorint(p-1)
    q = random.choice(list(factors))
    print(factors)
    print(q)
    z = (p - 1) / q
    return q, z
    
#   Cette fonction  retourne la première primitive root de p
    
def primitiveRoot(p):
    """return the first primitive root of p"""
    return ntheory.primitive_root(p)
