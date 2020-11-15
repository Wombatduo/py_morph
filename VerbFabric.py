from langs.english.EnglishVerb import EnglishVerb
from langs.spanish.SpanishVerb import SpanishVerb
from langs.german.GermanVerb import GermanVerb
from langs.russian.RussianVerb import RussianVerb


def get_verb(lang, infinitive):
    clazz = get_verb_class(lang)
    if clazz is None:
        return None
    return clazz(infinitive)


def get_verb_class(lang):
    lang = lang.lower()
    if lang == 'english':
        return EnglishVerb
    elif lang == 'spanish':
        return SpanishVerb
    elif lang == 'german':
        return GermanVerb
    elif lang == 'russian':
        return RussianVerb
    else:
        return None
