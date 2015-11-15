#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.12

import datetime

import _person

from exphil.things import color

SantaClaus = _person.FictionalPerson(
    'Santa', None, 'Claus', None,  # Name and birthday
    overweight=True,
    joyous=True,
    mustache=True,
    clothing_colors=(color.ColorRed, color.ColorWhite),
    hair_colors=(color.ColorWhite, color.ColorGray),
    nicknames=('Santa', 'Saint Nick', 'Kris Kringle'),
    exists=False,
)
SantaClaus_ID = id(SantaClaus)

# TODO(elimisteve): Being a King who never ruled is weird
PresentKingOfFrance = _person.Person(
    None, None, None, None,  # No name, no birthday
    rule_interval=None,
    king=True,

    # TODO(elimisteve): Eventually replace 'France' with complex object
    king_of_country='France',
    exists=False,
)
PresentKingOfFrance_ID = id(PresentKingOfFrance)

Nietzsche = _person.Person(
    'Friedrich', 'Wilhelm', 'Nietzsche', datetime.date(1844, 10, 15),
    deathday=datetime.date(1900, 8, 25),
    nationality='German',
    religion=None,
    mustache=True,
    philosopher=True,
    author=True,

    # TODO(elimisteve): Eventually replace book titles with,e.g., Books
    author_of=('Thus Spake Zarathustra', 'The Gay Science'),
)
Nietzsche_ID = id(Nietzsche)
