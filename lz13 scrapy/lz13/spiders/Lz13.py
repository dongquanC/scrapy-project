# -*- coding: utf-8 -*-
import scrapy
from lz13.items import Lz13Item

class Lz13Spider(scrapy.Spider):
    name = 'Lz13'
    allowed_domains = ['www.lz13.cn']
    start_urls = ['https://www.lz13.cn/']

    def parse(self, response):
        print("Lz13Spider start.")
        li = response.xpath('//ul[@class = "cmList"]/li')
        for l in li:
            txt = l.xpath('a/text()').extract()
            href = l.xpath('a/@href').extract()[0]
            yield scrapy.Request(url = href,meta={'txt':txt[0]}, callback = self.href_parse)
   
    def href_parse(self,response):
        print("href_parse start.")
        Lz13 = Lz13Item()
        Lz13['txt'] = response.meta['txt']
        content = response.xpath("//div[@class = 'PostContent']/p/text()").extract()
        content = ''.join(content)
        Lz13['content'] = content
        yield Lz13
        
