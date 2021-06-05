import telebot
import config, func
from random import randint


bot = telebot.TeleBot(config.token)

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('/start', 'Да/Нет', 'Вероятность')
keyboard.row('Случайное число')


@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуй.', reply_markup = keyboard)



@bot.message_handler(content_types = ['text'])
def send_answer(message):

    if message.text.lower() == 'вероятность':
        bot.send_message(message.chat.id, '{:.2%}'.format(func.probability()))
    
    elif message.text.lower() == 'да/нет':
        bot.send_message(message.chat.id, func.YorN())
    
    elif message.text.lower() == 'случайное число':
        bot.send_message(message.chat.id, 'Задайте нижнюю границу диапазона')
        bot.register_next_step_handler(message, bot_range)
    else:
        bot.send_message(message.chat.id, 'Данный запрос на данный момент не поддерживается обратитесь командой /start'\
                                          ' для вызова клавиатуры с подсказками')

def bot_range(message):
    global bottom_range
    try:
        bottom_range = int(message.text)
        bot.send_message(message.chat.id, 'Задайте верхнюю границу диапазона')
        bot.register_next_step_handler(message, top_range)
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "Формат ввода - числа (цифрами(не буквами)).")

def top_range(message):
    global top_range
    try:
        top_range = int(message.text)
        bot.send_message(message.chat.id, randint(bottom_range, top_range))
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id, "Формат ввода - числа (цифрами(не буквами)).")

bot.infinity_polling(True)
