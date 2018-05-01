#   sympy est une bibliothèque Python ayant des outils de génération et de calculs
#   de nombres premiers. Les détails des fonctions utilisées peuvent être trouvées
#   sur la documentation officielle http://docs.sympy.org/latest/index.html

from sympy import prime, sieve, ntheory
import random

#   La fonction getPime() utilise la fonction randprime de sympy.
#   Cette fonction choisi au hasard une valeur entre deux bornes
#   puis incrémente de façon optimisé cette valeur jusqu'à trouver
#   le prime suivant le plus proche.
#   La fonction randprime utilise donc la fonction isprime() de sympy.

def getPrime(min, max):
    """Return random prime between two numbers"""
    return ntheory.generate.randprime(min, max)

#   Pour trouver Q premier et Z tel que Q * Z = p-1,
#   nous listons les facteurs premiers de p-1 en utilisant la fonctions
#   factorint de sympy qui nous retourne sous forme de dictionnaire, les
#   facteurs premiers et leur nombre d'occurrence.
#   Ensuite, il suffit d'en prendre un au hasart pour Q,
#   et de diviser p-1 avec Q pour trouver Z. On retourne finalement Z et Q.

def getQandZinDSA(p):
    """Return Q and Z with Q prime and Q * Z = p-1"""
    factors = ntheory.factorint(p-1)
    q = random.choice(list(factors))
    z = (p - 1) / q
    return q, z

#   Cette fonction retourne la première primitive root de p en utilisant
#   la fonction fournie par sympy appelée primitive_root().

def getFirstPrimitiveRoot(p):
    """Return the first primitive root of p"""
    return ntheory.primitive_root(p)
