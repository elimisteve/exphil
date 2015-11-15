#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.09

class ExPhil(object):
    '''
    Every ExPhil Object, Theory, ThoughtExperiment, etc -- probably
    every class defined in any ExPhil argument -- should inherit from
    this class (ExPhil).
    '''

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls, *args, **kwargs)

        # TODO(elimisteve): Consider making this a custom dict-based type that
        # warns us when replacing an existing key's value
        obj.exphil_attrs = {}

        return obj


class Object(ExPhil):
    '''
    Every object posited by any argument should inherit from this
    class (Object).
    '''

    def __new__(cls, *args, **kwargs):
        obj = ExPhil.__new__(cls, *args, **kwargs)
        obj.exphil_attrs.update({
            'type': 'Object',
        })
        return obj


class Theory(Object):  # TODO(elimisteve): Inherit from Object, or no?
    '''
    Every (translation of a) philosophical theory defined should
    inherit from this class (Theory).
    '''

    def __new__(cls, *args, **kwargs):
        obj = Object.__new__(cls, *args, **kwargs)
        obj.exphil_attrs.update({
            'type': 'Theory',
        })
        obj.theory = {}
        return obj


class ThoughtExperiment(ExPhil):

    def __new__(cls, *args, **kwargs):
        obj = ExPhil.__new__(cls, *args, **kwargs)
        obj.exphil_attrs.update({
            'type': 'ThoughtExperiment',
        })
        return obj


# TODO(elimisteve): Create TheoryOfLanguage(Theory), then
# TheoryOfNames(TheoryOfLanguage)?

# TODO(elimisteve): Instead call this TheoryOfReference?
class TheoryOfNames(Theory):

    def __new__(cls, *args, **kwargs):
        obj = Theory.__new__(cls, *args, **kwargs)
        obj.exphil_attrs.update({
            'type': 'TheoryOfNames',
        })

        # There are implicit assumptions made by most theories of names
        obj.theory.update({
            'names_refer': True,
        })

        return obj


    def __init__(self, *args, **kwargs):
        self.theory.update(kwargs)
