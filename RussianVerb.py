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


class RussianVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
            if person == 1:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делаю"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делаем"
            if person == 2:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делаешь"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делаете"
            if person == 3:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делает"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делают"
        if tense == Tense.PAST.value:
            if person == 1:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
            if person == 2:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
            if person == 3:
                if number == Number.SINGULAR.value and Genus.MALE.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.SINGULAR.value and Genus.FEMALE.value:
                    if self.infinitive == "делала":
                        return "делал"
                elif number == Number.SINGULAR.value and Genus.MIDDLE.value:
                    if self.infinitive == "делало":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
        if tense == Tense.FUTURE.value:
            if person == 1:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "буду " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "будем " + self.get_infinitive()
            elif person == 2:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "будешь " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "будете " + self.get_infinitive()
            elif person == 3:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "будет " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "будут " + self.get_infinitive()


    def get_perfect_form(self, person, number):
        perfect_form = self.get_ed_form()
        if "/" in perfect_form:
            if number == Number.SINGULAR.value:
                perfect_form = perfect_form.split("/", 1)[0]
            elif number == Number.PLURAL.value:
                perfect_form = perfect_form.split("/", 1)[1]
        if person == Person.FIRST.value or person == Person.SECOND.value or number == Number.PLURAL.value:
            return "have " + perfect_form
        elif person == Person.THIRD.value:
            return "has " + perfect_form

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
