import time
from telebot import types
import config


def web_res_func(bot):
    @bot.message_handler(func=lambda message: message.text == config.BTN_WEB)
    def web_resources(message):
        kb_web_res = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_web_res.row(button(config.MAIN_MENU), button(config.BTN_WEB_TEXT_1))
        kb_web_res.row(button(config.BTN_WEB_TEXT_2), button(config.BTN_WEB_TEXT_3))
        kb_web_res.row(button(config.BTN_WEB_TEXT_4), button(config.BTN_WEB_TEXT_5))
        kb_web_res.row(button(config.BTN_WEB_TEXT_6))
        bot.send_message(
            message.chat.id, "Что Вас интересует?", reply_markup=kb_web_res
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_WEB_TEXT_1
    )
    def plagin_for_epgu(message):
        kb_plagin_epgu = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_plagin_epgu.add(button(config.MAIN_MENU), button(config.BTN_WEB))
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_1,
            reply_markup=kb_plagin_epgu,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_WEB_TEXT_2)
    def link_on_webpage(message):
        kb_on_webpage = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_on_webpage.add(button(config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_2,
            reply_markup=kb_on_webpage,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_WEB_TEXT_3)
    def redirect_https(message):
        kb_redirect_https = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_redirect_https.row(button(config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_3,
            reply_markup=kb_redirect_https,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_WEB_TEXT_4)
    def send_sertificates(message):
        kb_send_sertificates = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_send_sertificates.row(button(config.MAIN_MENU))
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_1)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_2)
        time.sleep(0.5)
        bot.send_message(message.chat.id, config.TEXT_WEB_4)
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_3)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_4)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_5)
        time.sleep(0.5)
        bot.send_document(message.chat.id, config.LINK_PACK_SERT_6)
        time.sleep(0.5)
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_5,
            reply_markup=kb_send_sertificates,
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_WEB_TEXT_5
    )
    def plagin_for_firefox(message):
        kb_plagin_for_firefox = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_plagin_for_firefox.add(button(config.MAIN_MENU), button(config.BTN_WEB))
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_6,
            reply_markup=kb_plagin_for_firefox,
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_WEB_TEXT_6
    )
    def sert_kazna(message):
        kb_sert_kazna = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_sert_kazna.add(button(config.MAIN_MENU), button(config.BTN_WEB))
        bot.send_message(
            message.chat.id,
            config.TEXT_WEB_7,
            reply_markup=kb_sert_kazna,
        )
