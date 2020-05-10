from AbstarctVerb import AbstractVerb, Person, Number, Tense


class SpanishVerb(AbstractVerb):

    def morph(self, person, number, tense, genus):

        if tense == Tense.PAST.value:
            if self.infinitive == "ser":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "fui"
                    elif person == Person.SECOND.value:
                        return "fuiste"
                    elif person == Person.THIRD.value:
                        return "fue"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "fuimos"
                    elif person == Person.SECOND.value:
                        return "fuisteis"
                    elif person == Person.THIRD.value:
                        return "fueron"
        elif tense == Tense.PRESENT.value:
            if self.infinitive == "ser":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "soy"
                    elif person == Person.SECOND.value:
                        return "eres"
                    elif person == Person.THIRD.value:
                        return "es"
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "somos"
                    elif person == Person.SECOND.value:
                        return "sois"
                    elif person == Person.THIRD.value:
                        return "son"
        elif tense == Tense.FUTURE.value:
            if self.infinitive == "ser":
                return "será"
