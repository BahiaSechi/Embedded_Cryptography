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
        return "[{},{},{}]".format(self.x,self.y,self.z)
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.z == other.z


def verifie_point(A, B, p, P):
    res = (math.pow(P.x, 3) + A * P.x + B)
    #print(res, math.pow(P.y, 2))
    return (res%p == (math.pow(P.y, 2)%p) or (P.z == 0))


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
            lamb = (Q.y - P.y) * number.inverse((Q.x - P.x), p)
            X = lamb ** 2 - P.x - Q.x
            Y = lamb * (P.x - X) - P.y
            return Point(X, Y, 1).__dict__
    elif P == Q:
        if P.y == 0:
            return point_infini.__dict__
        elif P.y != 0:
            lamb = (3 * P.x ** 2 + A) * number.inverse((2 * P.y), p)
            X = lamb ** 2 - 2 * P.x
            Y = lamb * (P.x - X) - P.y
            return Point(X, Y, 1).__dict__

def groupe_des_points(A,B,p):
    points = []
    points.append(Point(0,0,0))
    for x in range(p):
        for y in range(p):
            P = Point(x,y,1)
            appartient = verifie_point(A, B, p, P)
            if appartient : points.append(P)
    print("Pour X^3 + {}X + {} de groupe Z{} il y a {} element(s)".format(A, B, p, len(points)))
    


def ordre_point(A,B,p,P):
    print("hey")


def generateurs(A, B, p):
    print("hey")


def double_and_add(A, B, p, P, k):
    print("hey")



# Verification première fonction :
print("\nFonction verifier_point :")
P = Point(0,0,0)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))
P = Point(2,1,1)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))
P = Point(2,2,1)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))

print("\nFonction addition_points :")
A = 3
B = 2
p = 5

P1 = Point(1, 4, 1)
Q1 = Point(1, 4, 1)
point_infini = Point(0, 0, 0)

print(addition_points(A, B, p, P1, Q1))

print("\nFonction groupe_des_points :")
groupe_des_points(3,2,5)
groupe_des_points(1,2,11)


