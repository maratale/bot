# @translit_by_law_bot

Бот для транслитерации ФИО по Приказу МИД РФ № 2113.

---

## Как запустить

### 1. Клонируйте репозиторий:

```bash
 git clone https://github.com/maratale/bot.git

 cd bot
```

---

2. Запускаете с помощью Docker:

```bash
docker build -t translit-bot -f Dockerfile.bot .
docker run --rm --env-file .env.example translit-bot
```
