#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarItem


class QuotesSpider(CrawlSpider):

    name = 'ajarani'
    allowed_domains = ['stackoverflow.com']
    start_urls = \
        ['https://stackoverflow.com'
         ]

    rules = (Rule(sle(allow='/watch/'), callback='parse_anime',
             follow=True), )

    def parse_anime(self, response):
        item = []
        item = AjarItem()
        # item['name'] = \
        #     response.css('#main > div > div.widget.info > div > div:nth-child(1)'
        #                  ).get()

        item['image'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.thumb.col-md-5.hidden-sm.hidden-xs > img::attr(src)'
                      ).get()
        item['name'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.head > div.c1 > h2::text'
                      ).get()
        item['synonyms'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.head > div.c1 > p::text'
                      ).get()

        item['types'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(1) > dd:nth-child(2)::text'
                      ).get()
        item['studios'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(1) > dd:nth-child(4) > a::attr(title)'
                      ).get()
        item['aired'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(1) > dd:nth-child(6)::text'
                      ).get()
        item['status'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(1) > dd:nth-child(8)::text'
                      ).get()
        item['scores'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(2) > dd:nth-child(2)::text'
                      ).get()
        item['premired'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(2) > dd:nth-child(6) > a::text'
                      ).get()
        item['durination'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(2) > dd:nth-child(8)::text'
                      ).get()
        item['quality'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(2) > dd:nth-child(10) > span::text'
                      ).get()
        item['gener'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.row > dl:nth-child(1) > dd:nth-child(10) > a::text'
                      ).getall()
        item['about'] = \
            response.css('#main > div > div.widget.info > div > div:nth-child(1) > div.info.col-md-19 > div.desc::text'
                      ).get()
        item['tags'] = response.css('#tags > a::text').getall()
        item['cover'] = \
            response.xpath("//*[@id='player']/div[contains(@class, 'cover')]//@style"
                        ).re_first(r'url\(([^\)]+)')

        return item
