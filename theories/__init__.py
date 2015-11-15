import exphil

from exphil.theories.math import platonism
from exphil.theories.language import descriptivism

def _theories_in_module(module):
    return exphil.instances_in_module(exphil.Theory, module)

all = tuple(
    _theories_in_module(platonism) + _theories_in_module(descriptivism)
)
