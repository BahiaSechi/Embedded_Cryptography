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



P = Point(2, 1)

print(verifie_point(3,2,3,P))