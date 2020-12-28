# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Util import number
import math

import random
#p ; q premier
#N=p*q
#e entier premier 
#φ(N) = (p−1)(q−1)
#d = e^(-1) modulo φ(N)
#Clé privée (p,q,d) 


#Cle publique (N,e)
#pK=(N,e)
#sK=(p,q,d)
#p et q entier premier de n bits 
n=1024

def generer_cle_RSA(n):
    # Generation of two 1024bits prime number and N processing
    p = number.getStrongPrime(n)
    q = number.getStrongPrime(n)
    N = p*q

    phiN = (p-1)*(q-1)
    e=2
    while math.gcd() != 1 :
        e=random.randint(50000,1000000000000)

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
