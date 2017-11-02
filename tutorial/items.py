# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field()
    href = scrapy.Field()
    image_urls = scrapy.Field() #image url
    image_paths = scrapy.Field() #image save path
    name = scrapy.Field()
    director = scrapy.Field()
    actor = scrapy.Field()
    release_year = scrapy.Field()
    country = scrapy.Field()
    category = scrapy.Field()
    grade = scrapy.Field()
    grade_number = scrapy.Field()
    theme = scrapy.Field()
    pass

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
