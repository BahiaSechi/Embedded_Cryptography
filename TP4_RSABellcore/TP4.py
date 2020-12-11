# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Util import number
import math

def generer_cle_RSA(n):
    return


def generer_cle_RSA_CRT(N, e, p, q, d):
    dp = d % (p-1)
    dq = d % (q-1)
    ip = number.inverse(p, q) % q
    iq = number.inverse(q, p) % p
    return N, e, p, q, d, dp, dq, ip, iq


def signature_RSA_CRT(N, m, p, q, dp, dq):
    sp = m*math.sqrt(dp) % p
    sq = m*math.sqrt(dq) % q
    s = (number.inverse(q, p)*q*sp + number.inverse(p, q) * p * sq) % N
    return s


def signature_RSA_CRT_faute(m, sK):
    return


def RSA_CRT_Bellcore(m, sK, pK):
    return
