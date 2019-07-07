#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarGogoanimeItem


class QuotesSpider(CrawlSpider):

    name = 'gogoanime'
    rotate_user_agent = True
    allowed_domains = ['www6.gogoanime.io']
    start_urls = ['https://www6.gogoanime.io']

<<<<<<< HEAD
    rules = (Rule(sle(allow=''), callback='parse_anime_links', follow=True), )
=======
    rules = (Rule(sle(allow='', deny=(
        '/category/'
        )), callback='parse_anime_links', follow=True), )
>>>>>>> ffe4ee896006b24c40efffa25328a595c9f776d8

    def parse_anime_links(self, response):
        item = []
        item = AjarGogoanimeItem()

        item['episode'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_name.anime_video > div.title_name > h2::text'
                         ).extract()
        item['name_anime'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_video_body_cate > div.anime-info > a::text'
                         ).extract()
        item['download_url'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.download-anime > a::attr(href)'
                         ).extract()
        item['server_1'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(1) > a::attr(data-video)'
                         ).extract()
        item['server_2'] = \
            response.css('#wrapper_bg > section > section.content_left > div:nth-child(1) > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(2) >a::attr(data-video)'
                         ).extract()
        item['server_3'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(3) >a::attr(data-video)'
                         ).extract()
        item['server_4'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(4) >a::attr(data-video)'
                         ).extract()
        item['server_5'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(5) >a::attr(data-video)'
                         ).extract()
        item['server_6'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(6) >a::attr(data-video)'
                         ).extract()
        item['server_7'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(7) >a::attr(data-video)'
                         ).extract()
        item['server_8'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(8) >a::attr(data-video)'
                         ).extract()
        item['server_9'] = \
            response.css('#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(9) >a::attr(data-video)'
                         ).extract()

        return item
