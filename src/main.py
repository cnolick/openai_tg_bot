import os
import openai
import logging
from telegram import Update, ForceReply
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    CommandHandler,
    filters
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Пиши сюда любой вопрос, отвечу на все",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(" Просто напиши свой вопрос, или если что-то не работает пиши @SergeyKurbanov")


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    model_engine = "text-davinci-003"
    logger.info('get message:' + update.message.text)
    try:
        completion = openai.Completion.create(engine=model_engine, prompt=update.message.text, max_tokens=1024, n=1,
                                              stop=None,
                                              temperature=0.7)
        message = completion.choices[0].text
        await update.message.reply_text(message)
        logger.info('send message:' + message)
    except Exception as error:
        logger.error(f'Error: {error}')
        await update.message.reply_text('Случилась ошибка!')


def main() -> None:
    TG = os.getenv('TELEGRAM_TOKEN')
    AI = os.getenv('OPENAPI_TOKEN')
    logger.info(f'Start bot with TG_TOKEN: {TG} and AI_TOKEN {AI}')
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    openai.api_key = os.getenv('OPENAPI_TOKEN')
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, question))
    application.run_polling()


if __name__ == '__main__':
    main()
