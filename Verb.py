from EnglishVerb import EnglishVerb


def getVerb(lang, infinitive):
    if lang == 'eng':
        return EnglishVerb(infinitive)
    # elif lang == 'esp'
    #     return SpanishVerb(infinitive)
    # elif lang == 'rus'
    #     return RussianVerb(infinitive)
    else:
        return None
