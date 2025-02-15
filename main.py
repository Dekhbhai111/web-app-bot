from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

BOT_TOKEN = "6313286573:AAGLT88WGxAMX1O25nWt62zfJ2LAeE6kTq0"

# GIF URL
GIF_URL = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTA3d3FjMDNmNGtlYnR1ZHRuc2Nudmo2MnZvdndsZzQxYWkxenJnaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B3aenilOyPvxJRyQEP/giphy.gif"

# Web App & Social Links
WEB_APP_URL = "https://ankitasharma.shop/"
TELEGRAM_URL = "https://telegram.me/ankiitasharmmaa"
INSTAGRAM_URL = "https://www.instagram.com/ankitasharmmaa"


async def start(update: Update, context: CallbackContext):
    """Sends a greeting GIF with a stylish 'Launch App' button and social links"""
    keyboard = [
        # Full-width Launch App Button
        [
            InlineKeyboardButton("🚀 Launch App",
                                 web_app=WebAppInfo(url=WEB_APP_URL))
        ],
        # Telegram and Instagram buttons side by side
        [
            InlineKeyboardButton("📢 Telegram", url=TELEGRAM_URL),
            InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_URL),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message with GIF and interactive buttons
    await update.message.reply_animation(
        animation=GIF_URL,
        caption="""✨ **Welcome to the World of Ankita Sharma!** ✨  

🚀 **Your next-level experience starts here!**  
Tap the button below to **launch the app** and dive into something exciting!  

🔥 Stay connected with us for the latest updates and exclusive content!  
""",
        reply_markup=reply_markup,
        parse_mode="Markdown")


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
