# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    dt_publish = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    read_count = scrapy.Field()
    comment_count = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    # _id = scrapy.Field()
    stock_id = scrapy.Field()
    uid = scrapy.Field()
    user_url = scrapy.Field()


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    user_id = scrapy.Field()
    name = scrapy.Field()
    stock_count = scrapy.Field()
    following_count = scrapy.Field()
    following_list = scrapy.Field()
    follower_count = scrapy.Field()
    follower_list = scrapy.Field()
    guba_age = scrapy.Field()
    post_count = scrapy.Field()
    level = scrapy.Field()
    is_majia = scrapy.Field()
    intro = scrapy.Field()

