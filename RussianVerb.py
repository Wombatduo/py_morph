from AbstarctVerb import AbstractVerb, Person, Number, Tense, Genus


class RussianVerb(AbstractVerb):
    pronouns = {
        Person.FIRST: {
            Number.SINGULAR: {Genus.MALE: "я",   Genus.FEMALE: "я", Genus.MIDDLE: "я"},
            Number.PLURAL: {Genus.MALE: "мы", Genus.FEMALE: "мы", Genus.MIDDLE: "мы"}},
        Person.SECOND: {
            Number.SINGULAR: {Genus.MALE: "ты", Genus.FEMALE: "ты", Genus.MIDDLE: "ты"},
            Number.PLURAL: {Genus.MALE: "вы", Genus.FEMALE: "вы", Genus.MIDDLE: "вы"}},
        Person.THIRD: {
            Number.SINGULAR: {Genus.MALE: "он", Genus.FEMALE: "она", Genus.MIDDLE: "оно"},
            Number.PLURAL: {Genus.MALE: "они", Genus.FEMALE: "они", Genus.MIDDLE: "они"}}
    }
    def morph(self, person, number, tense, genus):

        if tense == Tense.PRESENT.value:
                if number == Number.SINGULAR.value:
                    if person == Person.FIRST.value:
                        return self.change_ending_with("ю")
                    if person == Person.SECOND.value:
                        return self.change_ending_with("ешь")
                    if person == Person.THIRD.value:
                        return self.change_ending_with("ет")
                elif number == Number.PLURAL.value:
                    if person == Person.FIRST.value:
                        return self.change_ending_with("ем")
                    if person == Person.SECOND.value:
                        return self.change_ending_with("ете")
                    if person == Person.THIRD.value:
                        return self.change_ending_with("ют")
        if tense == Tense.PAST.value:
                if person == 1:
                    if number == Number.SINGULAR.value:
                        return self.change_ending_with("л")
                    elif number == Number.PLURAL.value:
                        return self.change_ending_with("ли")
                if person == 2:
                    if number == Number.SINGULAR.value:
                        return self.change_ending_with("л")
                    elif number == Number.PLURAL.value:
                        return self.change_ending_with("ли")
                if person == 3:
                    if number == Number.SINGULAR.value and Genus.MALE.value:
                        return self.change_ending_with("л")
                    elif number == Number.SINGULAR.value and Genus.FEMALE.value:
                        return self.change_ending_with("ла")
                    elif number == Number.SINGULAR.value and Genus.MIDDLE.value:
                        return self.change_ending_with("ло")
                    elif number == Number.PLURAL.value:
                        return self.change_ending_with("ли")
        if tense == Tense.FUTURE.value:
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

    def change_ending_with(self, ending):
        return self.get_stem() + ending

    def get_stem(self):
        return self.get_infinitive()[:-2]
