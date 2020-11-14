# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class SpidersPipeline:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', passwd='123589', db='test_py', charset='utf8mb4',
                                  port=3306)
        self.cur = self.db.cursor()

    print('begin insert in to mysql')


    def process_item(self, item, spider):
        sql = 'INSERT INTO phone_comment(`rank`,`title`,`phone_url`,`commnet_text`,`comment_page`) VALUES(%s,%s,%s,%s,%s) '
        self.cur.execute(sql, (item['rank'],item['title'],item['phone_url'], item['commnet_text'],item['comment_page']))
        self.db.commit()
        return item


    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
