from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Bot komondalari: ",
            "/start - Botni ishga tushirish\n\n",
            "Botni yaratuvchisiga taklif: @azikk_0418")
    
    await message.answer("\n".join(text))
