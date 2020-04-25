from EnglishVerb import EnglishVerb
from SpanishVerb import SpanishVerb
from GermanVerb import GermanVerb
from RussianVerb import RussianVerb


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
