# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            item = dict(item)
            if self.collection.find(item).count() == 0:
                self.collection.insert(item)
        return item


class FinancialNewsPipeline(object):
    def process_item(self, item, spider):
        return item


if __name__ == "__main__":
    connection = pymongo.MongoClient(
        settings['MONGODB_SERVER'],
        settings['MONGODB_PORT']
    )
    db = connection[settings['MONGODB_DB']]
    collection = db[settings['MONGODB_COLLECTION']]
    print db.ths.find().count()
