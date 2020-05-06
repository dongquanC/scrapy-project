# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class EnglishPipeline(object):
    def process_item(self, item, spider):
        
        # local_url = 'D:\\user\\Desktop\\english.txt'
        # with open(local_url,'w') as f:
        #     f.write("ddd")
        # # json.dump(item,open(local_url,'w'))
        # print(item)
        return item
