#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AniList
import re


class QuotesSpider(CrawlSpider):

    name = 'anilist'
    allowed_domains = ['anilist.co']
    start_urls = ['https://anilist.co/anime/20/']

    rules = (Rule(sle(allow=[r'anime/\d+/\w+'], deny=[r'anime/\d+/\w+/staff']), callback='parse_anime_links', follow=True), )

    def parse_anime_links(self, response):
        anime = []
        anime = AniList()

        anime['Anime_url'] = \
            response.css('#app > div.page-content > div > div.header-wrap > div.header > div.container > div.content > h1::text').get()
        return anime
