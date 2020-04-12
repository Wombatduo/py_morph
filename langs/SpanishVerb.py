from grammar.AbstarctVerb import AbstractVerb

from grammar.Grammar import Tense, Person, Number, Genus


class SpanishVerb(AbstractVerb):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: 'Yo', Genus.FEMALE: 'Yo', Genus.MIDDLE: 'Yo'},
            Number.PLURAL: {Genus.MALE: 'Nosotros', Genus.FEMALE: 'Nosotras', Genus.MIDDLE: 'Nosotros'}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: 'Tu', Genus.FEMALE: 'Tu', Genus.MIDDLE: 'Tu'},
            Number.PLURAL: {Genus.MALE: 'Vosotros', Genus.FEMALE: 'Vosotras', Genus.MIDDLE: 'Vosotros'}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: 'Él', Genus.FEMALE: 'Ella', Genus.MIDDLE: 'El'},
            Number.PLURAL: {Genus.MALE: 'Ellos', Genus.FEMALE: 'Ellas', Genus.MIDDLE: 'Ellos'}}
    }

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
