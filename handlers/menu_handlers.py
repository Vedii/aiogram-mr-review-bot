from aiogram import types

from common import callbacks
from common import commands
from common import keyboards
from filters import is_admin
from handlers.error_handlers import show_error_msg_for_n_seconds
from loader import app, dp
from locales import Locale


@dp.message_handler(commands.CommandMenu())
async def show_main_menu(message: types.Message):
    await message.reply(text=Locale.Menu.MENU_HEADER,
                        reply_markup=keyboards.get_main_menu(),
                        disable_notification=True,
                        )


@dp.callback_query_handler(callbacks.MenuCallBack.filter(action=[keyboards.MainMenu.show_adm_menu]))
async def show_adm_menu(query: types.CallbackQuery):
    if await is_admin.check(query):
        await app.bot.send_message(chat_id=query.from_user.id,
                                   text=f'{Locale.Common.CHAT_ORIGIN_MSG}\n'
                                        f'Admins menu',
                                   disable_notification=True,
                                   )
    else:
        await show_error_msg_for_n_seconds(obj=query, error_msg=Locale.Error.ADMIN_RIGHTS_REQUIRED)
