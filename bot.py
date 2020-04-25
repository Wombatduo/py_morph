from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Verb import getVerb
from bot_settings import API_KEY, PROXY

def do_morph(bot, update):
    print(update.message)
    in_text = update.message.text
    args = in_text.split(' ')
    if len(args) != 2:
        update.message.reply_text("Точно?")
    verb = getVerb(args[0], args[1])
    # print(verb)
    if verb is None:
        update.message.reply_text("Это вапще на каком языке?")
    past = verb.morph(1, 1, 1, 1)
    present = verb.morph(1, 1, 2, 1)
    future = verb.morph(1, 1, 3, 1)
    reply = [past, present, future]
    reply = ['-' if v is None else v for v in reply]
    print(reply)
    update.message.reply_text(" / ".join(reply))


def greet_user(bot, update):
    text = "What do U want to morph today?\n(<lang> <infinitive>)"
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(API_KEY, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, do_morph))

    mybot.start_polling()
    mybot.idle()


main()
