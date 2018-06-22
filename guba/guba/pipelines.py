# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class GubaPipeline(object):
    def __init__(self):
        author = 'Kay Zhou'

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        out_file = open(self.file_path(item), 'a')
        out_file.write(line)
        return item

    def file_path(self, item):
<<<<<<< HEAD
        path = "data/{}.txt" .format(item['stock_id'])
=======
        path = "{}.txt".format(item['stock_id'])
>>>>>>> 6deb1678b47b469430238fd3f7cc3374c4b58d4d
        return path


class UserPipeline(object):
    def __init__(self):
        author = 'Kay Zhou'

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        out_file = open(self.file_path(item), 'a')
        out_file.write(line)
        return item

    def file_path(self, item):
        path = "data/follow/{}.txt"
        return path