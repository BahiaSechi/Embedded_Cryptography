# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

import time

import Crypto
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Util import number
from Crypto.Random import get_random_bytes

temps0 = time.perf_counter()

# Question 1

print("Question 1")

m = SHA256.new()

n = 0

while not m.hexdigest().endswith("4c4f4c"):
    m.update(b"bahia")
    n += 1

print("n = " + str(n) + " \nhexdigest = " + m.hexdigest())

temps1 = time.perf_counter()
print('Question 1 time :', temps1 - temps0, 'seconds')

e = SHA256.new(n*b"bahia")
print("Verification:" + str(e.digest()))

# Il y avait 2^8^3 resultats possibles.

# Question 2

print("\nQuestion 2")

#  Une clé est constitué de 128 bits si on considère qu'une seule clé peut donner les caractères
#  ILOVEYOU au début du message chiffré alors on a 1 chance sur 2^128 d'avoir la bonne clé.
#  Il existe environ 3.4*10^38 clés possible, ce qui serait beaucoup trop long à chercher.

key = Crypto.Random.get_random_bytes(16)
chiffrement = AES.new(key, AES.MODE_ECB)
m_chiffre = chiffrement.encrypt(b"message_128nbits")

while not m_chiffre.hex().endswith("4c4f4c"):
    key = number.bytes_to_long(key)
    key += 1
    key = number.long_to_bytes(key)
    chiffrement = AES.new(key, AES.MODE_ECB)
    m_chiffre = chiffrement.encrypt(b"message_128nbits")

print("message" + str(m_chiffre))
print("key for bob = " + str(key.hex()))
print("message descrypt = " + chiffrement.decrypt(m_chiffre).decode("utf8"))

# Taille de l'espace des clés :
#  ILOVEYOU est constitué de 8 lettres, LOL est constitué de 3 lettres.
#  Les bits variables sont plus nombreux dans les clés pour finir un
#  message par LOL. Il peut apparaître dans beaucoup de combinaisons de ces bits variables
#  car il "prend moins de place" que ILOVEYOU
#  Place pour les autres bits dans LOL : (128bits de clé - 3 (caractères) * 8 bits)
#  dans ILOVEYOU : 128 - 64

temps2 = time.perf_counter()
print('Question 2 time :', temps2 - temps1, 'seconds')
