import time
from telebot import types
import config


def alert_func(bot):
    @bot.message_handler(func=lambda message: message.text == config.BTN_ALRT)
    def alert(message):
        kb_alert = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_alert.add(
            button(text=config.BTN_ALRT_TEXT_1),
            button(text=config.BTN_ALRT_TEXT_2),
        )
        bot.send_message(
            message.chat.id, config.TEXT_ALRT_TEXT_1, reply_markup=kb_alert
        )
    

    @bot.message_handler(func=lambda message: message.text == config.BTN_ALRT_TEXT_1)
    def alert_policl(message):
        alert_policl = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        alert_policl.add(
            button(text=config.MAIN_MENU),
        )

        bot.send_message(
            message.chat.id,
            config.TEXT_ALRT_TEXT_2
        )

        bot.register_next_step_handler(message, alert_text, config.TEXT_ALRT_TEXT_5)

        # bot.send_message(
        #     message.chat.id, config.TEXT_ALRT_TEXT_3, reply_markup=alert_policl
        # )

    @bot.message_handler(func=lambda message: message.text == config.BTN_ALRT_TEXT_2)
    def alert_stac(message):
        alert_stac = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        alert_stac.add(
            button(text=config.MAIN_MENU),
        )

        bot.send_message(
            message.chat.id,
            config.TEXT_ALRT_TEXT_2
        )

        bot.register_next_step_handler(message, alert_text, config.TEXT_ALRT_TEXT_4)

    
    def alert_text(message, system):
        """Принимает текст ошибки и отправляет его."""
        alert_mes = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        alert_mes.add(
            button(text=config.MAIN_MENU),
        )
        text_from_user = message.text

        id_users = set(config.USERS)
        # id_users.remove(message.from_user.id)
        for id_user in id_users:
            try:
                bot.send_message(
                    id_user, 
                    f"❗❗ Оповещение о {system}:\n\n{text_from_user}",
                    reply_markup=alert_mes
                )
                time.sleep(0.5)
            except Exception:
                print(f'{id_user} не активен.')
        time.sleep(1)

        bot.send_message(
            message.chat.id, config.TEXT_ALRT_TEXT_3, reply_markup=alert_mes
        )
