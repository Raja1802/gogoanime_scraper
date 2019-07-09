#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarItem


class QuotesSpider(CrawlSpider):

    name = 'chia_anime'
    rotate_user_agent = True
    allowed_domains = ['ww2.chia-anime.tv']
    start_urls = ['http://ww2.chia-anime.tv']

    rules = (Rule(sle(allow='',), callback='parse_anime_links', follow=True), )

    def parse_anime_links(self, response):
        anime = []
        anime = AjarItem()

        anime['name'] = \
            response.css('#main > div > h1::text').get()
        anime['image'] = \
            response.css('#main > div > div:nth-child(4) > p > img::attr(src)').get()
        anime['english'] = \
            response.css('#main > div > blockquote:nth-child(6) > div:nth-child(1)::text').get()
        anime['japan'] = \
            response.css('#main > div > blockquote:nth-child(6) > div:nth-child(2)::text').get()
        anime['types'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(1)::text').get()
        anime['episodes'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(2)::text').get()
        anime['status'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(3)::text').get()
        anime['aired'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(4)::text').get()
        anime['premired'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(5)::text').get()
        anime['gener'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(6)::text').get()
        anime['durination'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(7)::text').get()
        anime['rating'] = \
            response.css('#main > div > blockquote:nth-child(8) > div:nth-child(8)::text').get()
        anime['about'] = \
            response.css('#main > div > blockquote:nth-child(9) > p::text').get()
        anime['tracker'] = \
            response.css('#main > div > div:nth-child(11) > a > span::text').get()

        return anime
