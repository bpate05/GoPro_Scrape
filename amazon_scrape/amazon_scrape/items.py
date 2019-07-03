# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    review_id = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    text = scrapy.Field()

