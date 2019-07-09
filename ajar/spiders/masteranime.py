#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import MalItem


class QuotesSpider(CrawlSpider):

    name = 'mal'
    allowed_domains = ['myanimelist.net']
    start_urls = ['https://myanimelist.net/']

    rules = (Rule(sle(allow='/anime/\d+/', deny=(
        'video',
        'forum',
        'suggestion',
        'episode',
        'characters',
        'news',
        'stats',
        'userrecs',
        'reviews',
        'clubs',
        'pics',
        'episode',
        'forum',
        'featured',
        'moreinfo',
        )), callback='parse_anime', follow=True), )

    def parse_anime(self, response):
        item = []
        item = MalItem()

        item['name'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['image'] = \
            response.css('img.ac::attr(src)'
                         ).get()

        item['japan_name'] = \
            response.css('div.spaceit_pad::text'
                         ).getall()

        item['types'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['episodes'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['status'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['aired'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['premired'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['studios'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['source'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['gener'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['durination'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['rating'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['scores'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['about'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        item['trailer'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        return item
