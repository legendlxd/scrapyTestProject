# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstpjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    coverImg = scrapy.Field()
    contentUrl = scrapy.Field()
    
class maoYanItem(scrapy.Item):
    fontUrl = scrapy.Field