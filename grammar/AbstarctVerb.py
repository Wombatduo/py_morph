from abc import ABC, abstractmethod


class AbstractVerb(ABC):

    def __init__(self, infinitive):
        self.infinitive = infinitive.lower()

    @abstractmethod
    def morph(self, person, number, tense, genus):
        pass

    def get_infinitive(self):
        """

        :rtype: str
        """
        return self.infinitive
