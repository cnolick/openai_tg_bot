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

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat.id
    await update.message.reply_text(f'Your id: {chat_id}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Sorry, i'm private bot but if you want you "
                                        "can create self instanse this bot "
                                        "link - https://github.com/cnolick/openai_tg_bot")


async def question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    model_engine = "text-davinci-003"
    logger.info('get message:' + update.message.text)
    if int(update.message.chat.id) == int(os.getenv('CHAT_ID')):
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                {"role": "user", "content": update.message.text}])
            await  update.message.reply_text(completion.choices[0].message.content)
        except Exception as e:
            await update.message.reply_text('UPS, try again')
    else:
        await update.message.reply_text("Sorry, i'm private bot but if you want you "
                                        "can create self instanse this bot "
                                        "link - https://github.com/cnolick/openai_tg_bot")


def main() -> None:
    application = Application.builder().token(os.getenv('TELEGRAM_TOKEN')).build()
    openai.api_key = os.getenv('OPENAI_TOKEN')
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chat_id", chat_id))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, question))
    application.run_polling()


if __name__ == '__main__':
    main()
