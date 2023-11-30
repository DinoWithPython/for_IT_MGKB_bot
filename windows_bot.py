import time
from telebot import types
import config


def windows_func(bot):
    @bot.message_handler(func=lambda message: message.text == config.BTN_WDW)
    def windows_menu(message):
        kb_windows = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_windows.row(
            button(config.BTN_WDW_TEXT_1),
            button(config.BTN_WDW_TEXT_2),
            button(config.BTN_WDW_TEXT_3),
        )
        kb_windows.row(button(config.BTN_WDW_TEXT_4), button(config.BTN_WDW_TEXT_5))
        kb_windows.row(button(config.BTN_WDW_TEXT_6), button(config.MAIN_MENU))
        bot.send_message(
            message.chat.id, "Выберите желаемый продукт...", reply_markup=kb_windows
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_WDW_TEXT_1)
    def install_kasp(message):
        kb_kasp = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_kasp.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_document(message.chat.id, config.LINK_KASP, reply_markup=kb_kasp)

    @bot.message_handler(func=lambda message: message.text == config.BTN_WDW_TEXT_2)
    def install_ass(message):
        kb_kasp = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_kasp.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_message(message.chat.id, config.ASSISTANT_SERVER)
        bot.send_document(message.chat.id, config.LINK_ASS, reply_markup=kb_kasp)

    @bot.message_handler(func=lambda message: message.text == config.BTN_WDW_TEXT_3)
    def install_ass_c(message):
        kb_install_ass_c = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_install_ass_c.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_document(message.chat.id, config.LINK_ASS_C_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_ASS_C_2)
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_WDW_TEXT_1,
            reply_markup=kb_install_ass_c,
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_WDW_TEXT_4
    )
    def sert_egisz_and_epgu_for_windows(message):
        kb_sert = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_sert.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_WDW_TEXT_2,
        )
        time.sleep(1)
        bot.send_document(message.chat.id, config.LINK_SERT_EGISZ_EGPU_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_SERT_EGISZ_EGPU_2)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_SERT_EGISZ_EGPU_3)
        time.sleep(0.5)
        bot.send_document(
            message.chat.id, config.LINK_SERT_EGISZ_EGPU_4, reply_markup=kb_sert
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_WDW_TEXT_5)
    def install_crypto_pro(message):
        kb_crypto_pro = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_crypto_pro.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_document(message.chat.id, config.LINK_CRYPTO_4_99)
        time.sleep(0.5)
        bot.send_document(
            message.chat.id, config.LINK_CRYPTO_4_99_txt, reply_markup=kb_crypto_pro
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_WDW_TEXT_6
    )
    def install_check_fss(message):
        kb_check_fss = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_check_fss.add(button(config.BTN_WDW), button(config.MAIN_MENU))
        bot.send_document(message.chat.id, config.LINK_ERS_FSS_PROG)
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_WDW_TEXT_3,
            reply_markup=kb_check_fss,
        )
