import telebot
from telebot import types
import requests
import lxml
from bs4 import BeautifulSoup as BS
from datetime import datetime

bot = telebot.TeleBot('6574813697:AAEE4FHm6yDbShanYzmqx3DDdSibH-9KyUg')

URL = 'https://kaktus.media/?lable=8&date=2021-31-32&order=time'

def get_now_url(url):
    calendar = datetime.now()
    index_start = url.index('date=')
    new_url = url[:index_start+5]
    date = str(calendar.year)+'-'
    month = ''
    day = ''
    if len(str(calendar.month)) == 1:
        month = '0'+str(calendar.month)
    else:
        month = str(calendar.month)
    if len(str(calendar.day)) == 1:
        day = '0'+str(calendar.day)
    else:
        day = str(calendar.day)
    date += month+'-'+day
    new_url += date + '&order=time'
    return new_url
    
NEW_URL = get_now_url(URL)




def get_html(url):
    response = requests.get(url)
    return response.text


# def get_data(html):
#     soup = BS(html,'lxml')
#     articles1 = soup.find('div',class_ = 'Tag--articles')
#     articles2 = articles1.find_all('div',class_ = 'Tag--article')
#     articles = articles[:21]
def get_mas_with_opis(url):
    html = get_html(url)
    soup = BS(html,'lxml')
    div = soup.find('div',class_ ='BbCode')
    p = div.find_all('p')
    return p

def get_data(html):
    list_id = [x for x in range(1,21)]
    soup = BS(html,'lxml')
    articles1 = soup.find('div',class_ = 'Tag--articles')
    articles2 = articles1.find_all('div',class_ = 'Tag--article')
    zagolovok_list = []
    list_href = []
    list_ = []
    list_photo = []
    for zagolovok in articles2:
        z = zagolovok.find('a',class_ = 'ArticleItem--name').get_text()
        z = z[18:-18]
        zagolovok_list.append(str(z))
        hr = zagolovok.find('a',class_ = 'ArticleItem--image').get('href')
        list_href.append(hr)
        try:
            img = zagolovok.find('img').get('src')
        except:
            img = ''
        finally:
            list_photo.append(img)
    dict_ = {}
    for key in list_id:
        for value in zagolovok_list[0:20]:
            dict_[key] = value

    list_.append(dict_)
    list_.append(list_href)
    list_.append(list_photo)
    return list_



start_markup = telebot.types.InlineKeyboardMarkup()
btn1= telebot.types.InlineKeyboardButton('1', callback_data='1')
btn2= telebot.types.InlineKeyboardButton('2', callback_data='2')
list_ = [btn1,btn2]
for x in list_:
    start_markup.add(x)




@bot.callback_query_handler(func=lambda callback: True)
def get_z(callback):
    dict_ = get_data(get_html(NEW_URL))
    # if callback.data == '1':
    #     bot.send_message(callback.message.chat.id, f'You choose 1')
    # elif callback.data == '2':
    #     bot.send_message(callback.message.chat.id, f'You choose 2')
    description= telebot.types.InlineKeyboardButton('description', callback_data='description')
    photo= telebot.types.InlineKeyboardButton('photo', callback_data='photo')
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(description,photo)
    bot.send_message(callback.message.chat.id, f'some title news you can see Description of this news and Photo',reply_markup=markup)
    if callback.data == 'description':
        textt = get_mas_with_opis(dict_[1][int(i)-1])
        bot.send_message(callback.message.chat.id,textt)
    



@bot.message_handler(commands = ['start'])
def start_message(message):
    list_ = get_data(get_html(NEW_URL))
    bot.send_message(message.chat.id,f'{list_[0]}',reply_markup=start_markup)



    








bot.polling()





