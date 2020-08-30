# -*- coding: utf-8 -*-
import scrapy
import scrapy
import sys

from scrapy import Selector
#sys.path.append(r"C:/Users\chenming/Python003-003/week01/MaoyanMovies/MaoyanMovies")

from time import sleep
from bs4 import BeautifulSoup
from items import MaoyanmoviesItem
from pipelines import MaoyanmoviesPipeline
from scrapy.cmdline import execute
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
cookie = '_lxsdk_cuid=172a8697a46c8-07863daf44f946-87f133f-1fa400-172a8697a46c8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%22172a8697e063bb-097bafa65e2e58-87f133f-2073600-172a8697e07460%22%7D; uuid_n_v=v1; uuid=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; _csrf=26f7ea61031d83843e1fe596d71bd2e030224cdd7c1a8252680e36988e32f740; mojo-uuid=8dfd7a9865de74edd7cd5f95c3b05da5; _lxsdk=07975540E22F11EABDF7A52DEC86ABCD34B57FAC3EDE4CDCABF378DBF5F0C83F; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597850227,1597850252,1597932875; mojo-session-id={"id":"1e5a367323fc454b7877e90d10d0ac53","time":1598686449857}; mojo-trace-id=1; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1598686450; __mta=150811913.1597850228100.1598673134579.1598686451134.21; _lxsdk_s=174392351e8-8f9-5c7-d40%7C%7C2'
header = {'user-agent':user_agent, 'cookie':cookie }
#
movie_href = []


with open('next_info.html', encoding='utf-8') as f:
    next_text = f.read()
    #print(next_text)
    # xx = (next_text, 'html.parser')


# pagedata = Selector(next_text)

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass
    # start_urls = ['https://maoyan.com/board']

    def start_requests(self, ):
        global url
        movie_type=[]
        movie_href = []
        start_urls = 'https://maoyan.com/board'
        #print(start_urls)
        #result = scrapy.Request(url=start_urls, headers=header)
        print('排名连接获取开始')
        yield scrapy.Request(url=start_urls, callback=self.parse)

        #yield self.parse2(next_text)
        #yield self.parse(next_text)

    def parse(self, response):
        # response_next = requests.get(url, headers=header)
        global movie_day
        print('in to parse')
        # print(response)
        # response = BeautifulSoup(response.text, 'html.parser')
        # print(response.text)
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div/div/dl/dd/a/@href')
        for movie in movies:
            herf = 'https://maoyan.com' + movie.extract()
            movie_href.append([herf])

        print(movie_href)
        print('排名连接获取完成')
        #
        # for tags in response.find_all('p', attrs={'class': 'name'}):
        #     for atag in tags.find_all('a'):
        #         # movie_name = atag.get('title')
        #         herf = 'https://maoyan.com' + atag.get('href')
        #         # movie_time = releasetime
        #         movie_href.append([herf])
        print('next to parse2')

        for url in movie_href:
            # print(url[0])
            url = url[0]
            # print(url)
            sleep(10)
            yield scrapy.Request(url=url, callback=self.parse2)
        #yield scrapy.Request(url='https://maoyan.com/films/344264', callback=self.parse2)
        #     # url 请求访问的网址
        #     # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        #     # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
        print('获取明细连接完成')

    def parse2(self, response):
        print('into parse2')
        # print(response)
        movie_type = []
        item = MaoyanmoviesItem()
        #pagedata = Selector(text=xx.html)
        # print(pagedata)
        movie_name = Selector(response=response).xpath('//div[1]/h1/text()').extract()[0]
        print(movie_name)
        M_type = Selector(response=response).xpath('//ul/li/a[@class="text-link"]/text()')
        M_time = Selector(response=response).xpath('//ul/li[@class="ellipsis"]/text()')
        # print(type(M_time[-1].extract()))
        movie_time = M_time[-1].extract()[0:10]
        print(movie_time)
        # x=[movie_type.append(i.extract()) for i in M_type]
        [movie_type.append(i.extract().strip()) for i in M_type[:]]
        # print('type being')
        # print(i.extract())
        print(movie_type)
        print('正在输出明细{}'.format(movie_name))
        item['movie_name'] = movie_name
        item['movie_type'] = '|'.join(movie_type)
        item['movie_time'] = movie_time
        yield item
        movie_type = []


execute(['scrapy', 'crawl', 'maoyan'])