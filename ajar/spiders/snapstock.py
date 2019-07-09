#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarPixabayItem


class QuotesSpider(CrawlSpider):

    name = 'stocksnap'
    allowed_domains = ['stocksnap.io']
    start_urls = \
        ['https://stocksnap.io/'
         ]

    rules = (Rule(sle(allow='/photo/'), callback='parse_images',
             follow=True), )

    def parse_images(self, response):
        image = []
        image = AjarPixabayItem()

        image['img_src'] = response.css('#main > div:nth-child(1) > div.img-col > figure > img::attr(src)').get()
        image['img_tags'] = \
            response.css('#main > div:nth-child(1) > div.img-col > figure > img::attr(alt)').get()

        return image
