from functools import reduce
from os.path import join

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
cookie = '__mta=150811913.1597850228100.1597933010209.1597933085021.12; _lxsdk_cuid=172a8697a46c8-07863daf44f946-87f133f-1fa400-172a8697a46c8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%7D; uuid_n_v=v1; uuid=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; _csrf=26f7ea61031d83843e1fe596d71bd2e030224cdd7c1a8252680e36988e32f740; mojo-uuid=8dfd7a9865de74edd7cd5f95c3b05da5; _lxsdk=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; mojo-session-id={"id":"3572b70c0721a3293409b50e481dce1c","time":1597932874850}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597850227,1597850252,1597932875; __mta=150811913.1597850228100.1597933008408.1597933011881.11; mojo-trace-id=12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597933084; _lxsdk_s=1740c388499-54c-643-799%7C%7C16'

header = {'user-agent':user_agent, 'cookie':cookie }
#
myurl = 'https://maoyan.com/board'
#
from time import sleep
sleep(5)
response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')

with open('next_info.txt', encoding='utf-8') as f:
    next_text = f.read()
    # print(text)
    xx = bs(next_text, 'html.parser')

type_name = []
movie = {}
movie_href = []
movie_list = []
movie_name = []
movie_time = []


for tags in bs_info.find_all('p', attrs={'class': 'name'}):
    for atag in tags.find_all('a'):
         #movie_name = atag.get('title')
         herf= 'https://maoyan.com' + atag.get('href')
        # movie_time = releasetime
         movie_href.append([herf])



def movie_next():
    # global bs_info_next
    global type_name, movie_day
    num = 1
    for url in movie_href:
        url = url[0]
        print(url)
        sleep(10)

        response_next = requests.get(url, headers=header)
        bs_info_next = bs(response_next.text, 'html.parser')
        #print(bs_info_next)
        for atag in bs_info_next.find_all('div', attrs={'class': 'movie-brief-container'}):

            # print(atag)
            # type_name.append(str(atag.text))
            # print(type_name)
            # movie_list.append([movie_name,type_name])
            # print(atag.text[-1])
            name = atag.find('h1', attrs={'class': 'name'}).text
            # time = atag.find_all('li', attrs={'class': 'ellipsis'}).text
            # print(time)

                # print(type_name)
            for atag2 in atag.find_all('li', attrs={'class': 'ellipsis'}):
                movie_time.append(atag2.text)
                # print(movie_time)
            for atag1 in atag.find_all('a', attrs={'class': 'text-link'}):
                type_name.append(atag1.text)
                movie_day =  str.replace(movie_time[-1],'中国大陆上映','',)
                movie_day = str.replace( movie_day,  '中国大陆重映', '', )
            # print(movie_time[-1])
            rank = '第' + str(num) +'名'
            movie_list.append([rank,name, '|'.join(type_name), movie_day])
            #print(movie_list)
            type_name=[]
            num +=1

movie_next()
print(movie_list)

movie1 = pd.DataFrame(data = movie_list)
#
# # windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
