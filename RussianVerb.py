from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus


class RussianVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
            if self._infinitive == "делать":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "делаю"
                    if person == Person.SECOND.value:
                        return "делаешь"
                    if person == Person.THIRD.value:
                        return "делает"
                elif number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "делаем"
                    if person == Person.SECOND.value:
                        return "делаете"
                    if person == Person.THIRD.value:
                        return "делают"
        if tense == Tense.PAST.value:
            if self._infinitive == "делать":
                if person == 1:
                    if number == Number.SINGULAR.value:
                        return "делал"
                    elif number == Number.PLURAL.value:
                        return "делали"
                if person == 2:
                    if number == Number.SINGULAR.value:
                        return "делал"
                    elif number == Number.PLURAL.value:
                        return "делали"
                if person == 3:
                    if number == Number.SINGULAR.value and Genus.MALE.value:
                        return "делал"
                    elif number == Number.SINGULAR.value and Genus.FEMALE.value:
                        return "делала"
                    elif number == Number.SINGULAR.value and Genus.MIDDLE.value:
                        return "делало"
                    elif number == Number.PLURAL.value:
                        return "делали"
        if tense == Tense.FUTURE.value:
            if self._infinitive == "делать":
                if person == 1:
                    if number == Number.SINGULAR.value:
                        return "буду " + self.get_infinitive()
                    elif number == Number.PLURAL.value:
                        return "будем " + self.get_infinitive()
                elif person == 2:
                    if number == Number.SINGULAR.value:
                        return "будешь " + self.get_infinitive()
                    elif number == Number.PLURAL.value:
                        return "будете " + self.get_infinitive()
                elif person == 3:
                    if number == Number.SINGULAR.value:
                        return "будет " + self.get_infinitive()
                    elif number == Number.PLURAL.value:
                        return "будут " + self.get_infinitive()
