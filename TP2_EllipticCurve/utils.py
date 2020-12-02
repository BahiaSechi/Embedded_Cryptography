def extended_euclid(aa, bb):
    a, b = abs(aa), abs(bb)
    u0, u1 = 1, 0
    v0, v1 = 0, 1
    while b != 0:
        q = int(a / b)
        a, b = b, a % b
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    u0 *= -1 if aa < 0 else 1
    v0 *= -1 if bb < 0 else 1
    return abs(a), u0, v0


def modular_inverse(a, n):
    pgcd, u, v = extended_euclid(a, n)
    n = abs(n)
    if pgcd == 1:
        return u % n
    return 0
