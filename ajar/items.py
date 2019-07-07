#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.aorg/en/latest/topics/items.html

import scrapy


# 9naime anime info downloader

class AjarItem(scrapy.Item):

    name = scrapy.Field()
    image = scrapy.Field()
    synonyms = scrapy.Field()
    types = scrapy.Field()
    studios = scrapy.Field()
    aired = scrapy.Field()
    status = scrapy.Field()
    scores = scrapy.Field()
    premired = scrapy.Field()
    durination = scrapy.Field()
    quality = scrapy.Field()
    gener = scrapy.Field()
    about = scrapy.Field()
    tags = scrapy.Field()
    cover = scrapy.Field()


# pixabay images links grabber

class AjarPixabayItem(scrapy.Item):

    img_srcset = scrapy.Field()
    img_src = scrapy.Field()
    img_tags = scrapy.Field()


# gogo anime urls collector

class AjarGogoanimeItem(scrapy.Item):

    anime_name = scrapy.Field()
    name_episode = scrapy.Field()
    download_url = scrapy.Field()
    server_name_1 = scrapy.Field()
    server_url_1 = scrapy.Field()
    server_name_2 = scrapy.Field()
    server_url_2 = scrapy.Field()
    server_name_3 = scrapy.Field()
    server_url_3 = scrapy.Field()
    server_name_4 = scrapy.Field()
    server_url_4 = scrapy.Field()
    server_name_5 = scrapy.Field()
    server_url_5 = scrapy.Field()
    server_name_6 = scrapy.Field()
    server_url_6 = scrapy.Field()
    server_name_7 = scrapy.Field()
    server_url_7 = scrapy.Field()
    server_name_8 = scrapy.Field()
    server_url_8 = scrapy.Field()
    server_url_9 = scrapy.Field()


class AjarAnilistItem(scrapy.Item):

    image_url = scrapy.Field()


class AjarWallAlphaItem(scrapy.Item):

    image_url = scrapy.Field()
    image_tags = scrapy.Field()
    image_type = scrapy.Field()


class DatabloggerScraperItem(scrapy.Item):

    # The source URL

    aloc = scrapy.Field()

    # The destination URL

    url_to = scrapy.Field()
    changefreq = scrapy.Field()
    priority = scrapy.Field()


class anime_planet_character(scrapy.Item):

    name = scrapy.Field()
    gender = scrapy.Field()
    hair_color = scrapy.Field()
    image_url = scrapy.Field()
    about = scrapy.Field()
    tags = scrapy.Field()
    anime_roles = scrapy.Field()
    manga_roles = scrapy.Field()


class pdfdrive(scrapy.Item):

    main_url = scrapy.Field()
    name = scrapy.Field()
    image_url = scrapy.Field()
    total_pages = scrapy.Field()
    year_pub = scrapy.Field()
    book_size = scrapy.Field()
    no_downloads = scrapy.Field()
    book_language = scrapy.Field()
    book_id = scrapy.Field()
    book_preview = scrapy.Field()
    book_buy = scrapy.Field()
    book_quotes = scrapy.Field()
    book_tags = scrapy.Field()
    book_author = scrapy.Field()
    download_url = scrapy.Field()

# 9naime anime info downloader

class AjarItem(scrapy.Item):

    name = scrapy.Field()
    image = scrapy.Field()
    english = scrapy.Field()
    japan = scrapy.Field()
    types = scrapy.Field()
    aired = scrapy.Field()
    status = scrapy.Field()
    episodes = scrapy.Field()
    premired = scrapy.Field()
    durination = scrapy.Field()
    gener = scrapy.Field()
    about = scrapy.Field()
    rating = scrapy.Field()
    tracker = scrapy.Field()


# pixabay images links grabber

class AjarPixabayItem(scrapy.Item):

    img_srcset = scrapy.Field()
    img_src = scrapy.Field()
    img_tags = scrapy.Field()


# gogo anime urls collector

class AjarGogoanimeItem(scrapy.Item):

    name_anime = scrapy.Field()
    episode = scrapy.Field()
    download_url = scrapy.Field()
    server_1 = scrapy.Field()
    server_2 = scrapy.Field()
    server_3 = scrapy.Field()
    server_4 = scrapy.Field()
    server_5 = scrapy.Field()
    server_6 = scrapy.Field()
    server_7 = scrapy.Field()
    server_8 = scrapy.Field()
    server_9 = scrapy.Field()


class AjarAnilistItem(scrapy.Item):

    image_url = scrapy.Field()


class AjarWallAlphaItem(scrapy.Item):

    image_url = scrapy.Field()
    image_tags = scrapy.Field()
    image_type = scrapy.Field()
    image_id = scrapy.Field()
    image_pixels = scrapy.Field()
    image_filesize = scrapy.Field()




class MalItem(scrapy.Item):

    # define the fields for your item here like:

    name = scrapy.Field()
    image = scrapy.Field()
    japan_name = scrapy.Field()
    types = scrapy.Field()
    episodes = scrapy.Field()
    status = scrapy.Field()
    aired = scrapy.Field()
    premired = scrapy.Field()
    studios = scrapy.Field()
    source = scrapy.Field()
    gener = scrapy.Field()
    durination = scrapy.Field()
    rating = scrapy.Field()
    scores = scrapy.Field()
    about = scrapy.Field()
    trailer = scrapy.Field()


class AniList(scrapy.Item):
    Anime_url = scrapy.Field()


class gogoanime_info(scrapy.Item):
    image_url = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    plot = scrapy.Field()
    gener = scrapy.Field()
    aired = scrapy.Field()
    status = scrapy.Field()
    other_name = scrapy.Field()
    url_name = scrapy.Field()