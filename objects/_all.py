#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.07.11

import inspect

import exphil.objects

## Objects

# All instances of exphil.Object in exphil.objects
all_objects = tuple(
    obj for name, obj in inspect.getmembers(exphil.objects, lambda o: isinstance(o, exphil.Object))
)


## Theories

# All instances of exphil.Theory in exphil.theories
all_theories = tuple(
    theory for name, theory in inspect.getmembers(exphil.theories, lambda th: isinstance(th, exphil.Theory))
)
