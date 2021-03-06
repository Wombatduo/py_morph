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


class GermanVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PAST.value:
            if self.infinitive == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "war"
                    elif person == Person.SECOND.value:
                        return "warst"
                    elif person == Person.THIRD.value:
                        return "war"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "waren"
                    elif person == Person.SECOND.value:
                        return "wart"
                    elif person == Person.THIRD.value:
                        return "waren"
        elif tense == Tense.PRESENT.value:
            if self.infinitive == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "bin"
                    elif person == Person.SECOND.value:
                        return "bist"
                    elif person == Person.THIRD.value:
                        return "ist"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "sind"
                    elif person == Person.SECOND.value:
                        return "seid"
                    elif person == Person.THIRD.value:
                        return "sind"
        elif tense == Tense.FUTURE.value:
            if self.infinitive == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return ""
                    elif person == Person.SECOND.value:
                        return ""
                    elif person == Person.THIRD.value:
                        return ""
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return ""
                    elif person == Person.SECOND.value:
                        return ""
                    elif person == Person.THIRD.value:
                        return ""
