import time
from telebot import types
import config


def linux_func(bot):
    # По части линукси
    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX)
    def linux(message):
        kb_linux = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_linux.add(
            button(text=config.BTN_LNX_TEXT_1),
            button(text=config.BTN_LNX_TEXT_2),
            button(text=config.BTN_LNX_TEXT_3),
            button(text=config.BTN_LNX_TEXT_4),
            button(text=config.BTN_LNX_TEXT_5),
            button(text=config.BTN_LNX_TEXT_6),
            button(text=config.BTN_LNX_TEXT_7),
            button(text=config.BTN_LNX_TEXT_8),
        )
        bot.send_message(
            message.chat.id, config.TEXT_LNX_1, reply_markup=kb_linux
        )

    @bot.message_handler(
        func=lambda message: message.text == config.TEXT_LNX_2
    )
    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_1)
    def assistant_for_linux(message):
        kb_type_assistant = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_type_assistant.add(button(text=config.BTN_LNX_TEXT_1_1), button(text=config.BTN_LNX_TEXT_1_2))
        bot.send_message(
            message.chat.id, config.TEXT_LNX_3, reply_markup=kb_type_assistant
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_1_1)
    def assistant_deb(message):
        kb_type_assistant_deb = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_type_assistant_deb.add(
            button(text=config.TEXT_LNX_2), button(text=config.MAIN_MENU)
        )
        bot.send_document(
            message.chat.id, config.LINK_DEB_ASS, reply_markup=kb_type_assistant_deb
        )
        bot.send_message(
            message.chat.id,
            f"{config.TEXT_LNX_4}{config.ASSISTANT_SERVER}",
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_1_2)
    def assistant_rpm(message):
        kb_type_assistant_rpm = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_type_assistant_rpm.add(
            button(text=config.TEXT_LNX_2), button(text=config.MAIN_MENU)
        )
        bot.send_document(
            message.chat.id, config.LINK_RPM_ASS, reply_markup=kb_type_assistant_rpm
        )
        bot.send_message(
            message.chat.id,
            f"{config.TEXT_LNX_4}{config.ASSISTANT_SERVER}",
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2)
    def menu_vipnet(message):
        kb_menu_vipnet = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True, row_width=2
        )
        button = types.KeyboardButton
        kb_menu_vipnet.add(
            button(text=config.BTN_LNX_TEXT_2_1),
            button(text=config.BTN_LNX_TEXT_2_2),
            button(text=config.BTN_LNX_TEXT_2_3),
            button(text=config.MAIN_MENU),
        )
        bot.send_message(
            message.chat.id,
            "Какой вариант Вам подойдёт сегодня?",
            reply_markup=kb_menu_vipnet,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2_1)
    def install_vipnet(message):
        kb_vipnet_install = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_vipnet_install.add(button(text=config.BTN_LNX_TEXT_2), button(text=config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_5,
        )
        bot.send_document(
            message.chat.id, config.LINK_INSTALL_VIPNET, reply_markup=kb_vipnet_install
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2_2)
    def delete_vipnet(message):
        kb_delete_vipnet = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_delete_vipnet.add(button(text=config.BTN_LNX_TEXT_2), button(text=config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_6,
        )
        bot.send_document(
            message.chat.id, config.LINK_DELETE_VIPNET, reply_markup=kb_delete_vipnet
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2_3)
    def vipnet_gudes(message):
        kb_troubles_vipnet = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_troubles_vipnet.add(
            button(text=config.BTN_LNX_TEXT_2_3_1),
            button(text=config.BTN_LNX_TEXT_2_3_2),
            button(text=config.BTN_LNX_TEXT_2_3_3),
            button(text=config.BTN_LNX_TEXT_2_3_4),
            button(text=config.MAIN_MENU),
        )
        bot.send_message(
            message.chat.id, "Укажите проблему...", reply_markup=kb_troubles_vipnet
        )

    # Функция для возвращения к ошибкам с випнет

    def vipnet_gudes_return(message):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button = types.KeyboardButton
        kb.add(button(text=config.BTN_LNX_TEXT_2_3), button(text=config.MAIN_MENU))
        return kb

    # Проблемы при работе с випнет

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2_3_1)
    def sign_error(message):
        kb_for_troubles = vipnet_gudes_return(message)
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_7,
        )
        bot.send_document(
            message.chat.id, config.LINK_SING_ERROR, reply_markup=kb_for_troubles
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_2_3_2)
    def password_on_vipnet(message):
        kb_for_troubles = vipnet_gudes_return(message)
        bot.send_photo(message.chat.id, config.LINK_IMG_PASS_CONT_1)
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_8,
        )
        time.sleep(1)

        bot.send_photo(message.chat.id, config.LINK_IMG_PASS_CONT_2)
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_9,
        )
        bot.send_photo(
            message.chat.id, config.LINK_IMG_PASS_CONT_3, reply_markup=kb_for_troubles
        )

    @bot.message_handler(
        func=lambda message: message.text
        == config.BTN_LNX_TEXT_2_3_3
    )
    def linux_cryptoplag(message):
        kb_linux_crypto = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_linux_crypto.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_10,
            reply_markup=kb_linux_crypto,
        )

    @bot.message_handler(
        func=lambda message: message.text == config.BTN_LNX_TEXT_2_3_4
    )
    def linux_status_not_defined(message):
        kb_linux_not_defined = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_linux_not_defined.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))

        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_11,
            f"{config.DURATION_SERT}",
            reply_markup=kb_linux_not_defined,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_3)
    def install_hp(message):
        kb_install_hp = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_install_hp.add(button(text=config.MAIN_MENU))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_12,
        )
        bot.send_document(
            message.chat.id, config.LINK_INSTALL_HP, reply_markup=kb_install_hp
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_4)
    def update_firefox(message):
        kb_update_firefox = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_update_firefox.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_13,
            reply_markup=kb_update_firefox,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_5)
    def mini_commands(message):
        kb_mini_commands = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_mini_commands.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_14,
            reply_markup=kb_mini_commands,
        )

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_6)
    def install_chr_gst(message):
        kb_install_chr_gst = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_install_chr_gst.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_15,
        reply_markup=kb_install_chr_gst)


    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_7)
    def install_redos(message):
        kb_install_redos = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_install_redos.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_document(
            message.chat.id,
            config.LINK_REDOS_INST_PREF,
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_16,
        reply_markup=kb_install_redos)

    @bot.message_handler(func=lambda message: message.text == config.BTN_LNX_TEXT_8)
    def install_telegram(message):
        kb_install_telegram = types.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        button = types.KeyboardButton
        kb_install_telegram.add(button(text=config.MAIN_MENU), button(text=config.BTN_LNX))
        bot.send_document(
            message.chat.id,
            config.LINK_TELEGREAM_4_9_9,
        )
        bot.send_message(
            message.chat.id,
            config.TEXT_LNX_17,
        reply_markup=kb_install_telegram)
