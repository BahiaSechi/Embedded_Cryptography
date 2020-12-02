# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

import math  

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def verifie_point(A,B,p,P):
    res = math.sqrt(math.pow(P.x, A) + P.x + B)
    return res == P.y


def addition_points(A, B, p, P, Q):
    if P == 0:
        return Q
    if Q == 0:
        return P
    if P != Q:
        return 0

def groupe_des_points(A,B,p):
    print("hey")

def ordre_point(A,B,p,P):
    print("hey")

def generateurs(A, B, p):
    print("hey")

def double_and_add(A,B,p,P,k):
    print("hey")

P = Point(2, 1)

print(verifie_point(3,2,3,P))