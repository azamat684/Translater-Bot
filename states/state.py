from aiogram.dispatcher.filters.state import State,StatesGroup

class tillar2(StatesGroup):
    eng_uz = State()
    
class tillar(StatesGroup):
    uz_eng = State()

class tillar3(StatesGroup):
    ru_uz = State()
    
class tillar4(StatesGroup):
    uz_ru = State()
class tillar5(StatesGroup):
    hohlagan_til = State()
    
class reklama(StatesGroup):
    reklamaa = State()