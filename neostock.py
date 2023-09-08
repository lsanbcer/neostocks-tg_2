from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

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

def echo(bot, update):
    message = update.message
    text = message.text
    if text in stock_lst:
        update.message.reply_text(text,
                                reply_markup = InlineKeyboardMarkup([[
                                    InlineKeyboardButton('Buy',
                                                        url = 'https://www.neopets.com/stockmarket.phtml?type=buy&ticker=' + text),
                                    InlineKeyboardButton('1 Day',
                                                        url = 'https://neostocks.info/tickers/' + text),
                                    InlineKeyboardButton('5 Day',
                                                        url = 'https://neostocks.info/tickers/' + text + '?period=5d'),
                                    InlineKeyboardButton('1 Month',
                                                        url = 'https://neostocks.info/tickers/' + text + '?period=1m'),
                                    InlineKeyboardButton('All',
                                                        url = 'https://neostocks.info/tickers/' + text + '?period=all')
                                ]])
        )
    else:
        text = '請輸入正確指令'
        update.message.reply_text(text = text)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))

who = '<your chat id>'
text = 'Neopest stocks 測試'
dispatcher.bot.send_message(chat_id = who, text = text)

updater.start_polling()