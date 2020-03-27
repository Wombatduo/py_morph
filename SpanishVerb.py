from AbstarctVerb import AbstractVerb
import enum


class Person(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Number(enum.Enum):
    SINGULAR = 1
    PLURAL = 2


class Tense(enum.Enum):
    PAST = 1
    PRESENT = 2
    FUTURE = 3


class Genus(enum.Enum):
    MALE = 1
    FEMALE = 2
    MIDDLE = 3


class Type(enum.Enum):
    PERFECT = 1
    IMPERFECT = 2


class Case(enum.Enum):
    FIRST = 1
    SECOND = 2


class SpanishVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PAST.value:
            if self.infinitive == "ser":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "fui"
                    elif person == Person.SECOND.value:
                        return "fuiste"
                    elif person == Person.THIRD.value:
                        return "fue"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "fuimos"
                    elif person == Person.SECOND.value:
                        return "fuisteis"
                    elif person == Person.THIRD.value:
                        return "fueron"
        elif tense == Tense.PRESENT.value:
            if self.infinitive == "ser":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "soy"
                    elif person == Person.SECOND.value:
                        return "eres"
                    elif person == Person.THIRD.value:
                        return "es"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "somos"
                    elif person == Person.SECOND.value:
                        return "sois"
                    elif person == Person.THIRD.value:
                        return "son"
        elif tense == Tense.FUTURE.value:
            if self.infinitive == "ser":
                return "será"
