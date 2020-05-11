import logging
from os import path

from AbstarctVerb import AbstractVerb, Person, Number, Tense


class SpanishVerb(AbstractVerb):

    def __init__(self, infinitive):
        super().__init__(infinitive)
        self.stem = self.get_infinitive()[:-2]
        self.ending = self.get_infinitive()[-2:]
        logging.info(self.get_stem())
        logging.info(self.ending)

    def morph(self, person, number, tense, genus):
        if tense == Tense.PAST.value:
            form = self.get_stem()['stem_past'] if self.get_stem() is not None else self.stem
            if number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    form += "i" if (self.stem == "s") else "e"
                elif person == Person.SECOND.value:
                    form += "iste"
                elif person == Person.THIRD.value:
                    form = form[:-1] + "z" if form[-1] == "c" else form
                    form += "e" if self.stem == "s" else "o"
            if number == Number.PLURAL.value:
                if person == Person.FIRST.value:
                    form += "imos"
                elif person == Person.SECOND.value:
                    form += "isteis"
                elif person == Person.THIRD.value:
                    form += "i" if form[-1] != "u" else ""
                    form += "eron"
        elif tense == Tense.PRESENT.value:
            form = self.stem
            if number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    form = form.rstrip("c")
                    if self.get_stem() is not None:
                        form += "go" if self.get_infinitive() != self.get_stem()['stem_future'] else "oy"
                elif person == Person.SECOND.value:
                    form = self.get_stem()['stem_present'] if self.get_stem() is not None else self.stem
                    form = "ere" + form if self.stem == "s" else form
                    form += "ás" if self.ending == "ar" else ("es" if self.stem != "s" else "")
                elif person == Person.THIRD.value:
                    form = self.get_stem()['stem_present'] if self.get_stem() is not None else self.stem
                    if self.stem != "s":
                        form += "á" if self.ending == "ar" else "e"
                    else:
                        form = "e" + form
            if number == Number.PLURAL.value:
                if person == Person.FIRST.value:
                    form += "a" if self.ending == "ar" else "o" if self.stem == "s" else "e"
                    form += "mos"
                elif person == Person.SECOND.value:
                    form += "á" if self.ending == "ar" else "o" if self.stem == "s" else "é"
                    form += "is"
                elif person == Person.THIRD.value:
                    form = self.get_stem()['stem_present'] if self.get_stem() is not None else self.stem
                    form += "á" if self.ending == "ar" else "o" if self.stem == "s" else "e"
                    form += "n"
        elif tense == Tense.FUTURE.value:
            form = self.get_infinitive() if self.get_stem() is None else self.get_stem()['stem_future']
            if number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    form += "é"
                elif person == Person.SECOND.value:
                    form += "ás"
                elif person == Person.THIRD.value:
                    form += "á"
            if number == Number.PLURAL.value:
                if person == Person.FIRST.value:
                    form += "emos"
                elif person == Person.SECOND.value:
                    form += "éis"
                elif person == Person.THIRD.value:
                    form += "án"
        return form

    def get_stem(self):
        ir_verb_table_path = path.join('langs', 'spanish', 'irverbs.csv')
        with open(ir_verb_table_path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        search = self.get_infinitive()
        for iverb in verbs_list:
            base = iverb["base_form"]
            if base.strip() == search.strip():
                return iverb
        return None
