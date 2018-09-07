# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for i_item in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = i_item.xpath(".//div[@class='pic']//em/text()").extract_first()
            douban_item['movie_name'] = i_item.xpath(".//div[@class='hd']//span[1][@class='title']/text()").extract_first()
            content = i_item.xpath(".//div[@class='bd']//p[1]/text()").extract()
            douban_item['introduce'] = "".join(content[1].split())
            douban_item['actor'] = "".join(content[0].split())
            douban_item['star'] = i_item.xpath(".//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i_item.xpath(".//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describe'] = i_item.xpath(".//div[@class='bd']//p[@class='quote']//span/text()").extract_first()

            yield douban_item

        next_link = response.xpath("//div[@class='paginator']//span[@class='next']//a[1]/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)