import scrapy

class imageDownloader(scrapy.Spider):
    name = "imageDownloader"

    def start_requests(self):
        for i in xrange(1, 18):
            url = site + str(i)
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
