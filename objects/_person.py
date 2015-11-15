#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.09

import exphil

class Person(dict, exphil.Object):

    def __init__(self, *args, **kwargs):
        if len(args) != 4:
            raise TypeError(
                "4 args required (first_name, middle_name, last_name, birthday)" + \
                    ", {} given".format(len(args))
            )

        self['first_name'] = args[0]
        self['middle_name'] = args[1]
        self['last_name'] = args[2]
        self['birthday'] = args[3]

        # Default
        self['fictional'] = False

        self.update(kwargs)

    @property
    def __dict__(self):
        return self


class FictionalPerson(Person):

    def __init__(self, *args, **kwargs):
        super(FictionalPerson, self).__init__(*args, **kwargs)
        self['fictional'] = True
