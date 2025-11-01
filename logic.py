
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import dp
from database import get_quiz_index, update_quiz_index,get_user_score,update_user_score
from data import quiz_data

async def get_question(message: types.Message, user_id: int):
    current_question_index = await get_quiz_index(user_id)
    correct_option_index = quiz_data[current_question_index]['correct_option']
    opts = quiz_data[current_question_index]['options']
    kb = generate_options_keyboard(opts, opts[correct_option_index])
    await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)

async def new_quiz(message):
    user_id = message.from_user.id
    current_question_index = 0
    new_score = 0
    await update_quiz_index(user_id, current_question_index)
    await get_question(message, user_id)
    await update_user_score(user_id,new_score)

def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()
    for option in answer_options:
        builder.add(
            types.InlineKeyboardButton(
                text=option,
                callback_data="right_answer" if option == right_answer else "wrong_answer"
            )
        )
    builder.adjust(1)
    return builder.as_markup()


# === Правильный ответ ===
@dp.callback_query(F.data == "right_answer")
async def right_answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    await callback.message.answer("Верно!")
    current_question_index = await get_quiz_index(callback.from_user.id)
    current_score = await get_user_score(callback.from_user.id)

    current_question_index += 1
    current_score+=1
    
    await update_quiz_index(callback.from_user.id, current_question_index)
    await update_user_score(callback.from_user.id,current_score)
    if current_question_index < len(quiz_data):
        await get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer(f"Это был последний вопрос. Квиз завершен!\nВаш результат: {current_score} правильных ответов")

@dp.callback_query(F.data == "wrong_answer")
async def wrong_answer(callback: types.CallbackQuery):
    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )
    current_question_index = await get_quiz_index(callback.from_user.id)
    current_score = await get_user_score(callback.from_user.id)
    correct_option = quiz_data[current_question_index]['correct_option']
    await callback.message.answer(f"Неправильно! Правильный ответ: {quiz_data[current_question_index]['options'][correct_option]}")
    current_question_index += 1
   
    await update_quiz_index(callback.from_user.id, current_question_index)
    await update_user_score(callback.from_user.id,current_score)
    if current_question_index < len(quiz_data):
        await get_question(callback.message, callback.from_user.id)
    else:
        await callback.message.answer(f"Это был последний вопрос. Квиз завершен!\nВаш результат: {current_score} правильных ответов")
