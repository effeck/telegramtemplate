Шаблон Telegram-бота
Легковесный и модульный шаблон для быстрого создания ботов для Telegram с соблюдением лучших практик. Этот проект служит основой для новых ботов: структура организована, команды готовы к использованию, а расширение функционала не требует лишних усилий.

https://img.shields.io/badge/Python-3.13%252B-blue.svg
https://img.shields.io/badge/Telegram-Bot-26A5E4.svg
https://img.shields.io/badge/License-MIT-green.svg

Демонстрация
Бот в работе: @TemplateBot

Рекомендуемый хостинг: fps.ms – бесплатный хостинг для Telegram-ботов

Основные возможности
Модульная структура (каждая команда в отдельном обработчике).

Централизованная регистрация команд и callback-запросов.

Сообщения с HTML-разметкой и inline-клавиатурами.

Настраиваемое логирование через переменную окружения (LOG_LEVEL).

Лёгкость в адаптации, тестировании и развёртывании.

Структура проекта
text
src/
├─ run.py                      # Точка входа: запуск бота (Application, загрузка .env, инициализация)
└─ handlers/
   ├─ commands.py              # Регистрация всех обработчиков (команд, callback-ов, ошибок)
   ├─ start.py                 # /start
   ├─ menu.py                  # /menu
   ├─ info.py                  # /info и /botinfo
   ├─ callbacks.py             # CallbackQueryHandler (обработка нажатий на кнопки)
   └─ error.py                 # Обработка ошибок
Совет: добавьте файлы __init__.py в папки для упрощения импортов.

Требования
Python 3.13+

Токен бота Telegram (получить у @BotFather)

Настройка
Создайте файл .env в корне проекта:

env
TELEGRAM_BOT_TOKEN=вставьте_свой_токен_здесь
LOG_LEVEL=INFO
LOG_LEVEL может принимать значения: DEBUG, INFO, WARNING, ERROR, CRITICAL.

Установка
bash
# (опционально) создайте и активируйте виртуальное окружение
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# установите зависимости
pip install -r requirements.txt
Локальный запуск
bash
python src/run.py
По умолчанию шаблон использует Long Polling. Для работы в продакшене с Webhook настройте конфигурацию под вашу хостинговую платформу.

Доступные команды
/start – Приветственное сообщение и список команд.

/menu – Интерактивное меню с кнопками.

/info – Информация о пользователе, чате и сообщении.

/botinfo – Описание проекта и ссылка на GitHub.

Callback-запросы и обработка ошибок регистрируются автоматически в handlers/commands.py.

Примеры
Обработчик команды /start
python
# src/handlers/start.py
from typing import Any
from telegram import Update

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
async def start(update: Update, context: Any) -> None:
    await update.message.reply_text(
        "<b>Olá, eu sou um Bot Template para Telegram!</b> 🤖\n\n"
        "Aqui estão os comandos disponíveis:\n"
        "• <b>/menu</b> – Exibe o menu interativo com opções\n"
        "• <b>/info</b> – Mostra informações detalhadas sobre você e o chat\n"
        "• <b>/botinfo</b> – Explica a função do bot e mostra o link para o template\n"
        "• <b>/start</b> – Exibe esta mensagem de boas-vindas\n\n"
        "Use os comandos acima para explorar as funcionalidades!\n"
        "Se encontrar algum erro, ele será tratado automaticamente 😉",
        parse_mode="HTML",
    )
Централизованная регистрация обработчиков
python
# src/handlers/commands.py
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from . import start, menu, info, callbacks, error

def register_handlers(app: Application) -> None:
    app.add_handler(CommandHandler("start", start.start))
    app.add_handler(CommandHandler("menu", menu.menu))
    app.add_handler(CommandHandler("info", info.info))
    app.add_handler(CommandHandler("botinfo", info.bot_info))
    app.add_handler(CallbackQueryHandler(callbacks.button))
    app.add_error_handler(error.error)
Запуск бота
python
# src/run.py
from __future__ import annotations

import os

from dotenv import load_dotenv
from pathlib import Path

from telegram.constants import ParseMode
from telegram.ext import Defaults, Application

from handlers.commands import registrar_comandos

def main() -> None:
    load_dotenv()
    bot_env = Path(__file__).resolve().parent / ".env"
    if bot_env.exists():
        load_dotenv(dotenv_path=bot_env, override=True)
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise RuntimeError("Defina o Token do Bot em .env! TELEGRAM_BOT_TOKEN=")
    defaults = Defaults(parse_mode=ParseMode.HTML)
    app = (
        Application.builder()
        .token(bot_token)
        .defaults(defaults)
        .build()
    )
    registrar_comandos(app)
    try:
        app.run_polling()
    except KeyboardInterrupt:
        print("Bot interrompido!")

if __name__ == "__main__":
    main()
Развёртывание
fps.ms – бесплатный хостинг для Telegram-ботов

Участие в разработке
Приветствуются любые вклады!
Открывайте issue, отправляйте pull request или предлагайте улучшения.

Лицензия
MIT
