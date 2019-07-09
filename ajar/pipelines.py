# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


class AjarPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='remotemysql.com',
            user='RdcCrIy31Z',
            passwd='jp7tDadtfT',
            database='RdcCrIy31Z'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS gogoanime_all_2""")
        self.curr.execute("""create table gogoanime_all_2(
                             episode text,
                             name_anime text,
                             download_url text,
                             anime_id_episode text,
                             episode_no text,
                             server_1 text,
                             server_2 text,
                             server_3 text,
                             server_4 text,
                             server_5 text,
                             server_6 text,
                             server_7 text,
                             server_8 text,
                             server_9 text,
                             
                             image_url text,
                             name text,
                             type text,
                             plot text,
                             gener text,
                             aired text,
                             status text,
                             other_name text,
                             anime_id_info text
                             
                              )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into gogoanime_all_2 values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            ''.join(item['episode']),
            ''.join(item['name_anime']),
            ''.join(item['download_url']),
            ''.join(item['anime_id_episode']),
            ''.join(item['episode_no']),
            ''.join(item['server_1']),
            ''.join(item['server_2']),
            ''.join(item['server_3']),
            ''.join(item['server_4']),
            ''.join(item['server_5']),
            ''.join(item['server_6']),
            ''.join(item['server_7']),
            ''.join(item['server_8']),
            ''.join(item['server_9']),
            #
            ''.join(item['image_url']),
            ''.join(item['name']),
            ''.join(item['type']),
            ''.join(item['plot']),
            ''.join(item['gener']),
            ''.join(item['aired']),
            ''.join(item['status']),
            ''.join(item['other_name']),
            ''.join(item['anime_id_info'])


        ))
        self.conn.commit()
#DELETE FROM table_name WHERE some_column = ''; removes empty items in database
