from flask import Flask, request
import telegram
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Ferme IA Ultra OK"

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    message = data.get("message", "Aucune donnée reçue.")
    bot.send_message(chat_id=CHAT_ID, text=message)
    return "Envoyé"

if __name__ == '__main__':
    app.run()
