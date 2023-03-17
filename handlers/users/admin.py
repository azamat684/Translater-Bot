import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
import aiogram
from aiogram.dispatcher import FSMContext
from states.state import reklama
@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[0])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(message.chat.id, df)
       

@dp.message_handler(text="/reklama", user_id=ADMINS, state="*")
async def optional_ad(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Menga reklama uchun ixtiyoriy xabar jo'nating va men uni foydalanuvchilarga jo'nataman.")
    await reklama.reklamaa.set()

@dp.message_handler(state=reklama.reklamaa)
async def send_optional_ad(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    try:
        for user in users:
            user_id = user[0]
            try:
                await message.send_copy(chat_id=user_id)
                await asyncio.sleep(0.05)
            except aiogram:
                await bot.send_message(chat_id=user_id,text=f"{user[1]} botni bloklagani uchun unga reklama bormadi")
                
    except Exception as error:
        print(error)
    finally:
        await message.answer(text="Reklama foydalanuvchilarga jo'natildi")
        await state.finish()

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")

@dp.message_handler(commands=['count'])
async def count_user(message: types.Message):
    a = db.count_users()
    await message.answer(f"Bazada {a} ta foydalanuvchi bor")