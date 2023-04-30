import telebot

TOKEN = '6109306528:AAFprd-EPNflD_g3uWlrgbS-cukHYXJgyCY'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "WELCOME I AM CALCI_ERA")


@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message, """
    /start->Greeting
    /help->will give you all commands list
    If you want to use it as a calculator feel free to do so""")

@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "This cannot be evaluated"
    bot.reply_to(message, msg)


bot.polling()
