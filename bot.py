from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters
from telegram import ReplyKeyboardMarkup
from Verb import getVerb
from bot_settings import TELEGRAM_API_KEY, PROXY

chats = {}


def do_morph(bot, update):
    chat_id = update.message.chat.id
    print(update.message)
    in_text = update.message.text
    args = in_text.split(' ')
    if len(args) != 1:
        update.message.reply_text("Точно?")
    lang = chats.get(chat_id)
    verb = getVerb(lang, args[0])
    # # print(verb)
    # if verb is None:
    #     update.message.reply_text("Это вапще на каком языке?")
    past = verb.morph(1, 1, 1, 1)
    present = verb.morph(1, 1, 2, 1)
    future = verb.morph(1, 1, 3, 1)
    reply = [past, present, future]
    reply = ['-' if v is None else v for v in reply]
    print(reply)
    update.message.reply_text(" / ".join(reply))


def greet_user(bot, update):
    chat_id = update.message.chat.id
    if chats.get(chat_id):
        chats[chat_id] = "eng"
    text = "Hi! What do U want to morph today?\nJust type infinitive ;)"
    print(text)
    update.message.reply_text(text)


def show_lang_keyboard(bot, update):
    print("/lang")
    lang_keyboard = ReplyKeyboardMarkup([["English", "Espanol"], ["Deutsche", "Русский"]])
    update.message.reply_text("выберите язык", reply_markup=lang_keyboard)


def switch_lang(bot, update):
    print(update.message)
    text = update.message.text
    lang = get_lang_by_text(text)
    chat_id = update.message.chat.id
    chats[chat_id] = lang
    print("switch to " + lang)
    print(str(chats))


def get_lang_by_text(text):
    if text == "English":
        lang = "eng"
    elif text == "Espanol":
        lang = "esp"
    elif text == "Deutsche":
        lang = "ger"
    elif text == "Русский":
        lang = "rus"
    return lang


def main():
    mybot = Updater(TELEGRAM_API_KEY
                    , request_kwargs=PROXY
                    )

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("lang", show_lang_keyboard))
    dp.add_handler(RegexHandler("^(English|eng|Eng|ENG)$", switch_lang))
    dp.add_handler(RegexHandler("^(Espanol|esp|Esp|ESP)$", switch_lang))
    dp.add_handler(RegexHandler("^(Deutsche|ger|Ger|GER)$", switch_lang))
    dp.add_handler(RegexHandler("^(Русский|rus|Rus|RUS)$", switch_lang))
    dp.add_handler(MessageHandler(Filters.text, do_morph))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
