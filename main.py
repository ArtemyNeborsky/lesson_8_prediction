import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater
from telegram.ext import MessageHandler, Filters


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Привет! Я могу предсказать твою судьбу по знаку зодиака. Напиши свой знак!"
    )


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Напиши свой знак зодиака, и я дам тебе предсказание!"
    )


def zodiac_prediction(update, context):
    predictions = {
        'овен': 'Сегодня день для решительных действий! Вас ждёт успех.',
        'телец': 'Проведите день спокойно, подумайте о будущем. Хороший день для планирования.',
        'близнецы': 'Будьте осторожны с новыми знакомыми, не все они искренни.',
        'рак': 'Сегодня удачный день для улучшения отношений с близкими.',
        'лев': 'Постарайтесь избежать конфликтов на работе, они могут затянуться.',
        'дева': 'Сегодня удачный день для финансовых вложений и покупок.',
        'весы': 'Возможно, вам придется принять важное решение, доверьтесь интуиции.',
        'скорпион': 'Не бойтесь рисковать сегодня, это принесет свои плоды.',
        'стрелец': 'Сегодня отличный день для путешествий и новых впечатлений.',
        'козерог': 'Уделите внимание здоровью, не перегружайте себя на работе.',
        'водолей': 'Вы найдете решение проблемы, которая давно вас беспокоит.',
        'рыбы': 'Сегодня вас ждет приятный сюрприз от близкого человека.'
    }

    text = update.message.text.lower().strip()

    if text in predictions:
        response = f"Твое предсказание для знака зодиака {text}: {predictions[text]}"
    else:
        response = "Я не знаю такого знака зодиака. Напиши, например: овен, телец, близнецы..."

    update.message.reply_text(response)


def main():
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", start)
    help_handler = CommandHandler("help", help)
    zodiac_handler = MessageHandler(Filters.text & ~Filters.command, zodiac_prediction)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(zodiac_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()