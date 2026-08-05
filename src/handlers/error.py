import logging
import os
from typing import Any
from telegram import Update
from telegram.constants import ParseMode

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

async def error(update: object, context: Any) -> None:
    logger.exception("Необработанная ошибка: %s", context.error)
    try:
        if isinstance(update, Update) and update.effective_chat:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="⚠️ Произошла непредвиденная ошибка. Я уже зафиксировал проблему. Попробуйте ещё раз или используйте /menu.",
                parse_mode=ParseMode.HTML,
            )
    except Exception:
        pass
