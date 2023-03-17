# '''
# from aiogram import types
# from googletrans import Translator

# translator = Translator()

# text = input("Text kirint: ")
# translate = translator.translate(text=text,dest='uz')
# print(translate.text)
# '''
# import json
# from aiogram import types
# from loader import dp, db, bot
# from googletrans import Translator
# from aiogram.dispatcher import FSMContext
# from states.state import tillar,tillar2,tillar3,tillar4

# #TARJIMON ENG-UZ #1
# @dp.message_handler(text="Eng🇺🇸-Uz🇺🇿",state="*")
# async def eng_uz(message: types.Message):
#     await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
#     await tillar2.eng_uz.set()
# @dp.message_handler(state=tillar2.eng_uz)
# async def eng_to_uz(message: types.Message,state: FSMContext):
#     try:
#         translator = Translator()
#         matn = message.text
#         translate = translator.translate(matn,dest='uz')
#         await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
#         # await state.finish()
#     except:
#         await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
#         # await state.finish()
#     finally:
#         await state.finish()

# @dp.message_handler(text="📥 Youtube",state="*")
# async def eng_uz(message: types.Message,state: FSMContext):
#     await message.answer("Hali bu funksiya ishga tushmagan😣")
#     await state.finish()
# #TARJIMON UZ-ENG #2
# @dp.message_handler(text="Uz🇺🇿-Eng🇺🇸",state="*")
# async def eng_uz(message: types.Message):
#     await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
#     await tillar.uz_eng.set()
# @dp.message_handler(state=tillar.uz_eng)
# async def eng1_to_uz(message: types.Message,state: FSMContext):
#     try:
#         translator = Translator()
#         matn = message.text
#         translate = translator.translate(matn)
#         await message.answer(f"{message.text} ni inglizchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
#         # await state.finish()
#     except:
#         await message.answer("Xato")
#         # state.finish()
#     finally:
#         await state.finish()
    
# #TARJIMON RU-UZ #3
# @dp.message_handler(text="Ru🇷🇺-Uz🇺🇿",state="*")
# async def eng_uz(message: types.Message,state: FSMContext):
#     await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
#     await tillar3.ru_uz.set()
# @dp.message_handler(state=tillar3.ru_uz)
# async def eng_to_uz(message: types.Message,state: FSMContext):
#     try:
#         translator = Translator()
#         matn = message.text
#         translate = translator.translate(matn,dest='uz')
#         await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
#         # await state.finish()
#     except:
#         await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
#         # await state.finish()
#     finally:
#         await state.finish()
# #TARJIMON UZ-RU #4
# @dp.message_handler(text="Uz🇺🇿-Ru🇷🇺",state="*")
# async def eng_uz(message: types.Message,state: FSMContext):
#     await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
#     await tillar4.uz_ru.set()
# @dp.message_handler(state=tillar4.uz_ru)
# async def eng_to_uz(message: types.Message,state: FSMContext):
#     try:
#         translator = Translator()
#         matn = message.text
#         translate = translator.translate(matn,dest='ru')
#         await message.answer(f"{message.text} ni ruschaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
#         # await state.finish()
#     except:
#         await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
#         # await state.finish()
#     finally:
#         await state.finish()
 

# @dp.message_handler(text="Hohlagan tilga tarjima")
# async def ll(message: types.Message):
#     listt = []
#     with open('languages.json','rb') as file:
#         tillar = json.load(file)
#         for til in tillar:
#             p = f"Long form {til['name']} Short form {til['code']}"
#             listt.append(p)
#             # print(a)
#         if len(listt) > 4096:
#             for x in range(0, len(listt), 4096):
#                 bot.send_message(message.chat.id, listt[x:x+4096])
#         # await message.answer(text=listt)
#Tarjimon Bo'limi
import aiogram
from states.state import tillar,tillar2,tillar3,tillar4,tillar5
from aiogram.dispatcher import FSMContext
from loader import db,bot,dp
from aiogram import types
from googletrans import Translator
from keyboards.default.defoultbutton import til


@dp.message_handler(text="🔄 Tarjimon",state="*")
async def tarjimon(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Qaysi tildan qaysi tilga tarjima qilmoqchisiz?\nPastdan menyudan tanlang!",reply_markup=til)

#TARJIMON ENG-UZ #1
@dp.message_handler(text="Eng🇺🇸-Uz🇺🇿",state="*")
async def eng_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zingizni yuboring")
    await tillar2.eng_uz.set()
    

#TARJIMON UZ-ENG #2
@dp.message_handler(text="Uz🇺🇿-Eng🇺🇸",state="*")
async def uz_eng(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zingizni yuboring")
    await tillar.uz_eng.set()

#TARJIMON RU-UZ #3
@dp.message_handler(text="Ru🇷🇺-Uz🇺🇿",state="*")
async def ru_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    await tillar3.ru_uz.set()
    
#TARJIMON UZ-RU #4
@dp.message_handler(text="Uz🇺🇿-Ru🇷🇺",state="*")
async def uz_ru(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    await tillar4.uz_ru.set()
    
    
    
#TARJIMON HOHLAGAN-TIL #5
@dp.message_handler(text="?-Uz 🇺🇿",state="*")
async def hohlagan_til_tarjima(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Siz hohlagan tildagi matnni yuboring men o'zbek tiliga tarjima qilib beraman!")
    await tillar5.hohlagan_til.set()



@dp.message_handler(state=tillar2.eng_uz)
async def eng_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
        await state.finish()

    


@dp.message_handler(state=tillar.uz_eng)
async def uz_eng1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn)
        await message.answer(f"{message.text} ni inglizchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato")
        await state.finish()
    

@dp.message_handler(state=tillar3.ru_uz)
async def ru_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
        await state.finish()


@dp.message_handler(state=tillar4.uz_ru)
async def uz_to_ru(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='ru')
        await message.answer(f"{message.text} ni ruschaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato 😑\nSiz boshqa tilda matn yubordingiz ❌")
        await state.finish()
        

    
@dp.message_handler(state=tillar5.hohlagan_til)
async def hohlagan_til_tarjima1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato 😑\nSiz boshqa tilda matn yubordingiz ❌")
        await state.finish()
