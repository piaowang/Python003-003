# -*- coding: utf-8 -*-
import re
from time import sleep
import time
import os

import scrapy
from scrapy import Selector
from scrapy.cmdline import execute
from ..items  import SpidersItem

with open('next.html', encoding='utf-8') as f:
    sel  = Selector(text=f.read())
    #print(next_text)
    # xx = (next_text, 'html.parser')
with open('demo.html', encoding='utf-8') as f:
    comment  = Selector(text=f.read())

# pagedata = Selector(next_text)
item = SpidersItem()


class ZdmSpider(scrapy.Spider):
    name = 'zdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['http://smzdm.com/']

    def start_requests(self, ):
        global url
        movie_type = []
        movie_href = []
        start_urls = 'https://www.smzdm.com/fenlei/zhinengshouji/h4c4s0f0t0p1/#feed-main/' #
        yield scrapy.Request(url=start_urls, callback=self.parse)
        print('3小时排行获取前十的评论')


    def parse(self, response):
        # response_next = requests.get(url, headers=header)
        global movie_day
        phone_href = []
        print('in to parse')
        #print(response)
        #movies = Selector(response=response).xpath('//*[@id="app"]/div/div/div/dl/dd/a/@href')
        #rank = sel.xpath('//*[contains(@articleid,"3")]/@data-position')#('//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a/@href')
        #articleid =[ i.replace('3_','') for i in sel.xpath('//*[contains(@articleid,"3")]/@articleid').extract()]
        rank = Selector(response=response).xpath('//*[contains(@articleid,"3")]/@data-position')#('//*[@id="feed-main-list"]/li[1]/div/div[2]/h5/a/@href')
        articleid =[ i.replace('3_','') for i in Selector(response=response).xpath('//*[contains(@articleid,"3")]/@articleid').extract()]

        all = zip(rank.extract(),articleid)

        for num, href in all:
            if int(num) <= 10 :
                herf = 'https://www.smzdm.com/p/' + href
                phone_href.append([num,herf])
                #item['rank'] = str(num)
                #print(herf)
        #print(phone_href)

        for url in phone_href:
            num = url[0]
            url = url[1]
            #print(num)
            #print(url)
            sleep(2)
            #yield scrapy.Request(url='', callback=self.parse2)
            yield scrapy.Request(url=url,meta={'num':num,'pyhone':url},callback=self.parse2)

    def parse2(self, response):
        print('into parse2')
        num = response.meta['num']
        phone = response.meta['pyhone']

        print(response.request.url)
        #list1 =  [ int(i) for i in list(filter(str.isdigit, comment.xpath('//*[@class="pagination"]/li/a/text()').extract()))]
        list1 = [int(i) for i in
                 list(filter(str.isdigit, Selector(response=response).xpath('//*[@class="pagination"]/li/a/text()').extract()))]
        #print(list1)
        #print(response.request.url)
        for comment_page in range(1,max(list1)+1): #
            url = response.request.url+'p'+str(comment_page)+'/#comments'
            print(url)
            #print('第‘ + comment_page + ’页面评论')
            yield scrapy.Request(url=url,meta={'num':num,'comment_page':comment_page,'phone':phone},callback=self.parse3,dont_filter=True)
            #print(comment_page ,' is ok')
        print(max(list1))

    def parse3(self,response):
        print('into parse3')
        rank = response.meta['num']
        comment_page =  response.meta['comment_page']
        phone_url = response.meta['phone']
        print('评论页面' +str(comment_page))
        #print(comment_page)
        title =  str(Selector(response=response).xpath('/html/head/title/text()').extract_first())
        #print(title)
        for commnet_text in Selector(response=response).xpath('//*[@itemprop="description"]/text()').extract()[2:]:
            item['rank'] = int(rank)
            item['title'] = title
            item['phone_url'] = phone_url
            item['commnet_text'] = commnet_text
            item['comment_page'] = comment_page
            yield item
        #print(commnet_text)
        # # print(response)
        # movie_type = []

        # phone_rank = Selector(response=response).xpath('//ul/li/a[@class="text-link"]/text()')
        # phone_commets = Selector(response=response).xpath('//ul/li[@class="ellipsis"]/text()')
        # # print(type(M_time[-1].extract()))
        # movie_time = M_time[-1].extract()[0:10]
        # print(movie_time)
        # # x=[movie_type.append(i.extract()) for i in M_type]
        # [movie_type.append(i.extract().strip()) for i in M_type[:]]
        # # print('type being')
        # # print(i.extract())
        # print(movie_type)
        # print('正在输出明细{}'.format(movie_name))


        # movie_type = []

if __name__ = '__main__':

    while True:
        os.system("scrapy crawl News")
        time.sleep(86400)  # 每隔一天运行一次 24*60*60=86400s