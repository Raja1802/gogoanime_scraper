#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AjarWallAlphaItem


class QuotesSpider(CrawlSpider):

    name = 'pics'
    allowed_domains = ['wall.alphacoders.com']
    start_urls = ['https://wall.alphacoders.com/']

    rules = (Rule(sle(allow='', deny=(
        'galleries',
        'profile',
        'search',
        'by_collection',
        'popular_searches',
        'users',
        'popular',
        'sub_categories',
        'index',
        'translate',
        'newest_wallpapers',
        'captions',
        'highest_rated',
        'language',
        'themes',
        'add_caption',
        'editor',
        'by_sub_gallery',
        'by_gallery',
        'featured',
        'by_license',
        'random',
        'authors',
        'random',
        'by_creator',
        'comments',
        'by_views',
        'by_category',
        'by_resolution',
        'by_category',
        'by_sub_category',
        'tags',
        'by_color',
        'favorites',
        )), callback='parse_images', follow=True), )

    def parse_images(self, response):
        image = []
        image = AjarWallAlphaItem()

        image['image_url'] = \
            response.css('#page_container > div.center.img-container-desktop > a::attr(href)'
                         ).get()
        image['image_tags'] = \
            response.css('#list_tags > div.tag-element > a::text'
                         ).getall()
        image['image_type'] = \
            response.css('#page_container > div.center > h2 > a::attr(title)'
                         ).get()
        image['image_id'] = \
            response.css('#page_container > div.wallpaper-options > div.main-container > span::attr(data-id)'
                         ).get()
        image['image_pixels'] = \
            response.css('#wallpaper_info_table > tbody > tr:nth-child(3) > td:nth-child(2) > span > span:nth-child(2) > a::text'
                         ).get()
        image['image_filesize'] = \
            response.css('#wallpaper_info_table > tbody > tr:nth-child(3) > td:nth-child(2) > span > span:nth-child(3)::text'
                         ).get()
        return image
