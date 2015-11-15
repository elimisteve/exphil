#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.05.29

import decimal

number_types = (int, long, float, decimal.Decimal)

def in_platonic_heaven(obj, contained_types=number_types):
    # All numbers are in Platonic heaven
    if any([isinstance(obj, typ) for typ in contained_types]):
        return True

    # TODO(elimisteve): Add other constraints here
    return False


if __name__ == '__main__':
    print "According to function in_platonic_heaven:\n"
    for val in [-100, 0, 5, 'hello str', in_platonic_heaven]:
        print 'It is {} that {} is in Platonic heaven'.format(
            in_platonic_heaven(val), val)
