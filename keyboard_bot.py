from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

markup1 = InlineKeyboardMarkup()
btn_weather = InlineKeyboardButton('🌦Weather🌦', callback_data='b_weather')
btn_currency = InlineKeyboardButton('💸Currency💸', callback_data='b_currency')
btn_weather_curr = InlineKeyboardButton('🌦Weather & Currency💸', callback_data='b_weather_curr')

markup1.row(btn_weather)
markup1.row(btn_currency)
markup1.row(btn_weather_curr)



