# OpenAI Bot for Telegram.

Set up an API key. To use the OpenAI API, you will need to sign up for an account and obtain an API key. You can sign up for an API key at the OpenAI website (https://beta.openai.com/signup/).

Create telegram bot after BotFather and get access token

And just start

```bash
docker run -it -d \
-e OPENAPI_TOKEN=YOUR_OPENAPI_TOKEN \
-e TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN \
$(docker build -q .)
```
and ask AI about anything in your telegram bot.
