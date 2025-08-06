import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

# Récupère le token Telegram depuis les variables d'environnement
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

# Dispatcher pour gérer les commandes et messages
dispatcher = Dispatcher(bot, None, workers=0)

# Commande /start
def start(update, context):
    update.message.reply_text("Salut ! Bot en ligne.")

# Echo : répète tout message texte reçu
def echo(update, context):
    update.message.reply_text(update.message.text)

# Ajout des handlers au dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Route principale (test simple)
@app.route("/", methods=["GET"])
def home():
    return "Ferme IA Ultra est en ligne !"

# Route webhook pour recevoir les updates Telegram
@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    # Port dynamique pour Render (ou 10000 par défaut)
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)

