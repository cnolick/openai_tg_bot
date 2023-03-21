# OpenAI Bot for Telegram.

Set up an API key. To use the OpenAI API, you will need to sign up for an account and obtain an API key. You can sign up for an API key at the OpenAI website (https://beta.openai.com/signup/).

Create telegram bot after BotFather and get access token

And just start

```bash
docker run -it -d \
-e OPENAPI_TOKEN=YOUR_OPENAPI_TOKEN \
-e TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN \
-e CHAT_ID=YOUR_CHAT_ID \
-e MODEL_NAME=YOUR_MODEL_NAME
$(docker build -q .)
```

YOUR_OPENAPI_TOKEN - you can get from openai.com

YOUR_TELEGRAM_TOKEN - you can get from @BotFather

YOUR_CHAT_ID -  your chat_id in telegram.

MODEL_NAME - model from openai.com


and ask AI about anything in your telegram bot.
