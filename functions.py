#   Rassemblement de fonctions utiles crées en classe de cryptographie, d'après
#   le cours de M. Marina

import math

#   Implémentation faite en exercice du cours de cryptographie de l'algorithme
#   d'Euclide étendu

def extendedEuclide(x, q):
    """Extended Euclide algorithme"""
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

#   Implémentation rapide du calcul a^e mod n fait en exercice du cours de
#   cryptographie

def fastModularExp(a, e, n):
    """Return a^e mod n"""

    c = 1
    a = a % n

    while(e > 0):
        if((e % 2) == 1):
            c = (c * a) % n
        e = math.floor(e / 2)
        a = (a * a) % n

    return c
