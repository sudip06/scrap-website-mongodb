# -*- coding: utf-8 -*-
import scrapy
import re


class GetdataSpider(scrapy.Spider):
    name = 'getdata'
    start_urls = ['http://www.theguardian.com/au']

    def parse(self, response):
        links = response.xpath('//h3[@class="fc-item__title"]')
        for link in links:
            url = link.xpath('./a/@href').get()
            yield scrapy.Request(url, callback=GetdataSpider.parse_nd)
        pass

    """
    Name: parse_nd
    Parameters: response
    Usage: This method gets the main body content, 
    author and all metadata.
    """
    @staticmethod
    def parse_nd(response):
        item = {'Title': (str(response.xpath('//h1/text()').get()).strip() +
                str(response.xpath('//h1/span/text()').get()).strip()
                          ).replace('None', '')}
        xpath1 = '//div[@itemprop="articleBody"]/p'
        xpath2 = '//div[@itemprop="reviewBody"]/p'
        body = response.xpath(xpath1+"|"+xpath2).getall()
        str_content = ''
        for txt in body:
            str_content = str_content+str(GetdataSpider.clean_html(txt).strip()).\
                            replace('\n', '')
        item['Body'] = str_content
        item['Url'] = response.url
        item['Author'] = str(response.xpath('//span[@itemprop="name"]/text()').get()).strip()
        if item['Body'] and len(item['Title']) > 10:
            yield(item)

    """
    Name: clean_html
    Parameters: raw html main content for an article
    Usage: This method removes the html tags from the main content
    """
    @staticmethod
    def clean_html(raw_html):
        cleanr = re.compile('<.*?>')
        clean_text = re.sub(cleanr, '', raw_html)
        return clean_text
