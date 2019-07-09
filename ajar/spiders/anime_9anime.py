#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarItem


class QuotesSpider(CrawlSpider):

    name = '9anime'
    rotate_user_agent = True
    allowed_domains = ['animefrenzy.net']
    start_urls = ['https://animefrenzy.net']

    rules = (Rule(sle(allow='', ), callback='parse_anime_links', follow=True),)

    def parse_anime_links(self, response):
        server = []
        server = AjarItem()

        server['name'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.head > div.c1 > h2::text').get()
        return server
