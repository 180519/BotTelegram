import telebot
bot = telebot.TeleBot("6518419350:AAFBS-ukrhgIi423aNIFfUpobPadmhqVTzU")
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hola! Soy Inutibot! (Intelectual Utility BOT). Por lo pronto no puedo hacer mucho, pero poco a poco creceré.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "¡Yo te ayudo!")

@bot.message_handler(commands=['hola'])
def send_welcome(message):
	bot.reply_to(message, "¡Hola! Gracias por saludar!")


bot.infinity_polling()