import time

import Crypto
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

temps0 = time.perf_counter()

# Question 1

print("Question 1")

m = SHA256.new()

n = 0

while not m.hexdigest().endswith("4c4f4c"):
    m.update(b"bahia")
    n += 1
    print(m.hexdigest())

print("n = " + str(n) + " \nhexdigest = " + m.hexdigest())

temps1 = time.perf_counter()
print('Question 1 time :', temps1-temps0, 'seconds')

e = SHA256.new(n*b"bahia")
print("Verification:" + str(e.digest()))

# Question 2

print("Question 2")

chiffrement = AES.new(b"Sixteen byte key", AES.MODE_ECB)
m_chiffre = chiffrement.encrypt(b"message_128nbits")
print(chiffrement.decrypt(m_chiffre).decode("utf_8"))

rand_nb = Crypto.Random.get_random_bytes(128)
print(rand_nb)

temps2 = time.perf_counter()
print('Question 2 time :', temps2-temps1, 'seconds')
