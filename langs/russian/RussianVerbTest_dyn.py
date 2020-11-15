import csv
import unittest
from os import path, listdir

from langs.russian.RussianVerb import RussianVerb


# write tests
# write code
# refactor tests
# refactor code


class RussianVerbTest(unittest.TestCase):

    def test_get_infinitive(self):
        self.assertEqual("быть", RussianVerb("быть").get_infinitive())

    def test_get_pronouns(self):
        self.assertEqual("я", RussianVerb.get_pronoun(1, 1, 1))
        self.assertEqual("ты", RussianVerb.get_pronoun(2, 1, 1))
        self.assertEqual("он", RussianVerb.get_pronoun(3, 1, 1))
        self.assertEqual("она", RussianVerb.get_pronoun(3, 1, 2))
        self.assertEqual("оно", RussianVerb.get_pronoun(3, 1, 3))
        self.assertEqual("мы", RussianVerb.get_pronoun(1, 2, 1))
        self.assertEqual("вы", RussianVerb.get_pronoun(2, 2, 1))
        self.assertEqual("они", RussianVerb.get_pronoun(3, 2, 1))

    def test_get_verb_forms(self):
        test_verbs_path = path.join('test_verbs')
        files = listdir(test_verbs_path)
        print(files)
        for file in files:
            infinitive = file[:file.index('.')]
            with open(path.join('test_verbs', file), newline='\n') as verb_forms:
                forms_list = list(csv.reader(verb_forms, csv.unix_dialect, delimiter='\t'))
                for row, forms in enumerate(forms_list):
                    number = (row & 1) + 1
                    row += 1  # increment (i++ for C successors)
                    # 1 // 2 == 0      1 & 1 == 1
                    # 2 // 2 == 1      2 & 1 == 0
                    # 3 // 2 == 1      3 & 1 == 1
                    # 4 // 2 == 2      4 & 1 == 0
                    # 5 // 2 == 2      5 & 1 == 1
                    # 6 // 2 == 3      6 & 1 == 0
                    tense = (row // 2) + (row & 1)
                    #  8421
                    #  1101 & 0001 == 0001
                    #  1100 & 0001 == 0000
                    for person, form in enumerate(forms):
                        person += 1
                        # print(f"{infinitive} {tense}t{person}p{number}n: {form}")
                        self.assertEqual(form, RussianVerb(infinitive).morph(person, number, tense, 'M'))

        if __name__ == '__main__':
            unittest.main()
