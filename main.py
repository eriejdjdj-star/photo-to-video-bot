import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN =9178976133:AAHfBvIJCA3IU7oT0F_6iXQFjB6cbn0jOqQ



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\n"
        "عکس خودت رو بفرست.\n"
        "فعلاً ربات در مرحله آزمایشی است."
    )


async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]

    file = await context.bot.get_file(photo.file_id)
    os.makedirs("photos", exist_ok=True)

    path = f"photos/{update.effective_user.id}.jpg"
    await file.download_to_drive(path)

    await update.message.reply_text(
        "عکست دریافت و ذخیره شد! ✅\n"
        "هنوز سرویس هوش مصنوعی ساخت ویدئو متصل نشده است."
    )


def main():
    if not TOKEN:
        raise RuntimeError("TELEGRAM_BOT_TOKEN تنظیم نشده است.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, receive_photo))
    app.run_polling()


if __name__ == "__main__":
    main()
