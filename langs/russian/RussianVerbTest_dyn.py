import csv
import unittest
from os import path, listdir


class RussianVerbTest(unittest.TestCase):

    def test_get_pronouns(self):
        test_verbs_path = path.join('test_verbs')
        files = listdir(test_verbs_path)

        print(files)
        for file in files:
            tense = 1
            number = 2
            with open(path.join('test_verbs', file), newline='\n') as verb_forms:
                forms_list = list(csv.reader(verb_forms, csv.unix_dialect, delimiter='\t'))
                for forms in forms_list:
                    for p, form in enumerate(forms):
                        if p == 0:
                            if number == 2:
                                number = 1
                            else:
                                number = 2
                        for e in range(1, 18):
                            tense = tense + 1
                            if tense <= 6:
                                tense = 1
                            elif 6 <= tense <= 12:
                                tense = 2
                            else:
                                tense = 3
                        p = p + 1
                        print(tense, p, number, form)

        if __name__ == '__main__':
            unittest.main()
