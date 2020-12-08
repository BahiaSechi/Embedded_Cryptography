# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

import math
from Crypto.Util import number


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return "[{},{},{}]".format(self.x, self.y, self.z)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z


def verifie_point(A, B, p, P):
    res = (math.pow(P.x, 3) + A * P.x + B)
    # print(res, math.pow(P.y, 2))
    return res % p == (math.pow(P.y, 2) % p) or (P.z == 0)


def addition_points(A, B, p, P, Q):
    point_infini = Point(0, 0, 0)

    if P.x == 0 and P.y == 0:
        return Q
    if Q.x == 0 and Q.y == 0:
        return P

    if P != Q:
        if P.x == Q.x:
            return point_infini
        elif P.x != Q.x:
            lamb = ((Q.y - P.y) * number.inverse((Q.x - P.x), p)) % p
            X = ((lamb ** 2) - P.x - Q.x) % p
            Y = (lamb * (P.x - X) - P.y) % p
            return Point(X, Y, 1)
    elif P == Q:
        if P.y == 0:
            return point_infini
        elif P.y != 0:
            lamb = ((3 * (P.x ** 2) + A) * number.inverse((2 * P.y), p)) % p
            X = ((lamb ** 2) - (2 * P.x)) % p
            Y = ((lamb * (P.x - X)) - P.y) % p
            return Point(X, Y, 1)


def groupe_des_points(A, B, p):
    points = [Point(0, 0, 0)]
    for x in range(p):
        for y in range(p):
            P = Point(x, y, 1)
            appartient = verifie_point(A, B, p, P)
            if appartient: points.append(P)
    print("Pour X^3 + {}X + {} de groupe Z{} il y a {} element(s)".format(A, B, p, len(points)))
    return points


def ordre_point(A, B, p, P):
    point_infini = Point(0, 0, 0)
    X = Point(P.x, P.y, P.z)
    c = 1
    while X != point_infini:
        X = addition_points(A, B, p, X, P)
        c = c + 1
    return c


def generateurs(A, B, p):
    groupe = groupe_des_points(A, B, p)
    generateurs = []
    for P in groupe:  # pas de generateur => groupe pas cyclique
        if ordre_point(A, B, p, P) == p:
            generateurs.append(P)
        # print("{} => {}".format(P.toString(), ordre_point(A, B, p, P)))
    return generateurs


def double_and_add(A, B, p, P, k):
    Q = Point(0, 0, 0)
    n = int(math.log(k, 2)) + 1
    for i in range(n, -1, -1):
        Q = addition_points(A, B, p, Q, Q)
        if (k >> i) & 1 == 1:
            Q = addition_points(A, B, p, Q, P)
    return Q


A = 3
B = 2
p = 5

# Verification première fonction :
print("\nFonction verifier_point :")
P = Point(0, 0, 0)
print("{} => {}".format(P.toString(), verifie_point(A, B, p, P)))
P = Point(2, 1, 1)
print("{} => {}".format(P.toString(), verifie_point(A, B, p, P)))
P = Point(2, 2, 1)
print("{} => {}".format(P.toString(), verifie_point(A, B, p, P)))

print("\nFonction addition_points :")

P = Point(2, 1, 1)
Q = Point(2, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

P = Point(2, 1, 1)
Q = Point(2, 1, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

P = Point(2, 1, 1)
Q = Point(0, 0, 0)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

P = Point(2, 1, 1)
Q = Point(1, 1, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

P = Point(2, 1, 1)
Q = Point(1, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

P = Point(1, 4, 1)
Q = Point(1, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q).toString()))

A2 = 1
B2 = 2
p2 = 11

print("\nFonction groupe_des_points :")
groupe_des_points(A, B, p)
groupe_des_points(A2, B2, p2)

print("\nFonction generateur :")
A2 = 1
B2 = 2 
p2 = 11
e1 = generateurs(A, B, p)
e2 = generateurs(A2, B2, p2)
for g in range(len(e1)):
    print("Generateur de E1 : {}".format(e1[g].toString()))
for g in range(len(e2)):
    print("Generateur de E2 : {}".format(e2[g].toString()))


print("\n")

print("\nFonction Double and Add :")
P = Point(2,4,1)
for k in range (5,11):
    print(double_and_add(A,B,p,P,k).toString())
