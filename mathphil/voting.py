#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.07.16

import collections
import math
import random

import exphil

def borda(prefs):
    '''
    prefs should be a tuple of tuples indicating preferences.  E.g.,
    (('A', 'B', 'C'), ('A', 'C', 'B'), ('C', 'B', 'A'))

    TODO(elimisteve): Handle ties, like ('A', ('B', 'C')) or perhaps ('A',
    {'B', 'C'}) means that A is preferred to B and C, but neither B
    nor C is preferred to the other.


    NOTE(elimisteve): Supposedly always spits out an ordering, unlike
    Condorcet (as per MathPhil lecture 7-1)

    Violates Independence of Irrelevant Alternatives
    '''
    # assert len(pairs) == math.factorial(numvoters)/2

    if not prefs:
        return None

    # If only 1 person voted, the first person's favorite candidate is
    # the winner
    if len(prefs) == 1:
        return prefs[0][0]

    assert len(prefs) > 1

    vote_totals = collections.defaultdict(int)

    # Tally votes for each candidate.  Each time a candidate is
    # preferred over another one, add 1 to its vote total.
    #
    # (This is equivalent to, but simpler to implement than, assigning
    # points based upon ordering; those point assignments are
    # mathematically identical to the sum of the number of opponents
    # beaten by each candidate according to each voter, which is how
    # this algorithm is implemented below.)
    #
    # Also track the candidate with the most votes with `winners`.
    winners = set()
    max_votes = 0

    for vote in prefs:
        for left_ndx in xrange(len(vote)):
            for _ in vote[left_ndx+1:]:
                # left candidate
                l_candidate = vote[left_ndx]
                vote_totals[l_candidate] += 1

                # Keep track of who's winning
                candidate_total = vote_totals[l_candidate]

                if candidate_total == max_votes:
                    winners.add(l_candidate)
                elif candidate_total > max_votes:
                    winners = set([l_candidate])
                    max_votes = candidate_total


    if len(winners) == 1:
        return winners.pop()

    # Multiple winners
    return frozenset(winners)


def condorcet(prefs):
    '''
    Pair-wise comparison of all candidates

    Violates Universal Domain
    '''
    vote_totals = collections.defaultdict(int)

    for vote in prefs:
        for left_ndx in xrange(len(vote)):
            for right in vote[left_ndx+1:]:
                left = vote[left_ndx]
                vote_totals[(left, right)] += 1

    # # Detect winner(s)
    # winners = set()
    # max_votes = 0



    # TODO(elimisteve): Detect cycles

    # The winner is the one that defeats all other candidates in a
    # pair-wise comparison, unless vote_totals[A] == vote_totals[B]
    # and A and B each beat all other candidates.

    # Only bother comparing (A, B), not (B, A); that's wasteful

    # "There's a cycle => Transitivity was violated".  So check for
    # transitivity violations to check for cycles?

    # When detecting cycles, remember that there could be one option
    # as a winner and a cycle between the remaining options!


    # FIXME(elimisteve): For now, assume there is either 1 winner, or a tie
    # between all candidates
    candidates = prefs[0]
    for c in candidates:
        other_candidates = [other for other in candidates if other != c]
        if all(vote_totals[(c, other)] > vote_totals[(other, c)] for other in other_candidates):
            # c beat all others
            return c

    # To repeat...
    # FIXME(elimisteve): For now, assume there is either 1 winner, or a tie
    # between all candidates
    return frozenset(candidates)

    # if len(winners) == 1:
    #     return winners.pop()

    # # Multiple winners
    # return winners


def approval_n(prefs, top_n):
    '''
    Approval Voting.  Voters state their preferences, then we ignore
    all but their favorite top_n candidates and see who gets more
    votes, ignoring the ordering of those top_n candidates and just
    counting how many times a candidate shows up in the top_n (0 or 1
    times per voter).

    Assumes every voter states their opinion on every candidate
    running.

    Violates Universal Domain (right? Since someone's first n choices
    could be swapped and that won't affect the outcome?).
    '''
    winners = set()
    max_votes = 0

    vote_totals = collections.defaultdict(int)
    for pref in prefs:
        for candidate in pref[:top_n]:
            vote_totals[candidate] += 1

            # Keep track of who's winning
            candidate_total = vote_totals[candidate]
            if candidate_total == max_votes:
                winners.add(candidate)
            elif candidate_total > max_votes:
                winners = set([candidate])
                max_votes = candidate_total


    if len(winners) == 1:
        return winners.pop()

    # Multiple winners
    return frozenset(winners)


