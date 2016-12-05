import scrapy
from scrapy.loader import ItemLoader
from NASA_wallpaper_collector.items import NASAImg
# from ..items import *

imageURL = 'https://www.spacetelescope.org/images/viewall/page/'
siteURL = 'https://www.spacetelescope.org'

class AllImageIterator(scrapy.Spider):
    name = "downloadAll"

    start_urls = ['https://www.spacetelescope.org/images/viewall/page/1/']

    def parse(self, response):
        for imageHref in response.css('div.image-list a.item').xpath('@href').extract():

            yield scrapy.Request(response.urljoin(imageHref), callback=self.parse_image)

        next_page = response.css('div.prev-next a').xpath('@href').extract()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_image(self, response):
        jpgURL = response.css('div.archive_download span.archive_dl_text a').xpath('@href').extract()[-1]
        jpgName = response.css('h1::text').extract()[0]

        item = NASAImg()
        item['image_urls'] = [jpgURL]
        return item
