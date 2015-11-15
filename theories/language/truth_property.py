# "truth is a property of sentences"

class Sentence(str):

    @property
    def true(self):
        '''
        TODO: Need to do way more than just `eval` for this to
        actually work, but my point was having `truth` be a property
        of a sentence.
        '''
        try:
            # Or perhaps bool(eval(self))
            return eval(self)
        except:
            # TODO(elimisteve): Consider 
            return False

# Ex: print Sentence("2 + 2 == 4").true  # True
# Ex: print Sentence("2 + 2 == 5").true  # False
