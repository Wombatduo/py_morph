from AbstarctVerb import AbstractVerb

import enum

class Person(enum.Enum):
   First = 1
   Second = 2
   Third = 3

class EnglishVerb(AbstractVerb):


    def morph(self, person, number, tense, genus):
        if person == Person.First:
            return "am"
        elif person == Person.Second:
            return "are"
        elif person == Person.Third:
            return "is"