from telegram.ext import Updater, CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your auto-massage bot.")


def auto_massage(update, context):
    # Implement your auto-massage logic here
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm massaging you automatically!")


def main():
    updater = Updater(token="6303490144:AAGfA9RzhDsdKkrsQQnxEnIrrzDbgj_S-cU", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    auto_massage_handler = CommandHandler('automassage', auto_massage)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(auto_massage_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
