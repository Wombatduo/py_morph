from abc import ABC, abstractmethod

from grammar.Grammar import Tense, Person, Number, Genus


class AbstractVerb(ABC):

    def __init__(self, infinitive):
        self.infinitive = infinitive.lower()

    @abstractmethod
    def morph(self, person, number, tense, genus):
        pass

    pronouns = {
        Person.FIRST: 'I',
        Person.SECOND: 'You',
        Person.THIRD: 'He'
    }

    def pronoun(self, person, number, genus):
        return self.pronouns[Person(person)][Number(number)][Genus(genus)]

    def get_infinitive(self):
        """

        :rtype: str
        """
        return self.infinitive
