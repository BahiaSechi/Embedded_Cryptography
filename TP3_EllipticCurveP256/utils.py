# -*- coding: utf-8 -*-
# PRUNIER Bastien
# SECHI Bahia

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
