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
    dict_ = dict(zip(list_id,zagolovok_list))

    list_.append(dict_)
    list_.append(list_href)
    list_.append(list_photo)
    return list_



start_markup = telebot.types.InlineKeyboardMarkup()
btn1= telebot.types.InlineKeyboardButton('1', callback_data='1')
btn2= telebot.types.InlineKeyboardButton('2', callback_data='2')
btn3= telebot.types.InlineKeyboardButton('3', callback_data='3')
btn4= telebot.types.InlineKeyboardButton('4', callback_data='4')
btn5= telebot.types.InlineKeyboardButton('5', callback_data='5')
btn6= telebot.types.InlineKeyboardButton('6', callback_data='6')
btn7= telebot.types.InlineKeyboardButton('7', callback_data='7')
btn8= telebot.types.InlineKeyboardButton('8', callback_data='8')
btn9= telebot.types.InlineKeyboardButton('9', callback_data='9')
btn10= telebot.types.InlineKeyboardButton('10', callback_data='10')
btn11= telebot.types.InlineKeyboardButton('11', callback_data='11')
btn12= telebot.types.InlineKeyboardButton('12', callback_data='12')
btn13= telebot.types.InlineKeyboardButton('13', callback_data='13')
btn14= telebot.types.InlineKeyboardButton('14', callback_data='14')
btn15= telebot.types.InlineKeyboardButton('15', callback_data='15')
btn16= telebot.types.InlineKeyboardButton('16', callback_data='16')
btn17= telebot.types.InlineKeyboardButton('17', callback_data='17')
btn18= telebot.types.InlineKeyboardButton('18', callback_data='18')
btn19= telebot.types.InlineKeyboardButton('19', callback_data='19')
btn20= telebot.types.InlineKeyboardButton('20', callback_data='20')


start_markup.add(btn1,btn2,btn3,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20)



@bot.callback_query_handler(func=lambda callback: True)
def get_z(callback):
    dict_ = get_data(get_html(NEW_URL))
    textt = ['aasd']
    if callback.data == '1':
        textt = get_mas_with_opis(dict_[1][int(btn1.callback_data)-1])
    if callback.data == '2':
        textt = get_mas_with_opis(dict_[1][int(btn2.callback_data)-1])
    if callback.data == '3':
        textt = get_mas_with_opis(dict_[1][int(btn3.callback_data)-1])
    if callback.data == '4':
        textt = get_mas_with_opis(dict_[1][int(btn4.callback_data)-1])
    if callback.data == '5':
        textt = get_mas_with_opis(dict_[1][int(btn5.callback_data)-1])
    if callback.data == '6':
        textt = get_mas_with_opis(dict_[1][int(btn6.callback_data)-1])
    if callback.data == '7':
        textt = get_mas_with_opis(dict_[1][int(btn7.callback_data)-1])
    if callback.data == '8':
        textt = get_mas_with_opis(dict_[1][int(btn8.callback_data)-1])
    if callback.data == '9':
        textt = get_mas_with_opis(dict_[1][int(btn9.callback_data)-1])
    if callback.data == '10':
        textt = get_mas_with_opis(dict_[1][int(btn10.callback_data)-1])
    if callback.data == '11':
        textt = get_mas_with_opis(dict_[1][int(btn11.callback_data)-1])
    if callback.data == '12':
        textt = get_mas_with_opis(dict_[1][int(btn12.callback_data)-1])
    if callback.data == '13':
        textt = get_mas_with_opis(dict_[1][int(btn13.callback_data)-1])
    if callback.data == '14':
        textt = get_mas_with_opis(dict_[1][int(btn14.callback_data)-1])
    if callback.data == '15':
        textt = get_mas_with_opis(dict_[1][int(btn15.callback_data)-1])
    if callback.data == '16':
        textt = get_mas_with_opis(dict_[1][int(btn16.callback_data)-1])
    if callback.data == '17':
        textt = get_mas_with_opis(dict_[1][int(btn17.callback_data)-1])
    if callback.data == '18':
        textt = get_mas_with_opis(dict_[1][int(btn18.callback_data)-1])
    if callback.data == '19':
        textt = get_mas_with_opis(dict_[1][int(btn19.callback_data)-1])
    if callback.data == '20':
        textt = get_mas_with_opis(dict_[1][int(btn20.callback_data)-1])
    
    

    description= telebot.types.InlineKeyboardButton('description', callback_data='description')
    photo= telebot.types.InlineKeyboardButton('photo', callback_data='photo')
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row(description,photo)
    bot.send_message(callback.message.chat.id, f'some title news you can see Description of this news and Photo',reply_markup=markup)
    if callback.data == 'description':
        bot.send_message(callback.message.chat.id,textt)
        
    



@bot.message_handler(commands = ['start'])
def start_message(message):
    list_ = get_data(get_html(NEW_URL))
    bot.send_message(message.chat.id,f'{list_[0]}',reply_markup=start_markup)



    








bot.polling()





