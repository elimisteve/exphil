#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.20

import exphil
import exphil.objects

def by_dict(kwargs, all_objects=exphil.objects.all):
    objects = []

    for obj in all_objects:
        all_attrs_match = True
        for k in kwargs:
            try:
                val_found = exphil.get_attr(obj, k)[0]
            except KeyError:
                # obj doesn't have attr k; skip to next obj
                all_attrs_match = False
                break

            val_wanted = kwargs[k]
            if not (val_found == val_wanted or \
                    exphil.is_collection(val_found) and val_wanted in val_found):
                # obj doesn't match; skip to next obj
                all_attrs_match = False
                break

        if all_attrs_match:
            objects.append(obj)

    return objects


def by_func(predicate, all_objects=exphil.objects.all):
    objects = []

    for obj in all_objects:
        try:
            if predicate(obj) == True:
                objects.append(obj)
        except:  # TODO(elimisteve): Catch _all_ exceptions here?
            pass

    return objects


def by_id(obj_id, all_objects=exphil.objects.all):
    objs = [obj for obj in all_objects if id(obj) == obj_id]
    return objs
