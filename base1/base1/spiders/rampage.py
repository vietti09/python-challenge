# -*- coding: utf-8 -*-
import scrapy


class RampageSpider(scrapy.Spider):
    name = 'rampage'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
