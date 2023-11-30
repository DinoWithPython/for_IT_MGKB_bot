import time
from telebot import types
import config


def emias_stacionar(bot):
    """Функция по работе бота в разделе стационара."""
    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC)
    def stacionar(message):
        kb_stacionar = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_stacionar.add(
            button(text=config.BTN_STAC_TEXT_1),
            button(text=config.BTN_STAC_TEXT_2),
            button(text=config.BTN_STAC_TEXT_3),
            button(text=config.BTN_STAC_TEXT_4),
            button(text=config.BTN_STAC_TEXT_5),
            button(text=config.BTN_STAC_TEXT_6),
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id, config.TEXT_STAC_1, reply_markup=kb_stacionar
        )


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_2)
    def stacionar_instruction(message):
        kb_stacionar_instruction = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_stacionar_instruction.add(
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_2,
            parse_mode='HTML',
            reply_markup=kb_stacionar_instruction
        )


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_3)
    def deleted_card(message):
        kb_deleted_card = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_deleted_card.add(
            button(text=config.BTN_STAC),
            button(text=config.MAIN_MENU)
        )
        bot.send_document(
            message.chat.id,
            config.LINK_DELETE_CARD_SRASIONAR
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_3,
            reply_markup=kb_deleted_card
        )


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_1)
    def stcnr_err_sign(message):
        kb_stcnr_err_sign = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_stcnr_err_sign.add(
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_4,
            reply_markup=kb_stcnr_err_sign
        )
        bot.register_next_step_handler(message, st_err)

    def st_err(message):
        """Ответ по ошибкам."""
        kb_st_err = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_st_err.add(
            button(text=config.BTN_STAC_TEXT_1),
            button(text=config.BTN_STAC),
            button(text=config.MAIN_MENU),
        )

        text_from_user = message.text
        errors = config.TEXT_STAC_5
        code_errors = sorted([x for x in errors])
        if text_from_user.lower() == 'ошибки':
            bot.send_message(
                message.chat.id,
                '\n'.join([f'{number}. {element}' for number, element in enumerate(code_errors, start=1)]),
                reply_markup=kb_st_err
            )
            return
        count = 0
        for key, value in errors.items():
            if text_from_user.lower() in key.lower():
                bot.send_message(
                    message.chat.id,
                    value,
                    reply_markup=kb_st_err
                )
                return
            if text_from_user.lower() in value:
                bot.send_message(
                    message.chat.id,
                    value,
                    reply_markup=kb_st_err
                )
                time.sleep(0.5)
                count += 1
        if count == 0:
            bot.send_message(
                message.chat.id,
                config.TEXT_STAC_6,
                reply_markup=kb_st_err
            )
        count = 0


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_4)
    def moderation_dubles(message):
        kb_moderation_dubles = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_moderation_dubles.add(
            button(text=config.BTN_STAC),
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_7
        )
        time.sleep(0.5)
        bot.send_photo(
            message.chat.id,
            config.LINK_MOD_DUB_STC_1
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_8,
        )
        time.sleep(0.5)
        bot.send_photo(
            message.chat.id,
            config.LINK_MOD_DUB_STC_2
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_9,
        )
        time.sleep(0.5)
        bot.send_photo(
            message.chat.id,
            config.LINK_MOD_DUB_STC_3
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_10,
            reply_markup=kb_moderation_dubles
        )


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_5)
    def change_crypto(message):
        kb_change_crypto = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_change_crypto.add(
            button(text=config.BTN_STAC),
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_11
        )
        time.sleep(0.5)
        bot.send_photo(
            message.chat.id,
            config.LINK_STC_CHANGE_CRYPT_1
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_12,
        )
        time.sleep(0.5)
        bot.send_photo(
            message.chat.id,
            config.LINK_STC_CHANGE_CRYPT_2
        )
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_13,
            reply_markup=kb_change_crypto
        )


    @bot.message_handler(func=lambda message: message.text == config.BTN_STAC_TEXT_6)
    def info_periodics(message):
        kb_info_periodics = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_info_periodics.add(
            button(text=config.BTN_STAC),
            button(text=config.MAIN_MENU)
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_STAC_14,
            reply_markup=kb_info_periodics
        )
