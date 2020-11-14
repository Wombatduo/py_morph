from langs.english.EnglishVerb import EnglishVerb
from langs.spanish.SpanishVerb import SpanishVerb
from langs.german.GermanVerb import GermanVerb
from langs.russian.RussianVerb import RussianVerb


def get_verb(lang, infinitive):
    lang = lang.lower()
    clazz = get_verb_class(lang)
    if clazz is None:
        return None
    return clazz(infinitive)


def get_verb_class(lang):
    lang = lang.lower()
    if lang == 'eng':
        return EnglishVerb
    elif lang == 'esp':
        return SpanishVerb
    elif lang == 'ger':
        return GermanVerb
    elif lang == 'rus':
        return RussianVerb
    else:
        return None
