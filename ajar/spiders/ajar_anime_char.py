#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import anime_planet_character


class QuotesSpider(CrawlSpider):
    name = 'planet_char'
    rotate_user_agent = True
    allowed_domains = ['www.anime-planet.com']
    start_urls = ['https://www.anime-planet.com']

    rules = (Rule(sle(allow='/characters/', ), callback='parse_anime_links', follow=True),)

    def parse_anime_links(self, response):
        server = []
        server = anime_planet_character()

        server['name'] = \
            response.css('#siteContainer > h1::text').get()
        server['gender'] = \
            response.css('#siteContainer > section.pure-g.entryBar > div:nth-child(1)::text').get()
        server['hair_color'] = \
            response.css('#siteContainer > section.pure-g.entryBar > div:nth-child(2)::text').get()
        server['image_url'] = \
            response.css(
                '#siteContainer > section:nth-child(10) > div.pure-1.md-2-3 > div.pure-g.entrySynopsis > div.pure-1-2.md-1-3 > div > img::attr(src)').get()
        server['about'] = \
            response.css(
                '#siteContainer > section:nth-child(10) > div.pure-1.md-2-3 > div.pure-g.entrySynopsis > div.pure-1.md-2-3 > div::text').getall()
        server['tags'] = \
            response.css(
                '#siteContainer > section:nth-child(10) > div.pure-1.md-2-3 > div.pure-g.entrySynopsis > div.pure-1.md-2-3 > div.tags > ul > li > a::text').getall()

        return server
