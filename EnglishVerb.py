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
        if person == Person.FIRST.value and number == Number.SINGULAR.value:
            return "am"
        elif person == Person.SECOND.value and number == Number.SINGULAR.value:
            return "are"
        elif person == Person.THIRD.value  and number == Number.SINGULAR.value:
            return "is"
        elif person == Person.FIRST.value  and number == Number.PLURAL.value:
            return "are"
        elif person == Person.SECOND.value and number == Number.PLURAL.value:
            return "are"
        elif person == Person.THIRD.value  and number == Number.PLURAL.value:
            return "are"
