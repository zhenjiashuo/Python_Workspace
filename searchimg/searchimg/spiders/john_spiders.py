#!/user/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import re
import os
import urllib.request
from scrapy.selector import Selector
from scrapy.http import HtmlResponse, Request

class JohnSpider(scrapy.spiders.Spider):
    name = "john"
    allowed_domains = ["mm131.com"]
    start_urls = ["http://www.mm131.com/xiaohua/",]

    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
        hxs = Selector(response)

        items = hxs.xpath("//div[@class='main']/dl[@class='list-left public-box']/dd")

        for i in range(len(items)):
            imgurl = hxs.xpath("//div[@class='main']/dl[@class='list-left public-box']/dd//a/@href")[i].extract()
            src = hxs.xpath("//div[@class='main']/dl[@class='list-left public-box']/dd//a/img/@src")[i].extract()
            name = hxs.xpath("//div[@class='main']/dl[@class='list-left public-box']/dd//a/img/@alt")[i].extract()

            print ("src is : %s "%src )

            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
            #src = "http://p.666ccc.com/upload/s0/2857-20862c6d5cd0e68eacd4b42b1b034ab0.jpg"
            req = urllib.request.Request(url=src, headers=headers)
            html = urllib.request.urlopen(req).read()

            if src:
                file_name = "%s.jpg" %name
                file_path = os.path.join("E:\Github\Python_Workspace\searchimg\data",file_name)
                #urllib.request.urlretrieve("http://p.666ccc.com/upload/s0/2857-20862c6d5cd0e68eacd4b42b1b034ab0.jpg",file_path)
                #html = urllib.request.urlopen(req).read()
                with open(file_path, 'wb') as f:
                    f.write(html)

                print ("* : %s "%src )
