#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.11.15

import itertools

def gen_all(theory):
    '''
    Each theory must be a list of strings or a dict[str, bool].

    Generates and returns all possible theories with the keys of the
    given theory (with corresponding values of True or False).
    '''
    if type(theory) is list:
        # List of properties -> dict[property, bool]
        theory = {prop: bool() for prop in theory}

    keys = theory.keys()
    combos = itertools.product(*[(False, True)]*len(keys))
    return [dict(zip(keys, c)) for c in combos]
