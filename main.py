from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from secret import TOKEN

state = 0
reply_keyboard = [['Буллинг', 'Ученик - ученик'], ['Ученик - ученица', 'Группа - группа'], ['Назад']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text('Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, text))
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text('''Привет! Это бот, который поможет тебе справиться с конфликтами в школе. Обращайся!''',
                              reply_markup=markup)


def text(update, context):
    global state, markup
    if update.message.text == 'Буллинг':
        update.message.reply_text('Контакт психолога: Олег 8(964)792-47-79 ')
    elif update.message.text == 'Ученик - ученик':
        update.message.reply_text('Контакт психолога: Владимир 8(926)267-25-51')
    elif update.message.text == 'Ученик - ученица':
        update.message.reply_text('Контакт психолога по межполовым конфликтам: Екатерина 8(985)239-26-68')
    elif update.message.text == 'Группа - группа':
        update.message.reply_text('Контакт психолога по групповым конфликтам: Павел \n8(906)011-38-85')
    # elif update.message.text == 'Назад':
    #     update.message.reply_text('Возвращаемся на главную страницу', reply_markup=markup)


if __name__ == '__main__':
    main()
