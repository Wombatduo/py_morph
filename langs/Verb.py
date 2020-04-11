from langs.EnglishVerb import EnglishVerb
from langs.SpanishVerb import SpanishVerb
from langs.GermanVerb import GermanVerb
from langs.RussianVerb import RussianVerb


def getVerb(lang, infinitive):
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
