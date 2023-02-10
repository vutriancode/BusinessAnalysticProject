# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#https://www.imdb.com/search/title/?release_date=2010-01-01,2022-12-31&sort=boxoffice_gross_us,desc
import scrapy  
from crawl_film.items import ImdbFilmItem
class IMDBSpider(scrapy.Spider): 
   name = "IMDBSpider" 
   allowed_domains = ["imdb.com"] 
   list_index = [i*50 + 1 for i in range(140)]
   start_urls = [
      "https://www.imdb.com/search/title/?release_date=2010-01-01,2022-12-31&sort=boxoffice_gross_us,desc&start={}".format(i) for i in list_index 
   ]  
   def parse(self, response):
        for sel in response.xpath('//*[@id="main"]/div/div[3]/div/div'):
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

            item = ImdbFilmItem()
            item["title"] = sel.xpath('div[3]/h3/a/text()').extract()[0]
            imdb_link = "https://www.imdb.com"+sel.xpath('div[3]/h3/a/@href').extract()[0]
            item["directors"] = {
                "imdb_link":sel.xpath('div[3]/p[3]/a[1]/@href').extract()[0],
                "name":sel.xpath('div[3]/p[3]/a[1]/text()').extract()[0]
            }
            try:
                item["box_office_gross"] = sel.xpath('div[3]/p[4]/span[5]/@data-value').extract()[0]
            except:
                pass
            try:
                item["imdb_rating"] = sel.xpath("div[3]/div/div[1]/strong/text()").extract()[0]
            except:
                pass
            request =  scrapy.Request(imdb_link, callback = self.parse_dir_contents,headers = headers)
            request.meta['item'] = item
            yield request

   def parse_dir_contents(self, response):
        item = response.meta['item']
        try:
            item['plot_description'] = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[3]/text()').extract()[0]
        except:
            pass
        try:
            h = response.css('section[data-testid="BoxOffice"]')[0]
            print(h.xpath('div[2]/ul/li'))
            for i in h.xpath('div[2]/ul/li'):
                item[i.xpath("button/text()").extract()[0].lower().replace(" & ","_").replace(" ","_")] = i.xpath("div/ul/li/label/text()").extract()[0]
        except:
            pass
        return item