# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import  os

import json
import scrapy
import pymysql
from scrapy.pipelines.images import ImagesPipeline

class MaoyanmoviesPipeline:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', passwd='123589', db='test_py', charset='utf8mb4',
                                  port=3306)
        self.cur = self.db.cursor()

    print('begin insert in to mysql')


    def process_item(self, item, spider):
        sql = 'INSERT INTO movie(movie_name,movie_type,movie_time) VALUES(%s,%s,%s) '
        self.cur.execute(sql, (item['movie_name'], item['movie_type'], item['movie_time']))
        self.db.commit()
        return item


    def close_spider(self, spider):
        self.cur.close()
        self.db.close()

