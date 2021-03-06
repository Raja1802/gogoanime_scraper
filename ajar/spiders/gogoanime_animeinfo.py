#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import gogoanime_info


class QuotesSpider(CrawlSpider):

    name = 'gogoinfo'
    rotate_user_agent = True
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
        item['anime_id_info'] = \
            response.css('#movie_id::attr(value)').extract()
        #episode
        #data
        #start
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
        item['anime_id_episode'] = \
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

        # item['url_name'] = \
        #     response.request.url
        return item
