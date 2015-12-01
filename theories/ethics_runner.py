#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.11.28

import exphil

def is_moral_theory_runner(theory, context):
    '''
    Takes an ethical theory and a context describing the situation at
    hand, and computes whether or not the action performed in the
    described context is ethical according to the given theory.
    '''
    if theory['is_skeptical']:
        raise exphil.Except("There are no moral facts")

    if theory['is_infinitely_lenient']:
        return True

    if theory['is_infinitely_strict']:
        return False

    if theory['is_consequentialist']:
        if not context['resulting_harm'] or context['net_lives_saved']:
            return True
        else:
            return False

    if theory['is_kantian']:
        if context['benign_intent'] and context['foreseeable_resulting_harm'] < 0.1:
            return True
        else:
            return False

    # TODO(elimisteve): Add many more checks here

    raise exphil.NotImplementedYet(
        "Handling moral theories like  {}  not implemented".format(theory))


if __name__ == '__main__':
    skepticism = {
        'is_skeptical': True,
        'is_infinitely_strict': False,
        'is_infinitely_lenient': False,
        'is_consequentialist': False,
        'is_kantian': False,
    }
    everything_is_moral = {
        'is_skeptical': False,
        'is_infinitely_strict': False,
        'is_infinitely_lenient': True,
        'is_consequentialist': False,
        'is_kantian': False,
    }
    everything_is_immoral = {
        'is_skeptical': False,
        'is_infinitely_strict': True,
        'is_infinitely_lenient': False,
        'is_consequentialist': False,
        'is_kantian': False,
    }
    consequentialism = {
        'is_skeptical': False,
        'is_infinitely_strict': False,
        'is_infinitely_lenient': False,
        'is_consequentialist': True,
        'is_kantian': False,
    }
    kantian = {
        'is_skeptical': False,
        'is_infinitely_strict': False,
        'is_infinitely_lenient': False,
        'is_consequentialist': False,
        'is_kantian': True,
    }

    theories = {
        'Skepticism': skepticism,
        'Everything is moral': everything_is_moral,
        'Everything is immoral': everything_is_immoral,
        'Consequentialism': consequentialism,
        'Kantian': kantian,
    }


    murder = {
        'resulting_harm': True,
        'foreseeable_resulting_harm': True,
        'benign_intent': False,
        'net_lives_saved': False,
    }
    manslaughter = {
        'resulting_harm': True,
        'foreseeable_resulting_harm': 0.05, # Low perceived chance of harm
        'benign_intent': True,
        'net_lives_saved': False,
    }
    innocuous = {
        'resulting_harm': False,
        'foreseeable_resulting_harm': False,
        'benign_intent': True,
        'net_lives_saved': False,
    }
    organ_harvesting = {
        'resulting_harm': True,
        'foreseeable_resulting_harm': True,
        'benign_intent': True,
        'net_lives_saved': True,
    }

    contexts = {
        'murder': murder,
        'accidental manslaughter': manslaughter,
        'walking': innocuous,
        'organ harvesting': organ_harvesting,
    }

    max_context_len = max([len(c) for c in contexts])

    for t in theories:
        print "\nAccording to the {} ethical theory  {}:".format(
            t, theories[t])
        for c in contexts:
            try:
                moral = is_moral_theory_runner(theories[t], contexts[c])
            except (exphil.Except, exphil.NotImplementedYet) as e:
                print "  {}".format(e)
                continue

            print ("  {:"+str(max_context_len)+"s}  is  {}").format(
                c, 'moral' if moral else 'immoral')
