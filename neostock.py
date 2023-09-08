from telegram.ext import Updater
from telegram.ext import CommandHandler

bot_token = '<your token>'

updater = Updater(bot_token, use_context=False)

stock_lst = ['AAVL','ACFI','BB','BOTT','BUZZ','CHIA','CHPS','COFL','CYBU','DROO','EEEEE','FAER',
             'FISH','HELT','HUW','KAUF','KBAT','KSON','LDSC','LUPE','MPC','MYNC','NAKR','NATN',
             'PDSS','PEOP','POWR','SHRX','SKBD','SKEI','SMUG','SSS','STFP','SWNC','TAG','TNAH',
             'TNPT','TPEG','TPP','TSRC','UNIB','VPTS','YIPP']

dispatcher = updater.dispatcher

def start(bot, update):
    message = update.message
    chat = message['chat']
    update.message.reply_text(text = 'HI ' + str(chat['id']))

dispatcher.add_handler(CommandHandler('start', start))

who = '<your chat id>'
text = 'Neopest stocks 測試'
dispatcher.bot.send_message(chat_id = who, text = text)

updater.start_polling()