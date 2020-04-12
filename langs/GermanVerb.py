from grammar.AbstarctVerb import AbstractVerb

from grammar.Grammar import Tense, Person, Number, Genus


class GermanVerb(AbstractVerb):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: 'Ich', Genus.FEMALE: 'Ich', Genus.MIDDLE: 'Ich'},
            Number.PLURAL: {Genus.MALE: 'Wir', Genus.FEMALE: 'Wir', Genus.MIDDLE: 'Wir'}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: 'Du', Genus.FEMALE: 'Du', Genus.MIDDLE: 'Du'},
            Number.PLURAL: {Genus.MALE: 'Ihr', Genus.FEMALE: 'Ihr', Genus.MIDDLE: 'Ihr'}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: 'Er', Genus.FEMALE: 'Sie', Genus.MIDDLE: 'Es'},
            Number.PLURAL: {Genus.MALE: 'Sie', Genus.FEMALE: 'Sie', Genus.MIDDLE: 'Sie'}}
    }

    def morph(self, person, number, tense, genus):

        if tense == Tense.PAST.value:
            if self.infinitive == "sein":
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
            if self.infinitive == "sein":
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
            if self.infinitive == "sein":
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return "wird " + self.get_infinitive()
                    elif person == Person.SECOND.value:
                        return "wird " + self.get_infinitive()
                    elif person == Person.THIRD.value:
                        return "wird " + self.get_infinitive()
                if number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return "wird " + self.get_infinitive()
                    elif person == Person.SECOND.value:
                        return "wird " + self.get_infinitive()
                    elif person == Person.THIRD.value:
                        return "wird " + self.get_infinitive()
