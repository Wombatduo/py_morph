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
            if form[-3:] == "аза":
                form = form[:-3] + "аж"
            if self.ending == "чь":
                if (number == Number.SINGULAR.value and person == Person.FIRST.value) or (
                        number == Number.PLURAL.value and person == Person.THIRD.value):
                    form = self.get_stem()['stem_past']
                form = self.add_personal_ending(form, number, person)
            elif form == "ес":
                form += "ть"
            elif number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    if form[-1:] in ["ж", "ч", "ш", "щ"]:
                        form += "у"
                    else:
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
                    if form[-1:] in ["ж", "ч", "ш", "щ"]:
                        form += "у"
                    else:
                        form += "ю"
                    form += "т"

            return form

        if tense == Tense.PAST.value:
            form = self.get_stem()['stem_past']
            if self.ending == "чь":
                if number == Number.PLURAL.value:
                    form += "ли"
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
            form = self.get_stem()['stem_future']
            stem_ending = form[-3:]
            if stem_ending == "аза":
                form = form[:-3] + "аж"
            prefix = self.get_prefix(form)
            if prefix in ["с", "о", "у"]:
                return self.add_personal_ending(form, number, person)
            if self.ending == "чь":
                if (number == Number.SINGULAR.value and person == Person.FIRST.value) or (
                        number == Number.PLURAL.value and person == Person.THIRD.value):
                    form = self.get_stem()['stem_past']
                form = "с" + self.add_personal_ending(form, number, person)
            else:
                if self.get_infinitive() == "быть":
                    main_verb = ""
                else:
                    main_verb = " " + self.get_infinitive()
                auxiliary_verb = self.add_personal_ending("буд", number, person)
                return auxiliary_verb + main_verb
            return form

    @staticmethod
    def get_prefix(form):
        return form[:1]

    @staticmethod
    def add_personal_ending(form, number, person):
        if number == Number.SINGULAR.value:
            if person == Person.FIRST.value:
                form += "у"
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
                form += "ут"
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
                'stem_future': stem}
