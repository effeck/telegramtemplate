from typing import Any
from telegram import Update

async def start(update: Update, context: Any) -> None:
    await update.message.reply_text(
        "<b>Привет! Я шаблон для Telegram-бота!</b> 🤖\n\n"
        "Доступные команды:\n"
        "• <b>/menu</b> – Показать интерактивное меню\n"
        "• <b>/info</b> – Информация о вас и чате\n"
        "• <b>/botinfo</b> – Информация о боте и ссылка на шаблон\n"
        "• <b>/start</b> – Показать это приветствие\n\n"
        "Используйте команды выше, чтобы изучить возможности!\n"
        "Если возникнет ошибка, она будет обработана автоматически 😉"
    )
