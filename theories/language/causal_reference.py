#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.20

import exphil

# TODO(elimisteve): Fill this in; not ready yet
class CausalTheoryOfReference(exphil.Theory):

    def __init__(self):

        self.exphil_attrs.update({
            'theory_type': ['reference', 'names'],
        })


    def refers_to(ref):
        '''
        What does `ref` refer to?
        '''
        if ref is None:
            return None

        if isinstance(ref, dict):
            raise NotImplementedError("dicts can't refer... for now at least")


    # def refers(ref):
    #     return self.refers_to(ref) != None


causal_theory = CausalTheoryOfReference()

print causal_theory.__dict__
print
print
