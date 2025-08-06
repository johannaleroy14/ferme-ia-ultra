from flask import Flask, request
import telegram
import os

app = Flask(__name__)

TOKEN = os.environ.get('TELEGRAM_TOKEN')

bot = telegram.Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f'Reçu: {text}')
    return 'ok'

@app.route('/')
def index():
    return 'Agent IA actif !'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)