from os import path

import requests
from bs4 import BeautifulSoup

from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus

verbs_source_url: str = "http://dict.ruslang.ru/freq.php?act=show&dic=freq_v"


class RussianVerb(AbstractVerb):

    @classmethod
    def get_top_100(cls):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        hundred_rus_verbs = requests.get(verbs_source_url, headers=headers)
        soup = BeautifulSoup(hundred_rus_verbs.content, features="html.parser")
        verb_table = soup.find('table').find("table")
        rows = verb_table.find_all("tr")
        verb_list = []
        for i, row in enumerate(rows):
            cells = row.find_all("td")
            if i > 0 and len(cells) > 1:
                text = cells[1].get_text(strip=True)
                if not set("[~!@#$%^&*()_+{}\":;\']+$").intersection(text):
                    verb_list.append(text)
                if len(verb_list) > 99:
                    break
        return verb_list

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
        # logging.info(self.ending)

    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
            form = self.get_stem()['stem_present']
            # print(f"--- {self.stem}-{self.ending} ->> {form}")
            if self.get_stem()['base_form'] in ["быть"]:
                return form + self.ending
            if form[-3:] == "аза":
                form = form[:-3] + "аж"
            if self.ending == "чь":
                if (number == Number.SINGULAR.value and person == Person.FIRST.value) or (
                        number == Number.PLURAL.value and person == Person.THIRD.value):
                    form = self.get_stem()['stem_past']
            # if (number == Number.SINGULAR.value and person == Person.FIRST.value and form[-2:] == "ди"):
            #     form = form[:-2] + "ж"
            form = self.add_personal_ending(form, number, person)
            return form

        if tense == Tense.PAST.value:
            form = self.get_stem()['stem_past']
            if self.ending == "чь":
                if number == Number.PLURAL.value:
                    form += "ли"
            else:
                if number == Number.SINGULAR.value:
                    if form[-1] == 'ш':
                        form += 'е'
                    form += 'л'
                    if genus == Genus.FEMALE.value:
                        form += "а"
                    elif genus == Genus.MIDDLE.value:
                        form += "о"
                elif number == Number.PLURAL.value:
                    form += "ли"
            return form

        if tense == Tense.FUTURE.value:
            form = self.get_stem()['stem_future']
            stem_ending = form[-3:]
            if stem_ending == "аза":
                form = form[:-3] + "аж"
            prefix = self.get_prefix(form)
            if prefix in ["с", "о", "у", "п"] and form != self.get_infinitive():
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
                if form[-2:] == "ди":
                    form = form[:-2] + "ж"
                form = RussianVerb.add_1st_sing_3rd_plur_ending(form)
            else:
                if not form[-1:] in ["и"]:
                    form += "е"
                if person == Person.SECOND.value:
                    form += "шь"
                if person == Person.THIRD.value:
                    form += "т"
        elif number == Number.PLURAL.value:
            if person == Person.THIRD.value:
                if form[-1:] in ["ч"]:
                    form = form[:-1] + "тя"
                if form[-2:] in ["ди"]:
                    form = form[:-1] + "я"
                form = RussianVerb.add_1st_sing_3rd_plur_ending(form)
                form += "т"
                if form[-3:] in "рют":
                    form = form[:-2] + "ят"
            else:
                if form[-1:] in ["ч"]:
                    form = form[:-1] + "ти"
                if not form[-1:] in ["и"]:
                    form += "е"
                if person == Person.FIRST.value:
                    form += "м"
                if person == Person.SECOND.value:
                    form += "те"
        return form

    @staticmethod
    def add_1st_sing_3rd_plur_ending(form):
        if form[-1:] in ["и"]:
            form = form[:-1]
        form_ending = form[-1:]
        # in ["ж", "ч", "ш", "щ", "г", "д", "н", "в", "м"]:
        if not RussianVerb.is_vowel(form_ending) and form_ending != 'р':
            form += "у"
        elif form_ending != "я":
            form += "ю"
        return form

    @staticmethod
    def is_vowel(letter):
        if str(letter).lower() in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
            return True
        else:
            return False

    def get_stem(self):
        stem = self.stem
        ir_verb_table_path = path.join(path.dirname(__file__), 'irverbs.tsv')
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
