#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.17

import exphil
import exphil.objects.query

class Descriptivism(exphil.Theory):

    def __init__(self, must_match=1):
        # Preparing for 80% matching to be acceptable
        self.must_match = must_match

        self.exphil_attrs.update({
            'theory_type': ['reference', 'names'],
        })


    def refers_to(self, ref):
        '''
        Answers the question, "what does `ref` refer to (according to
        Descriptivism)?"

        TODO(elimisteve): Decide which `ref` types should be accepted.  (Just
        dicts? Strings? Some types should refer to themselves,
        perhaps.)
        '''
        if ref is None:
            return None

        # Make sure we have a dict, or something dict-like
        if not isinstance(ref, dict):
            ref = ref.__dict__

        # TODO(elimisteve): Implement these other versions of Descriptivism
        # where, e.g., merely _most_ of the descriptors must match, so
        # that it's possible to have false beliefs about someone and
        # still successfully refer.
        if self.must_match != 1:
            raise NotImplementedError(
                "Haven't yet implemented fancy queries to do partial matches")

        objs = exphil.objects.query.by_dict(ref)

        # TODO(elimisteve): Is this correct?
        if isinstance(objs, dict):
            return objs

        # Descriptivism demands that descriptions be definite; they
        # may not be ambiguous/refer to multiple things
        if len(objs) > 1:
            raise ValueError(
                "Reference is ambiguous; refers to {} objects: {}".format(
                    len(objs), objs
                )
            )

        if not objs:
            return None

        # Turns objs into list in case it's a set, so we can grab the
        # 0th element
        #
        # TODO(elimisteve): If objs is a dict, this returns a random key.
        # Allow dicts?
        return list(objs)[0]


    def refers(self, ref):
        return self.refers_to(ref) != None


descriptivism = Descriptivism()

if __name__ == '__main__':
    from exphil.objects import people

    nietzsche = {
        'last_name':   'Nietzsche',
        'author_of':   'Thus Spake Zarathustra',
        'philosopher': True,
        'mustache':    True,
    }

    entities = [people.SantaClaus, {'king': True}, {'first_name': 'Santa'},
                {'last_name': 'Kripke'}, descriptivism, nietzsche]

    print "According to Descriptivism:\n"
    for entity in entities:
        print "{}\n    refers to\n{}\n".format(entity, descriptivism.refers_to(entity))

    # d = {}
    # print d, "  refers to  ", descriptivism.refers_to(d)
