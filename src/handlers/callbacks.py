from typing import Any
from telegram import Update

async def button(update: Update, context: Any) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        await query.edit_message_text("📋 Вы выбрали **информацию**.\nЗдесь будет информация о боте.")
    elif query.data == "stats":
        await query.edit_message_text("📊 Вы выбрали **статистику**.\nЗдесь будет статистика.")
    elif query.data == "settings":
        await query.edit_message_text("⚙️ Вы выбрали **настройки**.\nЗдесь будут настройки.")
    else:
        await query.edit_message_text("❓ Неизвестная опция.")
