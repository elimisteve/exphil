#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.07.11

import exphil
import exphil.things.color

class Snow(exphil.Object):

    def __init__(self, mass_in_grams, **kwargs):
        self.mass_in_grams = mass_in_grams
        exphil.update_object(self, kwargs)

        self.color = exphil.things.color.ColorWhite


# TODO(elimisteve): Artifact -- 10 grams of snow exist
snow = Snow(10)

snow_id = id(snow)
