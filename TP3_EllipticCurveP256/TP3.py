# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Hash import SHA256
from Crypto.Util import number
import math
import random
import utils

# P256 Elliptic Curve defined in FIPS 186-4
p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
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


def ecdh():
    a = random.randint(1, n)
    b = random.randint(1, n)
    if utils.Point(a * G.x, a * G.y, a * G.z) != utils.Point(b * G.x, b * G.y, b * G.z):
        return False
    elif utils.Point(a * G.x, a * G.y, a * G.z) == utils.Point(b * G.x, b * G.y, b * G.z):
        x = SHA256.new()
        x.update(number.long_to_bytes((a * G.x)))
        x.hexdigest()
        return x.digest().hex()


def ecdsa(A, B, p, P, n, m, a):
    return


def ecdsa_verif(A, B, p, P, n, m, A1, sign):
    return


# BONUS
def attack():
    return


# TESTS :
# Théorème de Hasse
print("La courbe respecte le théorème de Hasse : {}".format(test_hasse(n, p)))
# on peut voire que l'affichage dans le terminale ne permet pas la comparaison, comme les bornes sont arrondi on ne peut pas faire la comparaison.

# ECDH
print("\nECDH")
print(ecdh())
