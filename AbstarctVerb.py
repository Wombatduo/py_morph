import enum
from abc import ABC, abstractmethod


class AbstractVerb(ABC):

    def __init__(self, infinitive):
        self.infinitive = infinitive.lower()

    @abstractmethod
    def morph(self, person, number, tense, genus):
        pass

    def get_infinitive(self):
        return self.infinitive


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
    # PERFECT = 4
    # CONTINUOUS = 5