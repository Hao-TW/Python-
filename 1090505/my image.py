import scrapy
from scrapy import Request
import json
class ImageSpider(scrapy.spiders):
    BASE_URL = ''
    start_index = o
    #限制最大下載數量,防止用量過大
    MAX_DOWNLOAD_NUM = 1000
    name = 'images' #crawl 的 name
    allowed_domains = ['image.so.com'] #過濾爬取的網域名
    start_urls = [BASE_URL % o]

    def parse(self,response):
        #使用json的模組回應結果
        infos = json.loads(response.body.decode('utf-8'))
        #抓取下載圖片url
        yield{'image_urls':[info['qhimg_url'] for info in infos['list']]}
        #如果下載數量不足MAX_DOWNLOAD_NUM,繼續下載
        self.start_index+=infos['count']
        if infos['count']>0 and self.start_index<MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL% self.start_index)