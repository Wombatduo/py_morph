from abc import ABC, abstractmethod


class AbstractVerb(ABC):

    def __init__(self, infinitive):
        self.infinitive = infinitive

    @abstractmethod
    def morph(self, person, number, tense, genus):
        pass

    def get_infinitive(self):
        return self.infinitive
