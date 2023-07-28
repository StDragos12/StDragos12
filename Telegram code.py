import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


API_TOKEN = "6043529654:AAEHq6ezso6eV76ko90H1tREI6hMg8cr2XA"

def start(update, context):
    update.message.reply_text("Hello! I am your bot. Send /help to see the list of available commands.")

def help_command(update, context):
    help_text = "Available commands:\n"
    help_text += "/start - Start the bot\n"
    help_text += "/help - Show this help message\n"
    help_text += "/info - Get bot information\n"
    help_text += "/temperature - Get the current temperature in Bucharest"
    update.message.reply_text(help_text)

def info(update, context):
    bot_info = "Bot Name: {}\nUsername: @{}\nID: {}".format(
        context.bot.name, context.bot.username, context.bot.id
    )
    update.message.reply_text(bot_info)

def get_temperature(update, context):
    city = "Bucharest"
    url = f"http://wttr.in/{city.replace(' ', '+')}?format=%t"

    response = requests.get(url)
    if response.status_code == 200:
        temperature = response.text.strip()
        update.message.reply_text(f"The current temperature in {city} is {temperature}\u00b0C.")
    else:
        update.message.reply_text("Sorry, unable to fetch the temperature at the moment.")

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("temperature", get_temperature))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
