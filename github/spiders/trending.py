# -*- coding: utf-8 -*-
import scrapy


class TrendingSpider(scrapy.Spider):
    name = "trending"
    allowed_domains = ["github.com"]
    start_urls = ['http://github.com/']

    def parse(self, response):
        pass
