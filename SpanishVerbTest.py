import unittest
from SpanishVerb import SpanishVerb


class SpanishVerbTest(unittest.TestCase):

    def test_get_infinitive_for_ser(self):
        self.assertEqual("ser", SpanishVerb("ser").get_infinitive())

    def test_ser_should_be_different_for_3_persons_past(self):
        self.assertEqual("fui",    SpanishVerb("ser").morph(1, 1, 1, 'M'))
        self.assertEqual("fuiste", SpanishVerb("ser").morph(2, 1, 1, 'M'))
        self.assertEqual("fue",    SpanishVerb("ser").morph(3, 1, 1, 'M'))
        self.assertEqual("fuimos",   SpanishVerb("ser").morph(1, 2, 1, 'M'))
        self.assertEqual("fuisteis", SpanishVerb("ser").morph(2, 2, 1, 'M'))
        self.assertEqual("fueron",   SpanishVerb("ser").morph(3, 2, 1, 'M'))

    def test_ser_should_be_different_for_3_persons_present(self):
        self.assertEqual("soy",  SpanishVerb("ser").morph(1, 1, 2, 'M'))
        self.assertEqual("eres", SpanishVerb("ser").morph(2, 1, 2, 'M'))
        self.assertEqual("es",   SpanishVerb("ser").morph(3, 1, 2, 'M'))
        self.assertEqual("somos", SpanishVerb("ser").morph(1, 2, 2, 'M'))
        self.assertEqual("sois",  SpanishVerb("ser").morph(2, 2, 2, 'M'))
        self.assertEqual("son",   SpanishVerb("ser").morph(3, 2, 2, 'M'))

    def test_ser_should_be_different_for_3_persons_future(self):
        self.assertEqual("seré",  SpanishVerb("ser").morph(1, 1, 3, 'M'))
        self.assertEqual("serás", SpanishVerb("ser").morph(2, 1, 3, 'M'))
        self.assertEqual("será",  SpanishVerb("ser").morph(3, 1, 3, 'M'))
        self.assertEqual("seremos", SpanishVerb("ser").morph(1, 2, 3, 'M'))
        self.assertEqual("seréis",  SpanishVerb("ser").morph(2, 2, 3, 'M'))
        self.assertEqual("serán",   SpanishVerb("ser").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_estar(self):
        self.assertEqual("estar", SpanishVerb("estar").get_infinitive())

    def test_estar_should_be_different_for_3_persons_past(self):
        self.assertEqual("estuve",    SpanishVerb("estar").morph(1, 1, 1, 'M'))
        self.assertEqual("estuviste", SpanishVerb("estar").morph(2, 1, 1, 'M'))
        self.assertEqual("estuvo",    SpanishVerb("estar").morph(3, 1, 1, 'M'))
        self.assertEqual("estuvimos",   SpanishVerb("estar").morph(1, 2, 1, 'M'))
        self.assertEqual("estuvisteis", SpanishVerb("estar").morph(2, 2, 1, 'M'))
        self.assertEqual("estuvieron",  SpanishVerb("estar").morph(3, 2, 1, 'M'))

    def test_estar_should_be_different_for_3_persons_present(self):
        self.assertEqual("estoy", SpanishVerb("estar").morph(1, 1, 2, 'M'))
        self.assertEqual("estás", SpanishVerb("estar").morph(2, 1, 2, 'M'))
        self.assertEqual("está",  SpanishVerb("estar").morph(3, 1, 2, 'M'))
        self.assertEqual("estamos", SpanishVerb("estar").morph(1, 2, 2, 'M'))
        self.assertEqual("estáis", SpanishVerb("estar").morph(2, 2, 2, 'M'))
        self.assertEqual("están",  SpanishVerb("estar").morph(3, 2, 2, 'M'))

    def test_estar_should_be_different_for_3_persons_future(self):
        self.assertEqual("estaré",  SpanishVerb("estar").morph(1, 1, 3, 'M'))
        self.assertEqual("estarás", SpanishVerb("estar").morph(2, 1, 3, 'M'))
        self.assertEqual("estará",  SpanishVerb("estar").morph(3, 1, 3, 'M'))
        self.assertEqual("estaremos",  SpanishVerb("estar").morph(1, 2, 3, 'M'))
        self.assertEqual("estaréis", SpanishVerb("estar").morph(2, 2, 3, 'M'))
        self.assertEqual("estarán",  SpanishVerb("estar").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_hacer(self):
        self.assertEqual("hacer", SpanishVerb("hacer").get_infinitive())

    def test_hacer_should_be_different_for_3_persons_past(self):
        self.assertEqual("hice",    SpanishVerb("hacer").morph(1, 1, 1, 'M'))
        self.assertEqual("hiciste", SpanishVerb("hacer").morph(2, 1, 1, 'M'))
        self.assertEqual("hizo",    SpanishVerb("hacer").morph(3, 1, 1, 'M'))
        self.assertEqual("hicimos",   SpanishVerb("hacer").morph(1, 2, 1, 'M'))
        self.assertEqual("hicisteis", SpanishVerb("hacer").morph(2, 2, 1, 'M'))
        self.assertEqual("hicieron",  SpanishVerb("hacer").morph(3, 2, 1, 'M'))

    def test_hacer_should_be_different_for_3_persons_present(self):
        self.assertEqual("hago", SpanishVerb("hacer").morph(1, 1, 2, 'M'))
        self.assertEqual("haces", SpanishVerb("hacer").morph(2, 1, 2, 'M'))
        self.assertEqual("hace",  SpanishVerb("hacer").morph(3, 1, 2, 'M'))
        self.assertEqual("hacemos", SpanishVerb("hacer").morph(1, 2, 2, 'M'))
        self.assertEqual("hacéis", SpanishVerb("hacer").morph(2, 2, 2, 'M'))
        self.assertEqual("hacen",  SpanishVerb("hacer").morph(3, 2, 2, 'M'))

    def test_hacer_should_be_different_for_3_persons_future(self):
        self.assertEqual("haré",  SpanishVerb("hacer").morph(1, 1, 3, 'M'))
        self.assertEqual("harás", SpanishVerb("hacer").morph(2, 1, 3, 'M'))
        self.assertEqual("hará",  SpanishVerb("hacer").morph(3, 1, 3, 'M'))
        self.assertEqual("haremos",  SpanishVerb("hacer").morph(1, 2, 3, 'M'))
        self.assertEqual("haréis", SpanishVerb("hacer").morph(2, 2, 3, 'M'))
        self.assertEqual("harán",  SpanishVerb("hacer").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_tener(self):
        self.assertEqual("tener", SpanishVerb("tener").get_infinitive())

    def test_tener_should_be_different_for_3_persons_past(self):
        self.assertEqual("tuve",    SpanishVerb("tener").morph(1, 1, 1, 'M'))
        self.assertEqual("tuviste", SpanishVerb("tener").morph(2, 1, 1, 'M'))
        self.assertEqual("tuvo",    SpanishVerb("tener").morph(3, 1, 1, 'M'))
        self.assertEqual("tuvimos",   SpanishVerb("tener").morph(1, 2, 1, 'M'))
        self.assertEqual("tuvisteis", SpanishVerb("tener").morph(2, 2, 1, 'M'))
        self.assertEqual("tuvieron",  SpanishVerb("tener").morph(3, 2, 1, 'M'))

    def test_tener_should_be_different_for_3_persons_present(self):
        self.assertEqual("tengo", SpanishVerb("tener").morph(1, 1, 2, 'M'))
        self.assertEqual("tienes", SpanishVerb("tener").morph(2, 1, 2, 'M'))
        self.assertEqual("tiene",  SpanishVerb("tener").morph(3, 1, 2, 'M'))
        self.assertEqual("tenemos", SpanishVerb("tener").morph(1, 2, 2, 'M'))
        self.assertEqual("tenéis", SpanishVerb("tener").morph(2, 2, 2, 'M'))
        self.assertEqual("tienen",  SpanishVerb("tener").morph(3, 2, 2, 'M'))

    def test_tener_should_be_different_for_3_persons_future(self):
        self.assertEqual("tendré",  SpanishVerb("tener").morph(1, 1, 3, 'M'))
        self.assertEqual("tendrás", SpanishVerb("tener").morph(2, 1, 3, 'M'))
        self.assertEqual("tendrá",  SpanishVerb("tener").morph(3, 1, 3, 'M'))
        self.assertEqual("tendremos",  SpanishVerb("tener").morph(1, 2, 3, 'M'))
        self.assertEqual("tendréis", SpanishVerb("tener").morph(2, 2, 3, 'M'))
        self.assertEqual("tendrán",  SpanishVerb("tener").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_haber(self):
        self.assertEqual("haber", SpanishVerb("haber").get_infinitive())

    def test_haber_should_be_different_for_3_persons_past(self):
        self.assertEqual("hube",    SpanishVerb("haber").morph(1, 1, 1, 'M'))
        self.assertEqual("hubiste", SpanishVerb("haber").morph(2, 1, 1, 'M'))
        self.assertEqual("hubo",    SpanishVerb("haber").morph(3, 1, 1, 'M'))
        self.assertEqual("hubimos",   SpanishVerb("haber").morph(1, 2, 1, 'M'))
        self.assertEqual("hubisteis", SpanishVerb("haber").morph(2, 2, 1, 'M'))
        self.assertEqual("hubieron",  SpanishVerb("haber").morph(3, 2, 1, 'M'))

    def test_haber_should_be_different_for_3_persons_present(self):
        self.assertEqual("he", SpanishVerb("haber").morph(1, 1, 2, 'M'))
        self.assertEqual("has", SpanishVerb("haber").morph(2, 1, 2, 'M'))
        self.assertEqual("ha",  SpanishVerb("haber").morph(3, 1, 2, 'M'))
        self.assertEqual("hemos", SpanishVerb("haber").morph(1, 2, 2, 'M'))
        self.assertEqual("habéis", SpanishVerb("haber").morph(2, 2, 2, 'M'))
        self.assertEqual("han",  SpanishVerb("haber").morph(3, 2, 2, 'M'))

    def test_haber_should_be_different_for_3_persons_future(self):
        self.assertEqual("habré",  SpanishVerb("haber").morph(1, 1, 3, 'M'))
        self.assertEqual("habrás", SpanishVerb("haber").morph(2, 1, 3, 'M'))
        self.assertEqual("habrá",  SpanishVerb("haber").morph(3, 1, 3, 'M'))
        self.assertEqual("habremos",  SpanishVerb("haber").morph(1, 2, 3, 'M'))
        self.assertEqual("habréis", SpanishVerb("haber").morph(2, 2, 3, 'M'))
        self.assertEqual("habrán",  SpanishVerb("haber").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_poder(self):
        self.assertEqual("poder", SpanishVerb("poder").get_infinitive())

    def test_poder_should_be_different_for_3_persons_past(self):
        self.assertEqual("pude",    SpanishVerb("poder").morph(1, 1, 1, 'M'))
        self.assertEqual("pudiste", SpanishVerb("poder").morph(2, 1, 1, 'M'))
        self.assertEqual("pudo",    SpanishVerb("poder").morph(3, 1, 1, 'M'))
        self.assertEqual("pudimos",   SpanishVerb("poder").morph(1, 2, 1, 'M'))
        self.assertEqual("pudisteis", SpanishVerb("poder").morph(2, 2, 1, 'M'))
        self.assertEqual("pudieron",  SpanishVerb("poder").morph(3, 2, 1, 'M'))

    def test_poder_should_be_different_for_3_persons_present(self):
        self.assertEqual("puedo", SpanishVerb("poder").morph(1, 1, 2, 'M'))
        self.assertEqual("puedes", SpanishVerb("poder").morph(2, 1, 2, 'M'))
        self.assertEqual("puede",  SpanishVerb("poder").morph(3, 1, 2, 'M'))
        self.assertEqual("podemos", SpanishVerb("poder").morph(1, 2, 2, 'M'))
        self.assertEqual("podéis", SpanishVerb("poder").morph(2, 2, 2, 'M'))
        self.assertEqual("pueden",  SpanishVerb("poder").morph(3, 2, 2, 'M'))

    def test_poder_should_be_different_for_3_persons_future(self):
        self.assertEqual("podré",  SpanishVerb("poder").morph(1, 1, 3, 'M'))
        self.assertEqual("podrás", SpanishVerb("poder").morph(2, 1, 3, 'M'))
        self.assertEqual("podrá",  SpanishVerb("poder").morph(3, 1, 3, 'M'))
        self.assertEqual("podremos",  SpanishVerb("poder").morph(1, 2, 3, 'M'))
        self.assertEqual("podréis", SpanishVerb("poder").morph(2, 2, 3, 'M'))
        self.assertEqual("podrán",  SpanishVerb("poder").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_decir(self):
        self.assertEqual("decir", SpanishVerb("decir").get_infinitive())

    def test_decir_should_be_different_for_3_persons_past(self):
        self.assertEqual("dije",    SpanishVerb("decir").morph(1, 1, 1, 'M'))
        self.assertEqual("dijiste", SpanishVerb("decir").morph(2, 1, 1, 'M'))
        self.assertEqual("dijo",    SpanishVerb("decir").morph(3, 1, 1, 'M'))
        self.assertEqual("dijimos",   SpanishVerb("decir").morph(1, 2, 1, 'M'))
        self.assertEqual("dijisteis", SpanishVerb("decir").morph(2, 2, 1, 'M'))
        self.assertEqual("dijeron",  SpanishVerb("decir").morph(3, 2, 1, 'M'))

    def test_decir_should_be_different_for_3_persons_present(self):
        self.assertEqual("digo", SpanishVerb("decir").morph(1, 1, 2, 'M'))
        self.assertEqual("dices", SpanishVerb("decir").morph(2, 1, 2, 'M'))
        self.assertEqual("dice",  SpanishVerb("decir").morph(3, 1, 2, 'M'))
        self.assertEqual("decimos", SpanishVerb("decir").morph(1, 2, 2, 'M'))
        self.assertEqual("decís", SpanishVerb("decir").morph(2, 2, 2, 'M'))
        self.assertEqual("dicen",  SpanishVerb("decir").morph(3, 2, 2, 'M'))

    def test_decir_should_be_different_for_3_persons_future(self):
        self.assertEqual("diré",  SpanishVerb("decir").morph(1, 1, 3, 'M'))
        self.assertEqual("dirás", SpanishVerb("decir").morph(2, 1, 3, 'M'))
        self.assertEqual("dirá",  SpanishVerb("decir").morph(3, 1, 3, 'M'))
        self.assertEqual("diremos",  SpanishVerb("decir").morph(1, 2, 3, 'M'))
        self.assertEqual("diréis", SpanishVerb("decir").morph(2, 2, 3, 'M'))
        self.assertEqual("dirán",  SpanishVerb("decir").morph(3, 2, 3, 'M'))


    def test_get_infinitive_for_ir(self):
        self.assertEqual("ir", SpanishVerb("ir").get_infinitive())

    def test_ir_should_be_different_for_3_persons_past(self):
        self.assertEqual("fui",    SpanishVerb("ir").morph(1, 1, 1, 'M'))
        self.assertEqual("fuiste", SpanishVerb("ir").morph(2, 1, 1, 'M'))
        self.assertEqual("fue",    SpanishVerb("ir").morph(3, 1, 1, 'M'))
        self.assertEqual("fuimos",   SpanishVerb("ir").morph(1, 2, 1, 'M'))
        self.assertEqual("fuisteis", SpanishVerb("ir").morph(2, 2, 1, 'M'))
        self.assertEqual("fueron",  SpanishVerb("ir").morph(3, 2, 1, 'M'))

    def test_ir_should_be_different_for_3_persons_present(self):
        self.assertEqual("voy", SpanishVerb("ir").morph(1, 1, 2, 'M'))
        self.assertEqual("vas", SpanishVerb("ir").morph(2, 1, 2, 'M'))
        self.assertEqual("va",  SpanishVerb("ir").morph(3, 1, 2, 'M'))
        self.assertEqual("vamos", SpanishVerb("ir").morph(1, 2, 2, 'M'))
        self.assertEqual("vais", SpanishVerb("ir").morph(2, 2, 2, 'M'))
        self.assertEqual("van",  SpanishVerb("ir").morph(3, 2, 2, 'M'))

    def test_ir_should_be_different_for_3_persons_future(self):
        self.assertEqual("iré",  SpanishVerb("ir").morph(1, 1, 3, 'M'))
        self.assertEqual("irás", SpanishVerb("ir").morph(2, 1, 3, 'M'))
        self.assertEqual("irá",  SpanishVerb("ir").morph(3, 1, 3, 'M'))
        self.assertEqual("iremos", SpanishVerb("ir").morph(1, 2, 3, 'M'))
        self.assertEqual("iréis",  SpanishVerb("ir").morph(2, 2, 3, 'M'))
        self.assertEqual("irán",   SpanishVerb("ir").morph(3, 2, 3, 'M'))

    def test_pronouns(self):
        self.assertEqual("Yo", SpanishVerb.get_pronoun(1, 1, 1))

if __name__ == '__main__':
    unittest.main()
