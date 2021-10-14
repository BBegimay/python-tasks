import requests
import telebot
import json

TOKEN = "1972891747:AAE2QNvgCUGgqV6Pf9GWD2-S9hj83E0TVTc"
bot = telebot.TeleBot(TOKEN)

keys = {'US Dollar': 'USD', 'Euro': 'EUR', 'Russian Rubble': "RUB"}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = 'To get started, enter the command in the following order:\n<currency name>\<currency to transfer>\<amount>\n<list of all available currencies>: /values'
    bot.reply_to(message,   text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies: '
    for key in keys.keys():
        text = text + "\n" + keys[key] + ": " +key
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
   # Format is: EUR RUB 1
    try:
        quote, base, amount = message.text.split(' ')
        r = requests.get(f"https://v6.exchangerate-api.com/v6/b2cfb790ade9cf90bfecaa20/pair/%s/%s" % (quote, base))
        rate = json.loads(r.content)["conversion_rate"]
        text = f'Price {amount} {quote} in {base} - {round(float(rate) * float(amount), 2)}'
        bot.reply_to(message, text)
    except:
        bot.reply_to(message, "Wrong format. Please send message as\nEUR RUB 100")


bot.infinity_polling()