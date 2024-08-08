import config
from main import BotData

bot = BotData.bot

def send_admin():
    bot.send_message(config.USERS[0], 'test')

send_admin()