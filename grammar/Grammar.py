from enum import Enum


class Number(Enum):
    SINGULAR, PLURAL = range(1, 3)


class Person(Enum):
    FIRST, SECOND, THIRD = range(1, 4)

    @property
    def pronoun(self):
        return get_pronoun[self]


get_pronoun = {
    Person.FIRST: 'Я',
    Person.SECOND: 'Ты',
    Person.THIRD: 'Он'
}


class Tense(Enum):
    PAST, PRESENT, FUTURE = range(1, 4)

    @property
    def head(self):
        return get_head[self]

get_head = {
    Tense.PAST: 'Прошедшее',
    Tense.PRESENT: 'Настоящее',
    Tense.FUTURE: 'Будущее'
}

class Genus(Enum):
    MALE, FEMALE, MIDDLE = range(1, 4)


class PronounForNumber(Enum):
    SINGULAR = {Person.FIRST: "I", Person.SECOND: "You", Person.THIRD: "He"}
    PLURAL = {Person.FIRST: "We", Person.SECOND: "You", Person.THIRD: "They"}


class Pronoun:
    PRONOUNS = {'MALE': ('He', 'They'), 'FEMALE': ('She', 'They'), 'MIDDLE': ('It', 'Its')}

    def __init__(self, gender):
        self.singular, self.plural = self.PRONOUNS[gender]




class Type(Enum):
    PERFECT = 1
    IMPERFECT = 2


class Case(Enum):
    FIRST = 1
    SECOND = 2
