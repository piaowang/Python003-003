# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    print('into item')
    title= scrapy.Field()
    commnet_text = scrapy.Field()
    rank= scrapy.Field()
    comment_page = scrapy.Field()
    phone_url = scrapy.Field()

