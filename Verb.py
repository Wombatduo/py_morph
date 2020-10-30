from langs.english.EnglishVerb import EnglishVerb
from langs.spanish.SpanishVerb import SpanishVerb
from langs.german.GermanVerb import GermanVerb
from langs.russian.RussianVerb import RussianVerb


def getVerb(lang, infinitive):
    lang = lang.lower()
    if lang == 'eng':
        return EnglishVerb(infinitive)
    elif lang == 'esp':
        return SpanishVerb(infinitive)
    elif lang == 'ger':
        return GermanVerb(infinitive)
    elif lang == 'rus':
        return RussianVerb(infinitive)
    else:
        return None
