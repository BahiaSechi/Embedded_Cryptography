# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Util import number
from Crypto.Hash import SHA256
import math
import random
import utils

# P256 Elliptic Curve defined in FIPS 186-4
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
A = -3
B = int('5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b', 16)
Gx = int('6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296', 16)
Gy = int('4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5', 16)
G = utils.Point(Gx, Gy, 1)


def test_hasse(n, p):
    print(p)
    borneInf = p + 1 - math.sqrt(p)
    print(borneInf)
    borneSup = p + 1 + math.sqrt(p)
    print(borneSup)
    print(n)
    return borneInf <= n <= borneSup


def ecdh(A, B, p, P):
    a = random.randint(1, n)
    b = random.randint(1, n)

    aP = utils.double_and_add(A, B, p, P, a)
    bP = utils.double_and_add(A, B, p, P, b)

    aBG = utils.double_and_add(A, B, p, bP, a)
    bAG = utils.double_and_add(A, B, p, aP, b)

    if aBG == bAG:
        x = SHA256.new()
        x.update(number.long_to_bytes((a * b * G.x)))
        x.hexdigest()
        return x.digest().hex()
    elif aBG != bAG:
        return False



def ecdsa(A, B, p, P, n, m, a):
    k = random.randint(1, n - 1)
    K = utils.Point(P.x, P.y, 1)
    K = utils.double_and_add(A, B, p, K, k)
    t = K.x
    s = (m + a * t) * number.inverse(k, n) % n
    return utils.Point(t, s, 1)


def ecdsa_verif(A, B, p, P, n, m, A1, sign):
    return


# BONUS
def attack():
    return


# TESTS :
# Théorème de Hasse
print("La courbe respecte le théorème de Hasse : {}".format(test_hasse(n, p)))
# On peut voir que l'affichage dans le terminale ne permet pas la comparaison, comme les bornes sont arrondies, on ne peut pas faire la comparaison.

# ECDH
print("\nECDH")
print(ecdh(-3, B, p, utils.Point(2, 1, 1)))

# Fonction de chiffrement ECDSA :
print("\nECDSA")
print(ecdsa(A, B, p, G, n, "Je suis le message", 1))
