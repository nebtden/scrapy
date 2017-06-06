# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import MySQLdb
import MySQLdb.cursors
import types


# 打开数据库连接
# db = MySQLdb.connect("localhost","root","root","scrapy" )
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data)

class WebcrawlerScrapyPipeline(object):
    # pipeline默认调用
    def process_item(self, item, spider):
        db = MySQLdb.connect("localhost", "root", "root", "scrapy")
        cursor = db.cursor()
        # for x in item:
        #     # sql = "INSERT INTO kilimall(title,url) \
        #     #        VALUES ('%s', '%s')" % \
        #     #       (x['title'], x['url'])
        #     # cursor.execute(sql)
        #     print('--------------------')
        #     # print(x)
        #     # print(item['x'])
        #     print('--------------------')
        print('--------------------')
        print(item)

        title = item['title']
        url = item['url']
        print(title[0])
        print(url[0])
        sql = "INSERT INTO kilimall(title,url) \
                           VALUES ('%s', '%s')" % \
              (title[0], url[0])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

        print('--------------------')


class LearningScrapy2Pipeline(object):
    def process_item(self, item, spider):
        return item


class KilimallPipline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
