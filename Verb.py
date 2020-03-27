from EnglishVerb import EnglishVerb
from RussianVerb import RussianVerb


def getVerb(lang, infinitive):
    if lang == 'eng':
        return EnglishVerb(infinitive)
    # elif lang == 'esp'
    #     return SpanishVerb(infinitive)
    elif lang == 'rus':
        return RussianVerb(infinitive)
    else:
        return None
