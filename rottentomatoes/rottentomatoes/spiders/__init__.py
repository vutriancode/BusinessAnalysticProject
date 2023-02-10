# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#https://www.rottentomatoes.com/search?search=Rise%20of%20the%20Guardians
#https://www.rottentomatoes.com/search?search=Wrong Turn
import scrapy
import json
from rottentomatoes.items import RottentomatoesItem
class TomatoesSpider(scrapy.Spider): 
    name = "TomatoesSpider" 
    allowed_domains = ["rottentomatoes.com"] 
    list_index = [i*50 + 1 for i in range(140)]
    files = open("imdb.json","r",encoding="utf-8")
    a = json.load(files)
    #    files2 = open("tomatoes.txt","a")
    files2 = open("data1.json","r",encoding="utf-8")
    a2 = json.load(files2)
    list_id = [i["imdb_id"] for i in a2]
    start_urls = [
        "https://www.rottentomatoes.com"
    ]
    start_urls_dict = {}
    for index,i in enumerate(a):
        i["index"] = index
        start_urls_dict["https://www.rottentomatoes.com/search?search={}".format(i["title"])] = i
    def parse(self, response):
        for i in list(self.start_urls_dict.keys()):
            if self.start_urls_dict[i]["index"] not in self.list_id:
                item = RottentomatoesItem()

                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
                # self.index = self.index +1
                # self.files2.write("{}: {}\n".format(self.index,a))
                item["imdb_title"] = self.start_urls_dict[i]["title"]
                item["imdb_id"] = self.start_urls_dict[i]["index"]

                request =  scrapy.Request(i, callback = self.parse_dir_contents,headers = headers)
                request.meta['item'] = item

                yield request
    def parse_dir_contents(self, response):
        response1 = response.xpath('//*[@id="search-results"]/search-page-result/ul/search-page-media-row[1]/a[1]/@href').extract()[0]
        item = response.meta['item']
        item["url"] = response1
        return item
# import requests
# from bs4 import BeautifulSoup
# files = open("imdb.json","r",encoding="utf-8")
# a = json.load(files)
# start_urls = [
#     "https://www.rottentomatoes.com/search?search={}".format(i["title"]) for i in a 
# ]
# files = open("tomatoes.txt","w")
# for id, i in enumerate(start_urls):
#     b = requests.get(i).content.decode("utf-8")
#     bb = BeautifulSoup(b,"html.parser")
#     a = bb.find("search-page-media-row")
#     cc = a.find("a")["href"]
#     print("{}: {}\n".format(id,cc))
#     files.write("{}: {}\n".format(id,cc))