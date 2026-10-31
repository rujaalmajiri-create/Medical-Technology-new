import os
from flask import Flask
from threading import Thread
import telebot

# --- إعدادات سيرفر الويب الوهمي للبقاء 24/7 ---
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# --- كود البوت ---
TOKEN = "9100262932:AAHUo79g_vKxOPTWmPXAnj2mXhVIwN-PBdU"  # ضع توكن البوت الجديد هنا بين العلامتين
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا دكتور في بوت المحاضرات الطبية الجديد! 🩺")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(skip_pending=True)
