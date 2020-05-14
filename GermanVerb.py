from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus


class GermanVerb(AbstractVerb):

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
            if self._infinitive == "sein":
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
            if self._infinitive == "sein":
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
            if self._infinitive == "sein":
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
