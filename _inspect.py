#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.07.15

import inspect

def instances_in_module(cls, module):
    return [instance for name, instance in inspect.getmembers(module, lambda inst: isinstance(inst, cls))]

def vars_by_name_in_module(predicate, module):
    return [instance for name, instance in inspect.getmembers(module) if predicate(name)]
