from AbstarctVerb import AbstractVerb, Person, Number, Tense


class GermanVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

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
