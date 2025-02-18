from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

BOT_TOKEN = "6313286573:AAGLT88WGxAMX1O25nWt62zfJ2LAeE6kTq0"  # Replace with your bot token

# Flask Web Server to Keep Replit Alive
app = Flask(__name__)


@app.route('/')
def home():
    return "Bot is running 24/7!"


def run():
    app.run(host="0.0.0.0", port=8080)


# Start Flask server in a separate thread
Thread(target=run).start()

# Telegram Bot Code
GIF_URL = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTA3d3FjMDNmNGtlYnR1ZHRuc2Nudmo2MnZvdndsZzQxYWkxenJnaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B3aenilOyPvxJRyQEP/giphy.gif"
WEB_APP_URL = "https://ankitasharma.shop/"
TELEGRAM_URL = "https://telegram.me/ankiitasharmmaa"
INSTAGRAM_URL = "https://www.instagram.com/ankitasharmmaa"


async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("🚀 Launch App",
                                 web_app=WebAppInfo(url=WEB_APP_URL))
        ],
        [
            InlineKeyboardButton("📢 Telegram", url=TELEGRAM_URL),
            InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_URL),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_animation(
        animation=GIF_URL,
        caption=
        "✨ **Welcome to the World of Ankita Sharma!** ✨\n\n🚀 **Your next-level experience starts here!**\nTap the button below to **launch the app** and dive into something exciting!\n\n🔥 Stay connected with us for the latest updates and exclusive content!",
        reply_markup=reply_markup,
        parse_mode="Markdown")


def main():
    bot_app = Application.builder().token(BOT_TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    bot_app.run_polling()


if __name__ == "__main__":
    main()
