from functools import wraps
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import CallbackContext


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    async def typing_func(update: Update, context: CallbackContext):
        await context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return await func(update, context)

    return typing_func
