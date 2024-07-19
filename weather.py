import telebot
import json
import requests
from telebot import types

bot = telebot.TeleBot('6882643996:AAFkKtvXuozEm4WwW113px8AH83enXmgwx0')
API_KEY = '60755f54facf6bd08ac1ce6f3a99d14f'
city = 'Ryazan'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    return f'Погода в {city}: {temperature}°C, {description}'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    print(message)

    if message.text == "/start":
        bot.send_message(message.from_user.id,
                         " BOT By NetCat1051/ Привет. Я погодный бот. Нажми на кнопку, чтобы узнать актуальную погоду")

        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn1 = types.KeyboardButton('погода')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Выберите опцию:", reply_markup=markup)
    elif message.text == "погода":
        bot.send_message(message.from_user.id, get_weather(city))

bot.polling(none_stop=True, interval=0)