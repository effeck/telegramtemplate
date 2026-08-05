from typing import Any
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update

async def menu(update: Update, context: Any) -> None:
    keyboard = [
        [InlineKeyboardButton("📋 Информация", callback_data="info")],
        [InlineKeyboardButton("📊 Статистика", callback_data="stats")],
        [InlineKeyboardButton("⚙️ Настройки", callback_data="settings")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("📌 Выберите пункт меню:", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text("📌 Выберите пункт меню:", reply_markup=reply_markup)
