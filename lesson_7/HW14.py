from aiogram import Bot, Dispatcher, executor, types, filters

TOKEN = '6127723191:AAF1-3gFbKVAaMAx5fWuehUBrupGhSSF-AQ'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb1 = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(text='Алгебра', callback_data='sendAlgebra')
b2 = types.InlineKeyboardButton(text='Геометрия', callback_data='sendGeometry')
b3 = types.InlineKeyboardButton(text='Тригонометрия', callback_data='sendTri')
kb1.add(b1)
kb1.row(b2)
kb1.row(b3)

kb2 = types.InlineKeyboardMarkup()
b4 = types.InlineKeyboardButton(text='Свойства степеней', callback_data='sendDegree')
b5 = types.InlineKeyboardButton(text='Свойства логарифмов', callback_data='sendLog')
b6 = types.InlineKeyboardButton(text='Формулы сокращённого умножения', callback_data='sendFsu')
kb2.add(b4, b5)
kb2.row(b6)

kb3 = types.InlineKeyboardMarkup()
b7 = types.InlineKeyboardButton(text='Формулы площади треугольника', callback_data='sendST')
kb3.add(b7)

kb4 = types.InlineKeyboardMarkup()
b8 = types.InlineKeyboardButton(text='Тригонометрическая окружность', callback_data='2')
b9 = types.InlineKeyboardButton(text='Таблица стандартных значений', callback_data='sendTable')
kb4.add(b8, b9)

Ref = {'degree': 'https://clck.ru/34bXfc',
       'log': 'https://clck.ru/34bXgn',
       'fsu': 'https://clck.ru/34bXhC',
       'trigtable': 'https://clck.ru/34bXmk',
       'trigcircle': 'https://clck.ru/34bXkC'}


@dp.message_handler(commands=['Start'])
async def cmd_handler(message: types.Message):
    await message.answer('Добро пожаловать! Это бот-справочник по математике. Выберите раздел.', reply_markup=kb1)

@dp.callback_query_handler(filters.Text(contains='sendAlgebra'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Выберите раздел.', reply_markup=kb2)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendGeometry'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Выберите раздел.', reply_markup=kb3)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendTri'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Выберите раздел.', reply_markup=kb4)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendDegree'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo('https://clck.ru/34bXfc', reply_markup=kb2)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendLog'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo('https://clck.ru/34bXgn', reply_markup=kb2)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendFsu'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo('https://clck.ru/34bXhC', reply_markup=kb2)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendST'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer('Извините, картинка пока не готова...', reply_markup=kb3)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='2'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo('https://clck.ru/34bXkC', reply_markup=kb4)
    await callback_query.answer()

@dp.callback_query_handler(filters.Text(contains='sendTable'))
async def some_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.message.answer_photo('https://clck.ru/34bXmk', reply_markup=kb4)
    await callback_query.answer()

@dp.message_handler(commands=['degree'])
async def cmd_handler(message: types.Message):
    await message.answer_photo(Ref['degree'], reply_markup=kb2)


@dp.message_handler(commands=['log'])
async def cmd_handler(message: types.Message):
    await message.answer_photo(Ref['log'], reply_markup=kb2)


@dp.message_handler(commands=['fsu'])
async def cmd_handler(message: types.Message):
    await message.answer_photo(Ref['fsu'], reply_markup=kb2)


@dp.message_handler(commands=['trigtable'])
async def cmd_handler(message: types.Message):
    await message.answer_photo(Ref['trigtable'], reply_markup=kb4)

@dp.message_handler(commands=['trigcircle'])
async def cmd_handler(message: types.Message):
    await message.answer_photo(Ref['trigcircle'], reply_markup=kb4)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)