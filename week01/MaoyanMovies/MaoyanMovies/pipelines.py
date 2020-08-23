# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviesPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        output = f'{movie_name},\t{movie_type}\t,{movie_time}\n'
        print('正在输出')
        with open('maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
