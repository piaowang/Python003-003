# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanmoviesPipeline:

    # 开启爬虫时执行，只执行一次
    def open_spider(self, spider):
        # spider.hello = "world"  # 为spider对象动态添加属性，可以在spider模块中获取该属性值
        # 可以开启数据库等
        pass



    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        output = f'{movie_name},\t{movie_type}\t,{movie_time}\n'
        print('正在输出')
        with open('maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item

    def close_spider(self, spider):
        # 可以关闭数据库等
        pass
