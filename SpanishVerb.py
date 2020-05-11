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
            form = self.get_stem()['stem_past']
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
                    form += "i" if form[-1] not in ("u", "j") else ""
                    form += "eron"
        elif tense == Tense.PRESENT.value:
            stem_present = self.get_stem()['stem_present']
            form = stem_present
            if number == Number.SINGULAR.value:
                if person == Person.FIRST.value:
                    if abs(len(self.stem) - len(stem_present)) > 1:
                        form = stem_present + "e"
                    else:
                        form = stem_present if self.stem != "ten" else self.stem
                        form = form.rstrip("c")
                        form += "g" if not form.endswith("d") and form != stem_present else ""
                        form += "o"
                        form += "y" if self.stem == form.rstrip("o") else ""
                elif person == Person.SECOND.value:
                    form = "ere" + form if self.stem == "s" else form + "as" if form == "h" else form
                    form += "ás" if self.ending == "ar" else ("es" if self.stem not in ("hab", "s") else "")
                elif person == Person.THIRD.value:
                    if self.stem != "s":
                        form += "á" if self.ending == "ar" else "a" if self.stem == 'hab' else "e"
                    else:
                        form = "e" + form
            if number == Number.PLURAL.value:
                if person == Person.FIRST.value:
                    form = stem_present if (abs(len(self.stem) - len(stem_present)) > 1) else self.stem
                    form += "a" if self.ending == "ar" else "i" if self.ending == "ir" else "o" if self.stem == "s" else "e"
                    form += "mos"
                elif person == Person.SECOND.value:
                    form = self.stem
                    form += "ái" if self.ending == "ar" else "í" if self.ending == "ir" else "oi" if self.stem == "s" else "éi"
                    form += "s"
                elif person == Person.THIRD.value:
                    form += "á" if self.ending == "ar" else "o" if self.stem == "s" else "a" if form == "h" else "e"
                    form += "n"
        elif tense == Tense.FUTURE.value:
            form = self.get_stem()['stem_future']
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
        infinitive = self.get_infinitive()
        stem = self.stem
        ir_verb_table_path = path.join('langs', 'spanish', 'irverbs.csv')
        with open(ir_verb_table_path, newline='\n') as irregular_verbs:
            import csv
            verb_reader = csv.DictReader(irregular_verbs, delimiter='\t')
            verbs_list = list(verb_reader)
        for iverb in verbs_list:
            base = iverb["base_form"]
            if base.strip() == infinitive.strip():
                return iverb
        return {'base_form': infinitive, 'stem_past': stem, 'stem_present': stem, 'stem_future': infinitive}
