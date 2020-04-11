from grammar.AbstarctVerb import AbstractVerb

from grammar.Grammar import Tense, Person, Number, Genus


class RussianVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
            if person == 1:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делаю"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делаем"
            if person == 2:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делаешь"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делаете"
            if person == 3:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делает"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делают"
        if tense == Tense.PAST.value:
            if person == 1:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
            if person == 2:
                if number == Number.SINGULAR.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
            if person == 3:
                if number == Number.SINGULAR.value and Genus.MALE.value:
                    if self.infinitive == "делать":
                        return "делал"
                elif number == Number.SINGULAR.value and Genus.FEMALE.value:
                    if self.infinitive == "делала":
                        return "делал"
                elif number == Number.SINGULAR.value and Genus.MIDDLE.value:
                    if self.infinitive == "делало":
                        return "делал"
                elif number == Number.PLURAL.value:
                    if self.infinitive == "делать":
                        return "делали"
        if tense == Tense.FUTURE.value:
            if person == Person.FIRST.value:
                if number == Number.SINGULAR.value:
                    return "буду " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    return "будем " + self.get_infinitive()
            if person == Person.SECOND.value:
                if number == Number.SINGULAR.value:
                    return "будешь " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    return "будете " + self.get_infinitive()
            if person == Person.THIRD.value:
                if number == Number.SINGULAR.value:
                    return "будет " + self.get_infinitive()
                elif number == Number.PLURAL.value:
                    return "будут " + self.get_infinitive()
