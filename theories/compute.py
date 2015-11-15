#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.04

import exphil
import exphil.theories.language

def what(iterable, *args):
    '''
    `iterable` is usually a list of theories, each of which accept
    `*args`.  E.g., "what is the MEANING of $utterance?"
    '''

    # See http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable for potentially better ways to do this.  Or insist that what is now called `iterable` is a list
    if not hasattr(iterable, '__iter__'):
        # If there's only one input function given, then there's only one answer
        # we need to return...
        return iterable(*args)  # or `{iterable(*args)}` ?

    answers = set()
    for f in iterable:
        answers.add( f(*args) )
        # answers.add({ f.__name__, {f(*args)} })

    return answers
    # return {f(*args) for f in iterable}


#utterance = UtteranceContext('...')
print what(exphil.theories.language.meaning, 5)
