#!/usr/bin/env python
# Steve Phillips / elimisteve
# 2015.06.06

import _webcolors

class Color(object):

    # TODO: Consider accepting a colloquial_name, too (e.g., 'red')

    def __init__(self, r, g, b):
        if any([color < 0 or color > 255 for color in (r, g, b)]):
            raise ValueError("r, g, and b must be integers between 0 and 255, inclusive")

        self.red = r
        self.green = g
        self.blue = b

    def __eq__(self, color):
        '''
        For two colors to be equal to each other, where each color is
        "represented" as an RGB (red, green, blue) value, is for them
        to have the same amount of red, green, and blue, respectively.
        '''
        if not isinstance(color, Color):
            return False

        return (self.red, self.green, self.blue) == \
            (color.red, color.green, color.blue)

    def __ne__(self, color):
        return not self == color

    def redder_than(self, color):
        return self.red > color.red

    def greener_than(self, color):
        return self.green > color.green

    def bluer_than(self, color):
        return self.blue > color.blue

    def naive_distance(self, color):
        '''
        See http://en.wikipedia.org/wiki/Color_difference for "better"
        definitions
        '''
        return abs(self.red - color.red) + \
            abs(self.green - color.green) + \
            abs(self.blue - color.blue)

    def naive_distance2(self, color):
        self_sum = self.red + self.green + self.blue
        color_sum = color.red + color.green + color.blue
        return abs(self_sum - color_sum)

    @property
    def name(self):
        actual, closest = _webcolors.get_colour_name(
            (self.red, self.green, self.blue)
        )
        return actual or closest



# Convenience definitions

ColorWhite = Color(255, 255, 255)
ColorGray  = Color(128, 128, 128)
ColorBlack = Color(0, 0, 0)

ColorRed   = Color(255, 0, 0)
ColorGreen = Color(0, 255, 0)
ColorBlue  = Color(0, 0, 255)
