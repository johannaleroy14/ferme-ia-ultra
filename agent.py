from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)

# Ton token Telegram Bot
TELEGRAM_TOKEN = "7316577234:AAG1lDOcnJoXuvOaCJvsgWn_-VqzIXtzXLo"

bot = Bot(token=TELEGRAM_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("Salut ! Ferme IA Ultra est en ligne et prête à fonctionner.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

@app.route("/")
def home():
    return "Ferme IA Ultra est en ligne !"

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
