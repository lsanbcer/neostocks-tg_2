from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from bs4 import BeautifulSoup
import re
import json
import requests

bot_token = '<your token>'

updater = Updater(bot_token, use_context=False)

stock_lst = ['AAVL','ACFI','BB','BOTT','BUZZ','CHIA','CHPS','COFL','CYBU','DROO','EEEEE','FAER',
             'FISH','HELT','HUW','KAUF','KBAT','KSON','LDSC','LUPE','MPC','MYNC','NAKR','NATN',
             'PDSS','PEOP','POWR','SHRX','SKBD','SKEI','SMUG','SSS','STFP','SWNC','TAG','TNAH',
             'TNPT','TPEG','TPP','TSRC','UNIB','VPTS','YIPP']

dispatcher = updater.dispatcher

def ticker_curr(ticker):
    url = 'https://neostocks.info/'
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tags = soup.find_all('script', string=re.compile("^window.__data__"))
    for tag in script_tags:
        string = str((tag.string)[18:])

    json_s = json.loads(string)

    for item in json_s['summary_data']['1d']:
        if item['ticker'] == str(ticker):
            curr = str(item['curr'])
            break
    return curr

def start(bot, update):
    message = update.message
    chat = message['chat']
    update.message.reply_text(text = 'HI ' + str(chat['id']))

def echo(bot, update):
    message = update.message
    text = message.text
    if text in stock_lst:
        curr = ticker_curr(text)
        update.message.reply_text(text + '  目前價格  ' + curr,
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

def tickers(bot, update):
    tickers_list = [['AAVL','ACFI','BB','BOTT'],['BUZZ','CHIA','CHPS','COFL'],['CYBU','DROO','EEEEE','FAER'],
             ['FISH','HELT','HUW','KAUF'],['KBAT','KSON','LDSC','LUPE'],['MPC','MYNC','NAKR','NATN'],
             ['PDSS','PEOP','POWR','SHRX'],['SKBD','SKEI','SMUG','SSS'],['STFP','SWNC','TAG','TNAH'],
             ['TNPT','TPEG','TPP','TSRC'],['UNIB','VPTS','YIPP']]
    reply_markup = ReplyKeyboardMarkup(tickers_list, one_time_keyboard=True)
    update.message.reply_text('請選擇要查詢的股票', reply_markup=reply_markup)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, echo))
dispatcher.add_handler(CommandHandler('ticker', tickers))

who = '<your chat id>'
text = 'Neopest stocks 測試'
dispatcher.bot.send_message(chat_id = who, text = text)

updater.start_polling()