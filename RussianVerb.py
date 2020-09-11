import logging
from os import path

from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus


class RussianVerb(AbstractVerb):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: "я", Genus.FEMALE: "я", Genus.MIDDLE: "я"},
            Number.PLURAL: {Genus.MALE: "мы", Genus.FEMALE: "мы", Genus.MIDDLE: "мы"}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: "ты", Genus.FEMALE: "ты", Genus.MIDDLE: "ты"},
            Number.PLURAL: {Genus.MALE: "вы", Genus.FEMALE: "вы", Genus.MIDDLE: "вы"}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: "он", Genus.FEMALE: "она", Genus.MIDDLE: "оно"},
            Number.PLURAL: {Genus.MALE: "они", Genus.FEMALE: "они", Genus.MIDDLE: "они"}}
    }

    def __init__(self, infinitive):
        super().__init__(infinitive)
        self.stem = self.get_infinitive()[:-2]
        self.ending = self.get_infinitive()[-2:]
        # logging.info(f'Stem {}',self.get_stem())
        logging.info(self.ending)

    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
            form = self.get_stem()['stem_present']
            if self.ending == "чь":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        form += "гу"
                    if person == Person.SECOND.value:
                        form += "жешь"
                    if person == Person.THIRD.value:
                        form += "жет"
                elif number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        form += "жем"
                    if person == Person.SECOND.value:
                        form += "жете"
                    if person == Person.THIRD.value:
                        form += "гут"

            elif form == "ес":
                form += "ть"
            elif number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    form += "ю"
                if person == Person.SECOND.value:
                    form += "ешь"
                if person == Person.THIRD.value:
                    form += "ет"
            elif number == Number.PLURAL.value:
                if person == Person.FIRST.value:
                    form += "ем"
                if person == Person.SECOND.value:
                    form += "ете"
                if person == Person.THIRD.value:
                    form += "ют"
            return form

        if tense == Tense.PAST.value:
            form = self.get_stem()['stem_past']
            if self.ending == "чь":
                form += "г"
            elif person == 1:
                if number == Number.SINGULAR.value:
                    form += "л"
                elif number == Number.PLURAL.value:
                    form += "ли"
            elif person == 2:
                if number == Number.SINGULAR.value:
                    form += "л"
                elif number == Number.PLURAL.value:
                    form += "ли"
            elif person == 3:
                if number == Number.SINGULAR.value and Genus.MALE.value:
                    form += "л"
                elif number == Number.SINGULAR.value and Genus.FEMALE.value:
                    form += "ла"
                elif number == Number.SINGULAR.value and Genus.MIDDLE.value:
                    form += "ло"
                elif number == Number.PLURAL.value:
                    form += "ли"
            return form

        if tense == Tense.FUTURE.value:
            form = self.get_stem()['stem_past']
            if self.ending == "чь":
                form = "с" + form
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        form += "гу"
                    if person == Person.SECOND.value:
                        form += "жешь"
                    if person == Person.THIRD.value:
                        form += "жет"
                elif number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        form += "жем"
                    if person == Person.SECOND.value:
                        form += "жете"
                    if person == Person.THIRD.value:
                        form += "гут"
            else:
                if self.get_infinitive() == "быть":
                    main_verb = ""
                else:
                    main_verb = " " + self.get_infinitive()
                if person == 1:
                    if number == Number.SINGULAR.value:
                        return "буду" + main_verb
                    elif number == Number.PLURAL.value:
                        return "будем" + main_verb
                elif person == 2:
                    if number == Number.SINGULAR.value:
                        return "будешь" + main_verb
                    elif number == Number.PLURAL.value:
                        return "будете" + main_verb
                elif person == 3:
                    if number == Number.SINGULAR.value:
                        return "будет" + main_verb
                    elif number == Number.PLURAL.value:
                        return "будут" + main_verb
            return form

    def get_stem(self):
        stem = self.stem
        ir_verb_table_path = path.join('langs', 'russian', 'irverbs.csv')
        with open(ir_verb_table_path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        for irverb in verbs_list:
            base = irverb["base_form"]
            if base.strip() == self.get_infinitive().strip():
                return irverb
        return {'base_form': self.get_infinitive(),
                'stem_past': stem,
                'stem_present': stem,
                'stem_future': self.get_infinitive()}
