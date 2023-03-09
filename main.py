from config import Config
from strings import Strings
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging
from telegram import Update

conf = Config()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Strings['START_MSG'].format(update.effective_user.first_name))


if __name__ == '__main__':
    app = ApplicationBuilder().token(conf.BOT_TOKEN).build()

    app.add_handler(CommandHandler(
        command='start',
        callback=start
    ))

    app.run_polling()
