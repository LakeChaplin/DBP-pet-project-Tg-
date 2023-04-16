import datetime
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from selenium_script import get_best_story_data

from config import get_bot_token, get_comment
from cock_size import MeasuringState
from weather import Weather

TOKEN = get_bot_token()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

measurement_state = MeasuringState()

def create_keyboard():
    button_cook = InlineKeyboardButton("Share my cook size", callback_data="measure_cook_size")
    button_weather = InlineKeyboardButton("Get current weather", callback_data="get_weather")
    button_post = InlineKeyboardButton("Get a random post", callback_data="get_random_post")  
    keyboard = InlineKeyboardMarkup().add(button_cook).add(button_weather).add(button_post)
    return keyboard

@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Нажми на одну из кнопок для получения информации:",
                        reply_markup=create_keyboard())

@dp.callback_query_handler(lambda call: call.data == 'get_random_post')  
async def send_random_post(call: types.CallbackQuery):
    try:
        story_id, story_title, story_url, story_author, story_date, story_rating = get_best_story_data()
        await bot.send_message(chat_id=call.message.chat.id, text=f"Заголовок: {story_title}\nАвтор: {story_author}\nДата: {story_date}\nРейтинг: {story_rating}\nURL: {story_url}")
    except Exception as e:
        print('Error:', e)
        await bot.send_message(chat_id=call.message.chat.id, text="Извините, не удалось получить случайный пост.")


    

# MeasuringState
def measure_cook_size(self, user_id):
    self.last_measurement[user_id] = datetime.datetime.now()
    cook_size = random.randint(1, 30)
    message = f"{get_comment().format(cook_size)}"
    return cook_size, message

# Обработчик обратного вызова
@dp.callback_query_handler(lambda call: call.data == 'measure_cook_size')
async def process_callback(call: types.CallbackQuery):
    user_id = call.from_user.id
    user_fullname = call.from_user.username if call.from_user.username else call.from_user.first_name

    if measurement_state.can_measure(user_id):
        cook_size, message_with_comment = measurement_state.measure_cook_size(user_id)

        await bot.send_message(chat_id=call.message.chat.id, text=f"{user_fullname} - {message_with_comment}")
    else:
        await bot.answer_callback_query(call.id, "Вы уже измеряли свой кук недавно! Попробуйте еще раз через 24 часа.")










if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    
    
