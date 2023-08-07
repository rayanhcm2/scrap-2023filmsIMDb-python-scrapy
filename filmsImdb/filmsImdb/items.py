# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FilmsimdbItem(scrapy.Item):
    title = scrapy.Field()
    Image = scrapy.Field()
    Catégorie = scrapy.Field() 
    description = scrapy.Field()
    rate_IMDb = scrapy.Field() 
    Realisation = scrapy.Field() 
    Scénario = scrapy.Field() 
