import telebot
from token_config import TOKEN_CONFIG
import keyboard_bot as kb
import weather_bot as wb
import currency_bot as cu

bot = telebot.TeleBot(TOKEN_CONFIG)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hi, {user_name}! 👋\n'
                                      'I can send you weather and exchange rate data 🌦💸\n'
                                      'What do you want to know, my leather friend? 🤖',
                     reply_markup=kb.markup1)


@bot.callback_query_handler(func=lambda call: True)
def send_weather(call):
    if call.data == 'b_weather':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='{}'.format(wb.get_weather()))
    elif call.data == 'b_currency':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='{}'.format(cu.send_currency()))

    elif call.data == 'b_weather_curr':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='{}\n\n{}'.format(wb.get_weather(), cu.send_currency()))
    else:
        pass


if __name__ == '__main__':
    bot.infinity_polling()
