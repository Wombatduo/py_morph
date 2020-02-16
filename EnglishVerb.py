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

        if self.is_irregular:
            if tense == 1:
                past_simple = self.get_irregular()["past simple"]
                if "/" in past_simple:
                    if number == Number.SINGULAR.value:
                        past_simple = past_simple.split("/", 1)[0]
                    elif number == Number.PLURAL.value:
                        past_simple = past_simple.split("/", 1)[1]
                return past_simple
            elif tense == 2:
                if self.infinitive == "be":
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
                if self.infinitive == "do":
                    if person == Person.THIRD.value and number == Number.SINGULAR.value:
                        return "does"
                return self.infinitive
            elif tense == 3:
                return "will " + self.infinitive
            elif tense == 4:
                return self.get_perfect_form(person, number)
        else:
            if tense == 1:
                return self.get_ed_form()
            elif tense == 2:
                return self.infinitive
            elif tense == 3:
                return "will " + self.infinitive
            elif tense == 4:
                return self.get_perfect_form(person, number)

    def get_perfect_form(self, person, number):
        if person == Person.FIRST.value or person == Person.SECOND.value or number == Number.PLURAL.value:
            return "have " + self.get_ed_form()
        elif person == Person.THIRD.value:
            return "has " + self.get_ed_form()

    def get_ed_form(self):
        if self.is_irregular:
            return self.get_irregular()["-ed"]
        if self.infinitive[-1] == 'e':
            return self.infinitive + "d"
        return self.infinitive + "ed"

    def get_irregular(self):
        path = 'irverbs.txt'
        with open(path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        search = self.infinitive
        for iverb in verbs_list:
            base = iverb["base form"]
            if "[" in base:
                base = base.split("[")[0].strip()
                # print(">" + base + "<")
            if base.strip() == search.strip():
                return iverb
        return None

    @property
    def is_irregular(self):
        if self.get_irregular() is not None:
            return True
        return False
