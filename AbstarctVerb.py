import enum
from abc import ABC, abstractmethod


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


class AbstractVerb(ABC):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: "I", Genus.FEMALE: "I", Genus.MIDDLE: "I"},
            Number.PLURAL: {Genus.MALE: "We", Genus.FEMALE: "We", Genus.MIDDLE: "We"}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: "You", Genus.FEMALE: "You", Genus.MIDDLE: "You"},
            Number.PLURAL: {Genus.MALE: "You", Genus.FEMALE: "You", Genus.MIDDLE: "You"}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: "He", Genus.FEMALE: "She", Genus.MIDDLE: "It"},
            Number.PLURAL: {Genus.MALE: "They", Genus.FEMALE: "They", Genus.MIDDLE: "They"}}
    }

    def __init__(self, infinitive):
        self._infinitive = infinitive.lower()

    @abstractmethod
    def morph(self, person, number, tense, genus, infinitive):
        pass

    @classmethod
    def get_pronoun(cls, person, number, genus):
        return cls.pronouns[Person(person)][Number(number)][Genus(genus)]

    def get_infinitive(self):
        return self._infinitive
