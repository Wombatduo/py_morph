from os import path

import requests, csv
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

    tenses = {
        Tense.PAST: "Прошлое",
        Tense.PRESENT: "Настоящее",
        Tense.FUTURE: "Будущее"
    }

    def __init__(self, infinitive):
        super().__init__(infinitive)
        self.ending = self.get_infinitive()[-2:]
        self.stem = self.get_infinitive()[:-2]
        self.is_reflexive = self.ending == "ся"

        self.is_perfect = False
        verbs_list = self.read_tsv_as_list('perfect.tsv')
        for verb in verbs_list:
            perfect = verb["perfect_form"]
            if perfect == self.get_infinitive().strip():
                self.perfect = perfect
                self.is_perfect = True
                self.simple = verb["simple_form"]

        if self.stem[-3:] in ['ова', 'ева']:  # гаголы 3 класса
            self.v_class = 3
        elif self.stem[-1] in ['а', 'ы']:  # глаголы 1 и 2 классов
            self.v_class = 1
        elif self.stem[-1] in ['е', 'о']:  # глаголы 1 и 2 классов
            self.v_class = 2
        elif self.stem[-2:] in ['ну']:  # гаголы 4 класса
            self.v_class = 4
        elif self.stem[-1] in ['и']:  # гаголы 5 класса
            self.v_class = 5
        else:
            self.v_class = None
        if self.v_class in range(1, 4):
            self.conjugation = 1
        else:
            self.conjugation = 2
        # logging.info(f'Stem {}',self.get_stem())
        # logging.info(self.ending)

    def morph(self, person, number, tense, genus):
        if self.is_reflexive:
            sverb = RussianVerb(self.get_infinitive()[:-2])
            sform = sverb.morph(person, number, tense, genus)
            if RussianVerb.is_vowel(sform[-1]):
                return sform + 'сь'
            return sform + 'ся'

        if tense == Tense.PRESENT.value:
            if self.is_perfect:
                simple_form = RussianVerb(self.simple)
                return simple_form.morph(person, number, tense, genus)

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
            form = self.add_personal_ending(form, number, person, tense)
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

            if (form[:1] in ["с", "о", "у", "п", "в"] and (form != self.get_infinitive())) or form[-2:] == 'да':
                if form[-2:] == 'да':
                    if person == Person.FIRST.value and number == Number.SINGULAR.value:
                        return form + 'м'
                    else:
                        if number == Number.SINGULAR.value:
                            form += 'с'
                        elif number == Number.PLURAL.value:
                            form += 'д'
                return self.add_personal_ending(form, number, person, tense)

            if form[-3:] == "аза":
                form = form[:-3] + "аж"

            if self.ending == "чь":
                if (number == Number.SINGULAR.value and person == Person.FIRST.value) or (
                        number == Number.PLURAL.value and person == Person.THIRD.value):
                    form = self.get_stem()['stem_past']
                form = "с" + self.add_personal_ending(form, number, person, tense)
            else:
                if self.get_infinitive() == "быть":
                    main_verb = ""
                else:
                    main_verb = " " + self.get_infinitive()
                auxiliary_verb = self.add_personal_ending("буд", number, person, tense)
                return auxiliary_verb + main_verb
            return form

    def add_personal_ending(self, form, number, person, tense):
        if number == Number.SINGULAR.value:
            if person == Person.FIRST.value:
                if form[-2:] == "ди":
                    form = form[:-2] + "ж"
                if form[-2:] == "си":
                    form = form[:-2] + "ш"
                form = self.add_1st_sing_3rd_plur_ending(form, tense)
            else:
                if self.conjugation == 1:
                    form += 'е'
                elif self.conjugation == 2:
                    form += 'и'
                # if form[-1:] not in ["и", "с"]:
                #     form += "е"
                if person == Person.SECOND.value:
                    # if self.conjugation == 1:
                    # if form[-1:] == 'с':
                    #     form = form[:-1]
                    form += "шь"
                if person == Person.THIRD.value:
                    form += "т"
        elif number == Number.PLURAL.value:
            if person == Person.THIRD.value:
                if form[-1:] in ["ч"]:
                    form = form[:-1] + "тя"
                if form[-2:] in ["ди", "си"]:
                    form = form[:-1] + "я"
                form = self.add_1st_sing_3rd_plur_ending(form, tense)
                form += "т"
                if form[-3:] in "рют":
                    form = form[:-2] + "ят"
                if form[-3:] in "чут":
                    form = form[:-2] + "ат"
            else:
                if form[-1:] in ["ч"]:
                    form = form[:-1] + "ти"
                if form.endswith("ад"):
                    form += "и"
                # if form[-1:] not in ["и"]:
                #     form += "е"
                if self.conjugation == 1:
                    form += 'е'
                elif self.conjugation == 2:
                    form += 'и'
                if person == Person.FIRST.value:
                    form += "м"
                if person == Person.SECOND.value:
                    form += "те"
        return form

    def add_1st_sing_3rd_plur_ending(self, form, tense):
        # if self.conjugation == 1:
        if form[-1:] in ["и"]:
            form = form[:-1]
        form_ending = self.get_stem()['stem_past'][-1:] if tense == Tense.PRESENT.value else form[-1:]
        # in ["ж", "ч", "ш", "щ", "г", "д", "н", "в", "м"]:
        if not RussianVerb.is_vowel(form_ending) and (
                (form_ending not in ['р'])):  # or RussianVerb.is_vowel(form[-2:-1])):
            form += 'у'
        elif form[-2:] in ['ля'] or form_ending not in ['я']:
            form += 'ю'
        return form

    @staticmethod
    def read_tsv_as_list(tsv):
        perfect_table_path = path.join(path.dirname(__file__), tsv)
        with open(perfect_table_path, newline='\n') as perfects_file:
            verbs_list = list(csv.DictReader(perfects_file, delimiter='\t'))
        return verbs_list

    @staticmethod
    def is_vowel(letter):
        if str(letter).lower() in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
            return True
        else:
            return False

    def get_stem(self):
        verbs_list = self.read_tsv_as_list('irverbs.tsv')
        for irverb in verbs_list:
            base = irverb["base_form"]
            if base.strip() == self.get_infinitive().strip():
                return irverb
        if self.v_class == 3:
            stem_present = self.stem[:-3] + 'у'
        elif self.v_class in [1, 3]:
            stem_present = self.stem
        elif self.v_class == 4:
            stem_present = self.stem[:-2] + 'н'
        elif self.v_class == 5:
            stem_present = self.stem[:-1]
        else:
            stem_present = self.stem

        return {'base_form': self.get_infinitive(),
                'stem_past': self.stem,
                'stem_present': stem_present,
                'stem_future': self.get_infinitive()}
