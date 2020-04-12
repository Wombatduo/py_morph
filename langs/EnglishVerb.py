from grammar.AbstarctVerb import AbstractVerb

from grammar.Grammar import Tense, Person, Number, Genus


class EnglishVerb(AbstractVerb):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: 'I', Genus.FEMALE: 'I', Genus.MIDDLE: 'I'},
            Number.PLURAL: {Genus.MALE: 'We', Genus.FEMALE: 'We', Genus.MIDDLE: 'We'}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: 'You', Genus.FEMALE: 'You', Genus.MIDDLE: 'You'},
            Number.PLURAL: {Genus.MALE: 'You', Genus.FEMALE: 'You', Genus.MIDDLE: 'You'}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: 'He', Genus.FEMALE: 'She', Genus.MIDDLE: 'It'},
            Number.PLURAL: {Genus.MALE: 'They', Genus.FEMALE: 'They', Genus.MIDDLE: 'They'}}
    }

    def morph(self, person, number, tense, genus):

        if self.is_irregular:
            if tense == Tense.PAST.value:
                past_simple = self.get_irregular()["past simple"]
                if "/" in past_simple:
                    if number == Number.SINGULAR.value:
                        past_simple = past_simple.split("/", 1)[0]
                    elif number == Number.PLURAL.value:
                        past_simple = past_simple.split("/", 1)[1]
                return past_simple

            elif tense == Tense.PRESENT.value:
                if self.get_infinitive() == "be":
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
                if self.get_infinitive() == "do":
                    if person == Person.THIRD.value and number == Number.SINGULAR.value:
                        return "does"
                if self.get_infinitive() == "have":
                    if person == Person.THIRD.value and number == Number.SINGULAR.value:
                        return "has"
                if person == Person.THIRD.value and number == Number.SINGULAR.value:
                    return self.get_infinitive() + "s"
                return self.get_infinitive()

            elif tense == Tense.FUTURE.value:
                return "will " + self.get_infinitive()

            elif tense == 4:
                return self.get_perfect_form(person, number)

        elif not self.is_irregular:

            if tense == Tense.PAST.value:
                return self.get_ed_form()

            elif tense == Tense.PRESENT.value:
                if person == Person.THIRD.value and number == Number.SINGULAR.value:
                    return self.get_infinitive() + "s"
                return self.get_infinitive()

            elif tense == Tense.FUTURE.value:
                return "will " + self.get_infinitive()

            elif tense == 4:
                return self.get_perfect_form(person, number)

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
        if self.get_infinitive()[-1] == 'e':
            return self.get_infinitive() + "d"
        return self.get_infinitive() + "ed"

    def get_irregular(self):
        path = 'irverbs.txt'
        with open(path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        search = self.get_infinitive()
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
