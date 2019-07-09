#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import pdfdrive


class QuotesSpider(CrawlSpider):

    name = 'pdf'
    allowed_domains = ['www.pdfdrive.com']
    start_urls = ['https://www.pdfdrive.com/']

    rules = (Rule(sle(allow='', deny=('/auth/', '/home/', '/search\?',
             '/category/')), callback='parse_anime', follow=True), )

    def parse_anime(self, response):
        item = []
        item = pdfdrive()

        # item['name'] = \
        #     response.css('#main > div > div.widget.info > div > div:nth-child(1)'
        #                  ).get()

        item['main_url'] = response.url
        item['name'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > h1::text'
                         ).get()
        item['image_url'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-left > a > img::attr(src)'
                         ).get()
        item['year_pub'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-file-info > span:nth-child(3)::text'
                         ).get()
        item['total_pages'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-file-info > span:nth-child(1)::text'
                         ).get()
        item['book_size'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-file-info > span:nth-child(5)::text'
                         ).get()
        item['no_downloads'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-file-info > span.info-green.hidemobile::text'
                         ).get()
        item['book_language'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-file-info > span:nth-child(9)::text'
                         ).get()
        item['book_id'] = \
            response.css('#previewButtonMain::attr(data-id)').get()
        item['book_preview'] = \
            response.css('#previewButtonMain::attr(data-preview)').get()
        item['book_buy'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-buttons > div > a::attr(href)'
                         ).get()
        item['book_quotes'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.quotes::text'
                         ).get()
        item['book_author'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-author > a > span::text'
                         ).get()
        item['book_tags'] = \
            response.css('body > div.dialog > div.dialog-main > div.dialog-left > div.ebook-main > div.ebook-right > div > div.ebook-tags > a::text'
                         ).getall()
        item['download_url'] = \
            response.css('#download-button-link::attr(href)').get()
        return item
