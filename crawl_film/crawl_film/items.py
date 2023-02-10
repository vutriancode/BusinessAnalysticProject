# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# https://stackoverflow.com/questions/13910357/how-can-i-use-multiple-requests-and-pass-items-in-between-them-in-scrapy-python/25571270#25571270
import scrapy
from scrapy.item import Item, Field

class ImdbFilmItem(scrapy.Item):
    title = scrapy.Field()
    imdb_link = scrapy.Field()
    imdb_rating = scrapy.Field()
    plot_description = scrapy.Field()
    budget = scrapy.Field()
    box_office_gross = scrapy.Field()
    opening_weekend_gross = scrapy.Field()
    actors = scrapy.Field()
    directors = scrapy.Field()
    gross_us_canada = scrapy.Field()
    opening_weekend_us_canada = scrapy.Field()
    gross_worldwide = scrapy.Field()
