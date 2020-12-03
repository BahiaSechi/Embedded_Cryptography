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
        return Q.toString()
    if Q.x == 0 and Q.y == 0:
        return P.toString()

    if P != Q:
        if P.x == Q.x:
            return point_infini.toString()
        elif P.x != Q.x:
            lamb = ((Q.y - P.y) * number.inverse((Q.x - P.x), p)) % p
            X = ((lamb ** 2) - P.x - Q.x) % p
            Y = (lamb * (P.x - X) - P.y) % p
            return Point(X, Y, 1).toString()
    elif P == Q:
        if P.y == 0:
            return point_infini.toString()
        elif P.y != 0:
            lamb = ((3 * (P.x ** 2) + A) * number.inverse((2 * P.y), p)) % p
            X = ((lamb ** 2) - (2 * P.x)) % p
            Y = ((lamb * (P.x - X)) - P.y) % p
            return Point(X, Y, 1).toString()


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
    print("hey")


def generateurs(A, B, p):
    groupe = groupe_des_points(A, B, p)
    for P in groupe:
        ordre_point(A, B, p, P)



def double_and_add(A, B, p, P, k):
    print("hey")


# Verification première fonction :
print("\nFonction verifier_point :")
P = Point(0, 0, 0)
print("{} => {}".format(P.toString(), verifie_point(3, 2, 5, P)))
P = Point(2, 1, 1)
print("{} => {}".format(P.toString(), verifie_point(3, 2, 5, P)))
P = Point(2, 2, 1)
print("{} => {}".format(P.toString(), verifie_point(3, 2, 5, P)))

print("\nFonction addition_points :")

A = 3
B = 2
p = 5

P = Point(2, 1, 1)
Q = Point(2, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

P = Point(2, 1, 1)
Q = Point(2, 1, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

P = Point(2, 1, 1)
Q = Point(0, 0, 0)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

P = Point(2, 1, 1)
Q = Point(1, 1, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

P = Point(2, 1, 1)
Q = Point(1, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

P = Point(1, 4, 1)
Q = Point(1, 4, 1)
print("{} + {} = {}".format(P.toString(), Q.toString(), addition_points(A, B, p, P, Q)))

print("\nFonction groupe_des_points :")
groupe_des_points(3, 2, 5)
groupe_des_points(1, 2, 11)

print("\nFonction groupe_des_points :")
A1 = 3
B1 = 2
A2 = 1
B2 = 2 
p1 = 5
p2 = 11
generateurs(A1, B1, p1)
generateurs(A2, B2, p2)

print("\n")