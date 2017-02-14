# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GithubPipeline(object):
    def process_item(self, item, spider):
        # Here we are trying to clear the extracted items. The repo name does
        # not need to be cleaned because it is already clean when extracted.
        # For the rest we need to convert the list get into a single string
        # and remove the whitespace in the beginning and end.

        # Here we join the lists returned for language, stars, and forks using
        # an empty string and then use the strip method to remove whitespace
        # at the starting and end of the string.

        item['language'] = ''.join(item['language']).strip()
        item['stars'] = ''.join(item['stars']).strip()
        item['forks'] = ''.join(item['forks']).strip()
        return item
