from AbstarctVerb import AbstractVerb

import enum


class Person(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Number(enum.Enum):
    SINGULAR = 1
    PLURAL = 2


class EnglishVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):
        if person == Person.FIRST and number == Number.SINGULAR:
            return "am"
        elif person == Person.SECOND and number == Number.SINGULAR:
            return "are"
        elif person == Person.THIRD  and number == Number.SINGULAR:
            return "is"
        elif person == Person.FIRST  and number == Number.PLURAL:
            return "are"
        elif person == Person.SECOND and number == Number.PLURAL:
            return "are"
        elif person == Person.THIRD  and number == Number.PLURAL:
            return "are"
