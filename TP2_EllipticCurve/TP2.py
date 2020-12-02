# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

import math
import utils


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def verifie_point(A, B, p, P):
    res = (math.pow(P.x, 3) + A * P.x + B) % p
    # print(res, math.pow(P.y, 2))
    return (res == P.y) or (P.z == 0)


def addition_points(A, B, p, P, Q):
    point_infini = Point(0, 0, 0)
    if P.x == 0 and P.y == 0:
        return Q.__dict__
    if Q.x == 0 and Q.y == 0:
        return P.__dict__

    if P != Q:
        if P.x == Q.x:
            return point_infini.__dict__
        elif P.x != Q.x:
            lamb = (Q.y - P.y) * utils.modular_inverse((Q.x - P.x), p)
            X = lamb ** 2 - P.x - Q.x
            Y = lamb * (P.x - X) - P.y
            return Point(X, Y, 1).__dict__
    elif P == Q:
        if P.y == 0:
            return point_infini.__dict__
        elif P.y != 0:
            lamb = (3 * P.x ** 2 + A) * utils.modular_inverse((2 * P.y), p)
            X = lamb ** 2 - 2 * P.x
            Y = lamb * (P.x - X) - P.y
            return Point(X, Y, 1).__dict__


def groupe_des_points(A, B, p):
    print("hey")


def ordre_point(A, B, p, P):
    print("hey")


def generateurs(A, B, p):
    print("hey")


def double_and_add(A, B, p, P, k):
    print("hey")


P = Point(0, 0, 0)

# print(verifie_point(3, 2, 5, P))

A = 3
B = 2
p = 5

P1 = Point(2,1,1)
Q1 = Point(2,4,1)
point_infini = Point(0,0,0)

print(addition_points(A,B,p,P1,Q1))


