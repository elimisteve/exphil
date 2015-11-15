#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.09

import exphil
import exphil.objects.query

from exphil.objects.people import SantaClaus_ID, PresentKingOfFrance_ID, \
    Nietzsche_ID

class DirectReference(exphil.Theory):

    def __init__(self):
        self.exphil_attrs.update({
            'theory_type': ['reference', 'names'],
        })


    def refers_to(self, ref):
        '''
        Answers the question, "what does `ref` refer to (according to
        Direct Reference)?"
        '''
        if ref is None:
            return None

        # Make sure we have an ID
        #
        # TODO(elimisteve): Should/does Direct Reference say that we have
        # references to things themselves?  Using IDs as references
        # may be a mistake.
        if not isinstance(ref, int):
            raise ValueError("Reference '{}' must be an ID (int)", ref)

        objs = exphil.objects.query.by_id(ref)

        if len(objs) > 1:
            raise ValueError(
                "Reference is ambiguous; refers to {} objects: {}".format(
                    len(objs), objs
                )
            )

        if not objs:
            return None

        return list(objs)[0]


direct_reference = DirectReference()


if __name__ == '__main__':
    print "According to DirectReference:\n"

    nietzsche = Nietzsche_ID
    king_of_france = PresentKingOfFrance_ID
    santa = SantaClaus_ID

    for ref in [nietzsche, king_of_france, santa, None]:
        print "ID {}  refers to  {}\n".format(ref, direct_reference.refers_to(ref))
