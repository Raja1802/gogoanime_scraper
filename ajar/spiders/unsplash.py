#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarWallAlphaItem


class QuotesSpider(CrawlSpider):
    name = 'unspa'
    allowed_domains = ['pixabay.com']
    start_urls = ['https://pixabay.com/photos/']

    rules = (Rule(sle(allow=('photos'), deny=('search',

                                              )), callback='parse_images', follow=True),)

    def parse_images(self, response):
        image = []
        image = AjarWallAlphaItem()

        image['image_url'] = \
            response.request.url
        image['image_tags'] = \
            response.css('#media_show > div > div > p.tags > a::text'
                         ).getall()
        image['image_pixels'] = \
            response.css('#media_container > img::attr(src)'
                         ).get()

        return image

