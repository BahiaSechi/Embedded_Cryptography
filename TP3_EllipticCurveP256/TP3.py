# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Hash import SHA256
from Crypto.Util import number
import math

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
B = int('5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b', 16)
Gx = int('6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296', 16)
Gy = int('4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5', 16)


def test_hasse(n, p):
    borneInf = p + 1 - math.sqrt(p)
    borneSup = p + 1 + math.sqrt(p)
    return n >= borneInf and n <= borneSup


def ecdh(A, B, p, P):
    return


def ecdsa(A, B, p, P, n, m, a):
    return


def ecdsa_verif(A, B, p, P, n, m, A1, sign):
    return


# BONUS
def attack():
    return


# TESTS :
# Théoreme de hasse
