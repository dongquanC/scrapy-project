# -*- coding: utf-8 -*-
import scrapy
from english.items import EnglishItem

class CgdictSpider(scrapy.Spider):
    name = 'cgdict'
    allowed_domains = ['cgdict.com']

    
    # start_urls = ['http://www.cgdict.com/index.php?app=cigen&ac=list&page=1']

    def start_requests(self):
        # self.word_dict = {}
        url = 'http://www.cgdict.com/index.php?app=cigen&ac=list&page='
        for i in range(8):
            yield self.make_requests_from_url(url+str(i+1))
        
        

    def parse(self, response):
        print("out put.")
        item = EnglishItem()
        # print(response.text)
        words = response.xpath('//h2[@class = "clh2"]/a')
        for word in words:
            href = word.xpath('@href').extract()[0]
            w = word.xpath('text()').extract()[0]

            item['href'] = href
            item['w'] = w
            yield item
            # print(href+'++++'+w)
            # self.word_dict[w] = href
        
        # print(self.word_dict)
