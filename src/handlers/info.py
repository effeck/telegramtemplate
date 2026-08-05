from typing import Any
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def info(update: Update, context: Any) -> None:
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    info_text = (
        f"🧑 <b>Информация о пользователе</b>\n"
        f"ID: <code>{user.id}</code>\n"
        f"Имя: <code>{user.first_name} {user.last_name or ''}</code>\n"
        f"Юзернейм: <code>@{user.username or 'Нет'}</code>\n"
        f"Язык: <code>{user.language_code or 'Неизвестен'}</code>\n"
        f"Это бот?: <code>{'Да' if user.is_bot else 'Нет'}</code>\n\n"
        f"💬 <b>Информация о чате</b>\n"
        f"ID: <code>{chat.id}</code>\n"
        f"Тип: <code>{chat.type}</code>\n"
        f"Название: <code>{chat.title or 'Нет'}</code>\n"
        f"Юзернейм: <code>@{chat.username or 'Нет'}</code>\n\n"
        f"📝 <b>Информация о сообщении</b>\n"
        f"ID: <code>{message.message_id}</code>\n"
        f"Дата: <code>{message.date.strftime('%Y-%m-%d %H:%M:%S')}</code>\n"
        f"Текст: <code>{message.text or 'Не текст'}</code>\n"
    )

    await update.message.reply_text(info_text, parse_mode="HTML")


async def bot_info(update: Update, context: Any) -> None:
    info_text = (
        "<b>🤖 Шаблон для Telegram-бота</b>\n\n"
        "Этот бот создан как <b>шаблон</b> для разработчиков, которые хотят начать свои проекты в Telegram.\n"
        "В нём есть примеры команд, интерактивного меню и интеграции с современными библиотеками — "
        "это отличная отправная точка для любого бота!\n\n"
        "Основные возможности:\n"
        "• Простая и понятная структура\n"
        "• Готовые команды для редактирования и расширения\n"
        "• Интерактивное меню и персонализированные ответы\n"
        "• Готов к развёртыванию в облаке\n\n"
        "👉 Чтобы посмотреть исходный код, примеры и документацию, нажмите на кнопку ниже:\n"
    )

    github_url = "https://github.com/diegooilv/telegram-bot-template-py"
    keyboard = [
        [InlineKeyboardButton("🌐 Шаблон на GitHub", url=github_url)],
        [InlineKeyboardButton("📚 Документация python-telegram-bot",
                              url="https://docs.python-telegram-bot.org/en/stable/")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        info_text,
        reply_markup=reply_markup
    )
