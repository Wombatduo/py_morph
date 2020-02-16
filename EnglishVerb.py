from AbstarctVerb import AbstractVerb
import enum
import sys


class Person(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


class Number(enum.Enum):
    SINGULAR = 1
    PLURAL = 2


class EnglishVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if self.is_irregular(self.infinitive):
            return self.infinitive

        if person == Person.FIRST.value and number == Number.SINGULAR.value:
            return "am"
        elif person == Person.SECOND.value and number == Number.SINGULAR.value:
            return "are"
        elif person == Person.THIRD.value and number == Number.SINGULAR.value:
            return "is"
        elif person == Person.FIRST.value and number == Number.PLURAL.value:
            return "are"
        elif person == Person.SECOND.value and number == Number.PLURAL.value:
            return "are"
        elif person == Person.THIRD.value and number == Number.PLURAL.value:
            return "are"

    def is_irregular(self, verb):
        path = 'irverbs.txt'
        with open(path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        search = verb
        for iverb in verbs_list:
            if iverb["base form"] == search:
                print("глагол " + search + " - неправильный:\n" + iverb["past simple"] + " | " + iverb["-ed"],
                      file=sys.stderr)
                return True
        return False
