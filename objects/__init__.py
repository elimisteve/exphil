import exphil

import _person
import people
import snow

from _person import *

def _exphil_objects_in_module(module):
    return exphil.instances_in_module(exphil.Object, module)

all = tuple(
    _exphil_objects_in_module(_person) +
    _exphil_objects_in_module(people) +
    _exphil_objects_in_module(snow)
)
