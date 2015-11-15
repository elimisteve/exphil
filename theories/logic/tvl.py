#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.07.14

import exphil

class KleeneTruthValue(exphil.Object):

    def __init__(self, num):
        if num not in [0, 0.5, 1]:
            raise ValueError("num must be 0, 0.5, or 1")

        self.value = num


    # TODO(elimisteve): GETHELP -- Is there a method to define what happens
    # when 'not self' is evaluated?
    def negate(self):
        # 0   -> 1    (same as classical logic)
        # 1   -> 0    (same as classical logic)
        # 0.5 -> 0.5  (new)
        self.value = 1 - self.value
        return self


    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '"' + self.__str__() + '"'


true    = KleeneTruthValue(1)
false   = KleeneTruthValue(0)
neither = KleeneTruthValue(0.5)
