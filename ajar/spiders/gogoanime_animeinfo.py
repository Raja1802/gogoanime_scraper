#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import gogoanime_info


class QuotesSpider(CrawlSpider):

    name = 'gogoinfo'
    allowed_domains = ['www6.gogoanime.io']
    start_urls = \
        ['https://www6.gogoanime.io/'
         ]

    rules = (Rule(sle(allow=''), callback='parse_anime',
             follow=True), )

    def parse_anime(self, response):
        item = []
        item = gogoanime_info()

        item['image_url'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > img::attr(src)').extract()
        item['name'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > h1::text').extract()
        item['type'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(4) > a::text').extract()
        item['plot'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(5)::text').extract()
        item['gener'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(6) > a::text').extract()
        item['aired'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(7)::text').extract()
        item['status'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(8)::text').extract()
        item['other_name'] = \
            response.css('#wrapper_bg > section > section.content_left > div.main_body > div:nth-child(2) > div.anime_info_body_bg > p:nth-child(9)::text').extract()
        # item['url_name'] = \
        #     response.request.url
        return item
