from os import path

import requests
from bs4 import BeautifulSoup

from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus

verbs_source_url: str = "https://www.wordexample.com/list/most-common-verbs-english"


class EnglishVerb(AbstractVerb):

    @classmethod
    def get_top_100(cls):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        hundred_rus_verbs = requests.get(verbs_source_url, headers=headers)
        soup = BeautifulSoup(hundred_rus_verbs.content, features="html.parser")
        verb_table = soup.find("div", {"id": "wordexample-word-list"}).find("table").find("tbody")
        rows = verb_table.find_all("tr")
        verb_list = []
        for i, row in enumerate(rows):
            cells = row.find_all("td")
            text = cells[0].find("span").get_text(strip=True)
            if not set("[~!@#$%^&*()_+{}\":;\']+$").intersection(text):
                verb_list.append(text)
            if len(verb_list) > 99:
                break
        return verb_list

    default_verb = 'be'

    def morph(self, person, number, tense, genus):

        if self.is_irregular:
            if tense == Tense.PAST.value:
                past_simple = self.get_irregular()["past simple"]
                if "/" in past_simple:
                    if number == Number.SINGULAR.value and (
                            person != Person.SECOND.value or self.get_infinitive() != 'be'):
                        past_simple = past_simple.split("/", 1)[0]
                    elif number == Number.PLURAL.value or (
                            person == Person.SECOND.value and self.get_infinitive() == 'be'):
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
            elif tense == 5:
                return "am " + self.get_infinitive() + "ing"
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
            elif tense == 5:
                return "am " + self.get_infinitive() + "ing"

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
        if self.get_infinitive()[-1] == 'y':
            return self.get_infinitive()[0:-1] + "ied"
        return self.get_infinitive() + "ed"

    def get_irregular(self):
        ir_verb_table_path = path.join(path.dirname(__file__), 'irverbs.txt')
        with open(ir_verb_table_path, newline='\n') as irregular_verbs:
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

    @staticmethod
    def is_vovel(letter):
        if str(letter).lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False

    @property
    def is_irregular(self):
        if self.get_irregular() is not None:
            return True
        return False
