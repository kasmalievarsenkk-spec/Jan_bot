
import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Привет ❤️ Я Жан. Давай поговорим."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(
        message,
        "Я тебя слушаю ❤️ Расскажи мне, что у тебя на душе."
    )

bot.infinity_polling()
