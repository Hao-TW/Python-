import scrapy
from scrapy import Request
import json


class ImagesSpider(scrapy.Spider):
    BASE_URL = 'https://image.so.com/zj?ch=home&sn=%s&listtype=new&temp=1'
    start_index = 0

    
    MAX_DOWNLOAD_NUM = 10

    name = "images"
    allowed_domains = ["image.so.com"]
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        
        infos = json.loads(response.body.decode('utf8'))
        
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}

        
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.start_index)