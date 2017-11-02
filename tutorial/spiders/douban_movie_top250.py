# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from tutorial.items import MovieItem
import re

def str_trim(strs):
    return ''.join(''.join(strs).split())

def str_filter(str):
    return str.translate(dict.fromkeys((ord(c) for c in '\xa0\n\t')))


class MovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']
    base_url = 'http://movie.douban.com/top250'

    def parse(self, response):
        movie_list = response.xpath('//*[@class="grid_view"]/li')
        #yield self.parse_each(movie_list[0])
        for movie in movie_list:
            yield self.parse_each(movie)
        next_url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        print(next_url)
        if next_url:
           yield Request(self.base_url + next_url)


    def parse_each(self, item):
        #print(item)
        movie = item
        movie_item = MovieItem();
        movie_item['ranking'] = movie.xpath('div/div[1]/em/text()').extract_first()
        movie_item['href'] = movie.xpath('div/div[1]/a/@href').extract_first()
        movie_item['image_urls'] = movie.xpath('div/div[1]/a/img/@src').extract()
        movie_item['name'] = str_trim(movie.xpath('div/div[2]/div[1]/a/span/text()').extract()).split('/')
        l1 = movie.xpath('div/div[2]/div[2]/p[1]/text()').extract()[:2]
        describe = re.split(r'导演:|主演:',str_trim(l1[0]))
        movie_item['director'] = describe
        movie_item['actor'] = describe
        describe = str_trim(l1[1]).split('/')
        movie_item['release_year'] = describe[0]
        movie_item['country'] = describe[1]
        movie_item['category'] = describe[2]
        l2 = movie.xpath('div/div[2]/div[2]/div/span/text()').extract()
        movie_item['grade'] = l2[0]
        movie_item['grade_number'] = l2[1].split('人')[0]
        l3 = movie.xpath('div/div[2]/div[2]/p[2]/span/text()').extract()
        movie_item['theme'] = l3
        #print(movie_item)
        print(movie_item['name'])
        return movie_item

