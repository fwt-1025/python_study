# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    goodsName = scrapy.Field()
    goodsPrice = scrapy.Field()
    pass
