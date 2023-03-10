from config import Config
from strings import Strings
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import logging
from telegram import Update
from wrappers import send_typing_action
from frankfurter import FrankFurter

frank = FrankFurter()

conf = Config()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@send_typing_action
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(Strings['START_MSG'].format(update.effective_user.first_name))


@send_typing_action
async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    res = frank.latest()

    await update.message.reply_text(res)


if __name__ == '__main__':
    app = ApplicationBuilder().token(conf.BOT_TOKEN).build()

    app.add_handler(CommandHandler(
        command='start',
        callback=start
    ))

    app.add_handler(CommandHandler(
        command='latest',
        callback=latest
    ))

    app.run_polling()
