from AbstarctVerb import AbstractVerb


class EnglishVerb(AbstractVerb):


    def morph(self, person, number, tense, genus):
        return "am"