def approval_2(prefs):
    return approval_n(prefs, 2)

def approval_3(prefs):
    return approval_n(prefs, 3)


def majority(prefs):
    '''
    Which candidate is the first choice of the most voters?
    '''
    # Majority voting is a special case of approval voting, where
    # voters only approve of their top 1 favorite candidate.
    return approval_n(prefs, 1)


all_theories = (
    borda,
    condorcet,
    approval_2,
    approval_3,
    majority,
)


def randomly(prefs):
    '''
    Randomly choose a candidate among those included in the first
    voter's preferences.

    Assumes the first voter states his/her opinion on every candidate.
    '''
    candidates = prefs[0]
    return random.choice[candidates]


##
## When in doubt, go meta
##

def metatheory_simple(prefs, theories=all_theories):
    '''
    Which candidate do most theories consider to be the winner?
    '''
    borda_winner     = borda(prefs)
    condorcet_winner = condorcet(prefs)
    approval2_winner = approval_2(prefs)
    approval3_winner = approval_3(prefs)
    majority_winner  = majority(prefs)

    winners = (
        tuple([borda_winner]),
        tuple([condorcet_winner]),
        tuple([approval2_winner]),
        tuple([approval3_winner]),
        tuple([majority_winner]),
    )

    return majority(winners)


# def metatheory_approval_n(prefs, top_n_candidates, top_n_theories, weighers, theories=all_theories):
#     theories


if __name__ == '__main__':
    all_prefs = []

    # A
    prefs1 = (
        ('A', 'B', 'C'),
        ('A', 'B', 'C'),
        ('A', 'B', 'C'),
    )
    all_prefs.append(prefs1)

    # Usually A
    prefs2 = (
        ('A', 'B', 'C'),
        ('B', 'A', 'C'),
        ('C', 'A', 'B'),
    )
    all_prefs.append(prefs2)

    # No preference
    prefs3 = (
        ('A', 'B', 'C'),
        ('B', 'C', 'A'),
        ('C', 'A', 'B'),
    )
    all_prefs.append(prefs3)

    # D borda-helps A
    prefs4 = (
        ('A', 'D', 'B', 'C'),
        ('B', 'C', 'A', 'D'),
        ('C', 'A', 'D', 'B'),
    )
    all_prefs.append(prefs4)

    # A is majority winner & condorcet loser; B is borda winner
    prefs5 = (
        ('A', 'B', 'C', 'D'),
        ('A', 'B', 'C', 'D'),
        ('B', 'C', 'D', 'A'),
        ('D', 'B', 'C', 'A'),
        ('C', 'D', 'B', 'A'),
    )
    all_prefs.append(prefs5)


    # dict[prefs] -> dict[theory] -> winner(s)
    results = collections.defaultdict(dict)

    for prefs in all_prefs:
        print "\n\n\nVotes:", prefs
        print
        for theory in all_theories:
            winners = theory(prefs)
            results[prefs][theory.func_name] = winners
            print theory.func_name, '  \t', winners


    # Compare each individual theory's computed winners with those
    # from metatheory_simple, which computes the most common winner
    # among all the other (non-meta) theories of voting.
    print "\n\n\nWhich theory agrees with a majority of the other theories" + \
        " most frequently (regarding the winners of the above elections)?\n"

    agreement_with_most_theories = collections.defaultdict(int)

    for prefs in results:
        metatheory_simple_winner = metatheory_simple(prefs)
        for theory in results[prefs]:
            # If theory agrees with metatheory_simple regarding who
            # won, track this
            if results[prefs][theory] == metatheory_simple_winner:
                agreement_with_most_theories[theory] += 1

    winners = sorted(agreement_with_most_theories.keys(),
                     key=lambda x: agreement_with_most_theories[x],
                     reverse=True)
    for winner in winners:
        print winner, '  \t', agreement_with_most_theories[winner]
