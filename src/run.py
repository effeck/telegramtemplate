from __future__ import annotations

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
