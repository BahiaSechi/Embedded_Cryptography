# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

from Crypto.Util import number
from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long
from decimal import Decimal
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

    pk = []
    pk.append(N)
    sk = []
    sk.append(p)
    sk.append(q)

    phiN = (p-1)*(q-1)
    e = 2
    while math.gcd(e, phiN) != 1 :
        e = random.randint(50000,1000000000000)
        
    d = number.inverse(e, phiN)

    pk.append(e)
    sk.append(d)

    return pk, sk

def generer_cle_RSA_CRT(pk, sk):
    p = sk[0]
    q = sk[1]
    d = sk[2]

    dp = d % (p-1)
    dq = d % (q-1)
    ip = number.inverse(p, q) % q
    iq = number.inverse(q, p) % p

    sk.append(dp)
    sk.append(dq)
    sk.append(ip)
    sk.append(iq)

    return sk


def signature_RSA_CRT(N, m, p, q, dp, dq):
    b = m.encode('utf-8')
    hash = SHA256.new()
    hash.update(b)
    encodedM = bytes_to_long(hash.digest())

    if encodedM >= N :
        return False

    sp = encodedM*math.sqrt(dp) % p
    sq = encodedM*math.sqrt(dq) % q
    s = (number.inverse(q, p)*q*sp + number.inverse(p, q) * p * sq) % N
    return s


def signature_RSA_CRT_faute(N, m, p, q, dp, dq):
    b = m.encode('utf-8')
    hash = SHA256.new()
    hash.update(b)
    encodedM = bytes_to_long(hash.digest())

    if encodedM >= N :
        return False
        
    sp = encodedM*math.sqrt(dp) % p
    sq = encodedM*math.sqrt(dq) % q + 1 # La "faute"
    s = (number.inverse(q, p)*q*sp + number.inverse(p, q) * p * sq) % N
    return s


def RSA_CRT_Bellcore(m):
    pk, sk = generer_cle_RSA(n)
    sk = generer_cle_RSA_CRT(pk, sk)

    sOk = signature_RSA_CRT(pk[0], m, sk[0], sk[1], sk[3], sk[4])
    sFaute = signature_RSA_CRT_faute(pk[0], m, sk[0], sk[1], sk[3], sk[4])

    print(sOk)
    print(sFaute)
    
    return

RSA_CRT_Bellcore("Je suis le message")