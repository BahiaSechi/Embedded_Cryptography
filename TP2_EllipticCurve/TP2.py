# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

import math  

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return "[{},{},{}]".format(self.x,self.y,self.z)

def verifie_point(A,B,p,P):
    res = (math.pow(P.x, 3) + A*P.x + B)%p
    #print(res, math.pow(P.y, 2))
    return (res == P.y) or (P.z == 0)


def addition_points(A, B, p, P, Q):
    if P == 0:
        return Q
    if Q == 0:
        return P
    if P != Q:
        return 0

def groupe_des_points(A,B,p):
    total = 0
    for x in range(p):
        for y in range(p):
            P = Point(x,y,1)
            appartient = verifie_point(A, B, p, P)
            if appartient : total += 1
            print("{} => {}".format(P.toString, appartient))
    print("Pour X^3 + {}X + {} de groupe Z{} il y a {} element(s)".format(A, B, p, total))
    


def ordre_point(A,B,p,P):
    print("hey")

def generateurs(A, B, p):
    print("hey")

def double_and_add(A,B,p,P,k):
    print("hey")



# Verification première fonction :
print("\nFonction verifier_point :")
P = Point(0,0,0)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))
P = Point(2,1,1)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))
P = Point(2,2,1)
print("{} => {}".format(P.toString(), verifie_point(3,2,5,P)))

print("\nFonction groupe_des_points :")
groupe_des_points(3,2,5)