# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

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
