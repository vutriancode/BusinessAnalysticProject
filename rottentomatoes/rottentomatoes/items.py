# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RottentomatoesItem(scrapy.Item):
    imdb_title = scrapy.Field()
    imdb_id = scrapy.Field()
    url = scrapy.Field()
    tomatometer_score = scrapy.Field()
    audience_score = scrapy.Field()
    tomatometer_review = scrapy.Field()
    audience_number = scrapy.Field()
    genre = scrapy.Field()
    original_language= scrapy.Field()
    theater_release_date = scrapy.Field()
    streaming_release_date = scrapy.Field()
    runtime = scrapy.Field()
    cast = scrapy.Field()

