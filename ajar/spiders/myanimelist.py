#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarWallAlphaItem


class QuotesSpider(CrawlSpider):

    name = 'anime_list'
    allowed_domains = ['myanimelist.net']
    start_urls = \
        ['https://myanimelist.net/anime/34134/One_Punch_Man_2nd_Season']

    rules = (Rule(sle(allow='https://myanimelist.net/anime/', deny=(
		'userrecs',
		'video',
		'episode',
		'characters',
		'featured',
		'profile',
		'login\.php',
		'anime\.php',
		'password\.php'
		'pressroom',
		'people',
		'advertising',
		'producer',
		'membership',
		'manga_translation_battle',
		'watch',
		'about\.php',
		'register\.php',
		'genre',
		'reviews',
		'stats',
		'forum',
		'clubs',
		'character',
		'news',
		'modules'
        )), callback='parse_images', follow=True), )

    def parse_images(self, response):
        image = []
        image = AjarWallAlphaItem()

        image['image_url'] = response.request.url
        image['image_pixels'] = \
            response.css('#contentWrapper > div:nth-child(1) > h1 > span::text'
                         ).get()

        return image
