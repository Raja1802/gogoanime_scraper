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

    rules = (Rule(sle(allow='', deny=(
        '/category/',
        '/contact-us.html',
        '/about-us.html',
        '/search.html',
        '/genre/',
        '/login.html',
        '/sub-category/',
        '/forget.html',
        '/privacy.html',
        '/anime-list.html',
        '/new-season.html',
        '/anime-movies.html',
        '/popular.html',
        '/register.html',
    )), callback='parse_anime_links', follow=True),)

    def parse_anime_links(self, response):
        item = []
        item = AjarGogoanimeItem()

        item['episode'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_name.anime_video > div.title_name > h2::text'
                ).extract()
        item['name_anime'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_video_body_cate > div.anime-info > a::text'
                ).extract()
        item['download_url'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.download-anime > a::attr(href)'
                ).extract()
        item['episode_no'] = \
            response.css(
                '#default_ep::attr(value)'
            ).extract()
        item['anime_id'] = \
            response.css(
                '#movie_id::attr(value)'
            ).extract()
        item['server_1'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(1) > a::attr(data-video)'
                ).extract()
        item['server_2'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div:nth-child(1) > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(2) >a::attr(data-video)'
                ).extract()
        item['server_3'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(3) >a::attr(data-video)'
                ).extract()
        item['server_4'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(4) >a::attr(data-video)'
                ).extract()
        item['server_5'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(5) >a::attr(data-video)'
                ).extract()
        item['server_6'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(6) >a::attr(data-video)'
                ).extract()
        item['server_7'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(7) >a::attr(data-video)'
                ).extract()
        item['server_8'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(8) >a::attr(data-video)'
                ).extract()
        item['server_9'] = \
            response.css(
                '#wrapper_bg > section > section.content_left > div > div.anime_video_body > div.anime_muti_link > ul > li:nth-child(9) >a::attr(data-video)'
                ).extract()

        return item
