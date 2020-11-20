import requests
from bs4 import BeautifulSoup

from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus

verbs_source_url: str = "https://en.wikibooks.org/wiki/German/Grammar/Verbs"


class GermanVerb(AbstractVerb):

    @classmethod
    def get_top_100(cls):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        hundred_rus_verbs = requests.get(verbs_source_url, headers=headers)
        soup = BeautifulSoup(hundred_rus_verbs.content, features="html.parser")
        vbs_table = soup.find('div', {"id": "mw-content-text"}).find("div", {"class": "mw-parser-output"}).find("table")
        rows = vbs_table.find_all("tr")
        verb_list = []
        for i, row in enumerate(rows):
            cells = row.find_all("td")
            if (i > 2) and (len(cells) > 2):
                text = cells[1].find("b").get_text(strip=True)
                if not set("[~!@#$%^&*()_+{}\":;\']+$").intersection(text):
                    verb_list.append(text)
                if len(verb_list) > 99:
                    break
        return verb_list

    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: "ich", Genus.FEMALE: "ich", Genus.MIDDLE: "ich"},
            Number.PLURAL: {Genus.MALE: "wir", Genus.FEMALE: "wir", Genus.MIDDLE: "wir"}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: "du", Genus.FEMALE: "du", Genus.MIDDLE: "du"},
            Number.PLURAL: {Genus.MALE: "ihr", Genus.FEMALE: "ihr", Genus.MIDDLE: "ihr"}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: "er", Genus.FEMALE: "sie", Genus.MIDDLE: "es"},
            Number.PLURAL: {Genus.MALE: "sie", Genus.FEMALE: "sie", Genus.MIDDLE: "sie"}}}

    def morph(self, person, number, tense, genus):

        # Единственное число
        # Множественное число
        # 1-е
        # ich - я
        # wir – мы
        # Лицо говорящее
        # 2-е
        # du – ты
        # ihr - вы
        # Лицо, к которому обращена речь
        # 3-е
        # er, sie, es – он, она, оно
        # sie – они или Sie - Вы
        # Лицо или предмет, о котором идет речь

        if tense == Tense.PAST.value:
            if self.get_infinitive() == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "war"
                    elif person == Person.SECOND.value:
                        return "warst"
                    elif person == Person.THIRD.value:
                        return "war"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "waren"
                    elif person == Person.SECOND.value:
                        return "wart"
                    elif person == Person.THIRD.value:
                        return "waren"
        elif tense == Tense.PRESENT.value:
            if self.get_infinitive() == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "bin"
                    elif person == Person.SECOND.value:
                        return "bist"
                    elif person == Person.THIRD.value:
                        return "ist"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "sind"
                    elif person == Person.SECOND.value:
                        return "seid"
                    elif person == Person.THIRD.value:
                        return "sind"
        elif tense == Tense.FUTURE.value:
            if self.get_infinitive() == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "werde " + self.get_infinitive()
                    elif person == Person.SECOND.value:
                        return "wirst " + self.get_infinitive()
                    elif person == Person.THIRD.value:
                        return "wird " + self.get_infinitive()
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "werden " + self.get_infinitive()
                    elif person == Person.SECOND.value:
                        return "werdet " + self.get_infinitive()
                    elif person == Person.THIRD.value:
                        return "werden " + self.get_infinitive()
