# Подключаем модуль для Телеграма
import datetime
import os
import time
import telebot
from telebot import types
import config
from admin import admin_bot
from dotenv import load_dotenv
from linux_bot import linux_func
from windows_bot import windows_func
from web_res_bot import web_res_func
from emias_stacionar import emias_stacionar
from alerts_bot import alert_func


# Токен мгкб бота
load_dotenv()
token = os.getenv("TOKEN")

class BotData:
    bot = telebot.TeleBot(token)
#bot = telebot.TeleBot(token)

bot = BotData.bot
# Админка бота
admin_bot(bot)


def now():
    return datetime.datetime.now().strftime("%d.%m %H_%M_%S")


def tree_func():
    return config.MAIN_BUTTON


# Начальная команда
@bot.message_handler(func=lambda message: message.text == config.MAIN_MENU)
@bot.message_handler(commands=["start"])
def start(message):
    kb_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton
    kb_1.add(button(text=config.BTN_LNX), button(text=config.BTN_WDW), button(text=config.BTN_WEB))
    kb_1.add(button(text=config.BTN_STAC), button(text="ЕМИАС Поликлиника⚕️"))
    kb_1.add(button(text=config.TREES_TEXT), button(text=config.BTN_ALRT))
    # if message.from_user.id in config.USERS:
    #     kb_1.row(button(text='Режим учёта активности'))
    bot.send_message(message.chat.id, "С чем работаем?", reply_markup=kb_1)


# По части линукси
linux_func(bot)

# По части винды
windows_func(bot)

# Веб ресурсы
web_res_func(bot)

# Режим активности
# activity_mode_func(bot)

# ответы на вопросы по стационару
emias_stacionar(bot)

# оповещения дляИТ банды
alert_func(bot)


@bot.message_handler(commands=["help"])
def help_func(message):
    bot.send_message(
        message.chat.id,
        config.NOT_PARTNER,
    )


@bot.message_handler(func=lambda message: message.text == config.TREES_TEXT)
def skill_tree(message):
    kb_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton
    kb_1.add(button(text=config.BTN_LNX), button(text=config.BTN_WDW), button(text=config.BTN_WEB))
    kb_1.add(button(text=config.BTN_STAC), button(text="ЕМИАС Поликлиника⚕️"))
    kb_1.add(button(text=config.TREES_TEXT), button(text=config.BTN_ALRT))
    # if message.from_user.id in config.USERS:
    #     kb_1.row(button(text='Режим учёта активности'))
    bot.send_message(message.chat.id, tree_func(), reply_markup=kb_1)

@bot.message_handler(func=lambda message: message.text == "ЕМИАС Поликлиника⚕️")
def emias_policl(message):
    bot.send_message(message.chat.id, "Раздел в разработке. Сорян :)")

# Для добавления файлов
@bot.message_handler(
    func=lambda message: message.from_user.id == config.USERS[0],
    content_types=["document", "text", "photo"],
)
def send_admin(message):
    bot.send_message(message.chat.id, message)
    # ms = "сори, тест"
    # for i in (292078406, 96735814):
    #     bot.send_message(i, ms)
    #     time.sleep(0.5)


# while True:
#     try:
#         print("Бот пашет за копейки...")
#         bot.polling(non_stop=True, interval=1)
#         print("Бот уволился")
#     except Exception as e:
#         with open(config.PATH_ERRORS, "a+") as logs:
#             print(f"[{now()}]Error:\n{str(e)}", file=logs)
#         time.sleep(5)
if __name__ == "__main__":
    print("Бот пашет за копейки...")
    bot.infinity_polling()
    print("Бот уволился")
