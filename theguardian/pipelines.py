# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient, errors
from scrapy.conf import settings
import sys

class TheguardianPipeline(object):
    def __init__(self):
        connection = MongoClient(
            "mongodb+srv://user1:password12345@cluster0-82tvq.mongodb.net/"
            "test?retryWrites=true&w=majority")
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        if self.collection.count() == 0:
            self.collection.create_index("Url", unique=True)

    def process_item(self, item, spider):
        try:
            # self.collection.update(dict(item),upsert=True)
            self.collection.insert(dict(item), safe = True)
            # log.msg("Question added to MongoDB database!",
            #        level=log.DEBUG, spider=spider)
        except errors.DuplicateKeyError:
            pass
        except (errors.OperationFailure,
                errors.ServerSelectionTimeoutError) as e:
            print(e)
            sys.exit(1)

        return item
