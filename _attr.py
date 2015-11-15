#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.04.24


def get_attr(dict_or_obj, *attrs):
    ATTR_NOT_FOUND = KeyError("{} doesn't have attr(s) {}".format(dict_or_obj, attrs))

    if isinstance(dict_or_obj, dict):
        for attr in attrs:
            if attr in dict_or_obj:
                return dict_or_obj[attr], attr
        raise ATTR_NOT_FOUND

    for attr in attrs:
        if hasattr(dict_or_obj, attr):
            return getattr(dict_or_obj, attr), attr

    raise ATTR_NOT_FOUND


def has_attr(dict_or_obj, attr):
    if isinstance(dict_or_obj, dict):
        return attr in dict_or_obj

    # Assuming it's an object
    return hasattr(dict_or_obj, attr)


def has_method(obj, method_name):
    # If the attribute is callable, it's a method, otherwise it's a
    # property

    return hasattr(obj, method_name) and callable(getattr(obj, method_name))


def update_object(obj, kwargs):
    for k in kwargs:
        setattr(obj, k, kwargs[k])


collection_types = (list, tuple, set, frozenset)

def is_collection(coll):
    return any([ isinstance(coll, typ) for typ in collection_types ])


def Is(obj, attr_value):
    '''
    Meant to capture the following senses of 'is':

    - Snow is white, George W. Bush is Republican, this desk is wood,
      etc (object `obj` has some attribute `a`, or has an attribute
      with a value of `a`.)

    - Santa Claus is Santa Claus, 2 + 2 is 4, etc (identity)


    Not done yet:

    - 2 is even (search for an `is_even` function and see if is_even(2) == True)
    '''
    #
    # TODO(elimisteve): Consider leaving this notion of 'is' out
    #

    # if type(obj) == type(attr_value):
    #     return obj is attr_value

    # TODO(elimisteve): Questionable.  Should string comparisons work?
    if isinstance(obj, str) and isinstance(attr_value, str):
        return obj is attr_value

    # If they're not both strings, assume they're both objects and compare
    if type(obj) != str and type(attr_value) != str:
        # TODO(elimisteve): Could use `==` instead of `is` here, especially
        # to make dict comparisons match... but it's not clear that
        # that would be the right behavior; shouldn't a custom __eq__
        # method be defined in that case, a custom equals() method
        # function, or similar?
        return obj is attr_value


    assert type(obj) != str
    assert type(attr_value) == str

    # Check for `obj.something == attr_value`
    matches_value = any([ v == attr_value or is_collection(v) and attr_value in v
                          for v in obj.__dict__.values() ])
    if matches_value:
        return True

    # Check for `obj.attr_value is True`
    if has_attr(obj, attr_value) and get_attr(obj, attr_value)[0] is True:
        return True

    return False


# Does(some_object, 'exists') is probably less awkward than
# Is(some_object, 'exists').  Maybe.
##Does = Is
