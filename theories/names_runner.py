#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.12.01

import exphil.objects
import exphil.objects.people
import exphil.objects.query

from exphil.objects import _person

import copy


def refers_to_theory_runner(theory, context):
    if 'ontology' in context:
        ontology = context['ontology']
    else:
        ontology = exphil.objects.all

    if theory['is_skeptical']:
        # Skeptical theories don't believe in reference, and therefore
        # don't think anything refers to anything.
        return None

    if theory['is_descriptivist']:
        if context['description'] is None:
            return None

        objs = exphil.objects.query.by_dict(context['description'],
                                            ontology=ontology)

        if len(objs) == 0:
            return None

        if len(objs) == 1:
            return objs[0]

        if theory['is_singular']:
            raise ValueError(
                "Singular theories don't permit references to multiple entities"
            )
        else:
            return objs


    if theory['is_intensional']:
        return context['intended_referent']

    if theory['is_rigid_designating']:
        # Rigid(ly) designating theories say that names refer
        # directly, and therefore when you have a name of someone, you
        # have a reference to them.
        return context['reference']

    raise exphil.NotImplementedYet(
        "Handling theories of reference like  {}  not implemented".format(theory))


if __name__ == '__main__':
    references_dont_exist = {
        'is_skeptical': True,
        'is_descriptivist': False,
        'is_singular': True,
        'is_rigid_designating': False,
        'is_intensional': False,
    }
    everything_refers_to_nothing = {
        'is_skeptical': True,
        'is_descriptivist': False,
        'is_singular': True,
        'is_rigid_designating': False,
        'is_intensional': False,
    }
    # What should the difference(s) between the 2 above theories be?

    descriptivism = {
        'is_skeptical': False,
        'is_descriptivist': True,
        'is_singular': True,
        'is_rigid_designating': False,
        'is_intensional': False,
    }

    # TODO(elimisteve): Distinguish between Mill, Kripke, and Salmon
    direct_reference = {
        'is_skeptical': False,
        'is_descriptivist': False,
        'is_singular': True,
        'is_rigid_designating': True,
        'is_intensional': False,
    }

    plural_direct_reference = {
        'is_skeptical': False,
        'is_descriptivist': False,
        'is_singular': False,  # OK for a description to refer to multiple entities
        'is_rigid_designating': True,
        'is_intensional': False,
    }

    intensional = {
        'is_skeptical': False,
        'is_descriptivist': False,
        'is_singular': False,  # Could intend to refer to multiple entities
        'is_rigid_designating': False,
        'is_intensional': True,
    }

    theories = {
        'References do not exist': references_dont_exist,
        'Nothing refers': everything_refers_to_nothing,
        'Descriptivist': descriptivism,
        'Direct reference': direct_reference,
        'Intensional': intensional,
    }

    ##
    ## Contexts
    ##

    santa_description = {
        'description': {'first_name': 'Santa',
                        'last_name': 'Claus',
                        'fictional': True},
        'reference': exphil.objects.people.SantaClaus,
        'intended_referent': exphil.objects.people.SantaClaus,
    }

    # A friend tells you of the BRILLIANT female philosopher who wrote
    # 'The Origins of Totalitarianism' and 'Thus Spake Zarathustra',
    # both of which he has read.
    female_author_of_zarathustra = {
        'description': {'sex': 'female',
                        'author_of': 'Thus Spake Zarathustra',
                        'philosopher': True},
        'reference': exphil.objects.people.Nietzsche,
        'intended_referent': exphil.objects.people.Nietzsche,
    }

    # TODO(elimisteve): Include a fallible version of descriptivism
    # here, where a 100% descriptive match isn't necessary.

    # Kripke's thought experiment
    schmidt = _person.Person(
        None, None, 'Schmidt', None,
        mathematician=True,
        discovered=('The Incompleteness Theorem', 'The Completeness Theorem'),
    )
    godel = copy.copy(exphil.objects.people.Godel)
    # In this thought experiment, Godel didn't discover the incompleteness theorem
    godel['discovered'] = None

    discoverer_of_incompleteness_theorem = {
        'description': {'discovered': 'The Incompleteness Theorem'},
        'reference': godel,
        'intended_referent': godel,
        'ontology': (godel, schmidt),
    }

    
    contexts = {
        'Santa': santa_description,
        'Female author of "Thus Spake Zarathustra"': female_author_of_zarathustra,
        "Discoverer of the incompleteness theorem (in Kripke's thought experiment)": discoverer_of_incompleteness_theorem,
    }

    max_context_len = max([len(c) for c in contexts])

    for t in theories:
        print "\n\nAccording to the `{}` theory of reference  {}:".format(
            t, theories[t])
        for c in contexts:
            try:
                ref = refers_to_theory_runner(theories[t], contexts[c])
            except (exphil.Except, exphil.NotImplementedYet) as e:
                print "  {}".format(e)
                continue

            print ("\n  {:"+str(max_context_len)+"s}  refers to  {}").format(
                c, ref)
