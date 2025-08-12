# Telegram Translit Bot

Бот для транслитерации ФИО по Приказу МИД РФ № 2113.

---

## Как запустить

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/maratale/bot.git

cd telegram_translit_bot

### 2. Запускаете с помощью Docker:

docker build -t translit-bot -f Dockerfile.bot .

docker run --rm --env-file .env.example translit-bot
