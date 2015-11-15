#!/usr/bin/env python
# Steven Phillips / elimisteve
# 2015.06.04

import exphil

class AnswerSet(exphil.Object):

    def __init__(answer_dict):
        # map[theory_import_path]answer_from_corresponding_theory
        self.answer_dict = answer_dict
        self.answer_set = set(answers.values())

    def __str__(self):
        return str(self.answer_set)
