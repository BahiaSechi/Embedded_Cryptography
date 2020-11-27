import time
from Crypto.Hash import SHA256

temps0 = time.perf_counter()

# Exercice 1

m = SHA256.new()
m.update(b"debut")
m.update(b"suite")
print(m.hexdigest())

n = SHA256.new(data=b"debutsuite")
print(n.hexdigest())

temps1 = time.perf_counter()
print('Temps exercice 1 :', temps1-temps0, 'secondes')

# Exercice 2

# INSTRUCTIONS

# temps2 = time.perf_counter()
# print ('Temps2 :', temps2-temps1, 'secondes')