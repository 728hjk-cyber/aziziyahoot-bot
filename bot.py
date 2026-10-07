import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا بيك ببوت عزيزية هوت 😎🔥\nدز رابط التيك توك واحملك الفيديو بدون علامة!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت اشتغل...")
    app.run_polling()

if __name__ == "__main__":
    main()
