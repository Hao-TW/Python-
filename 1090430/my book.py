import scrapy
from scrapy.linkextractors import Linkextractor
from ..items import BookItem
class BookSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_url = 'http://books.toscrape.com/'
    #書及列表的 function
    def parse(self,response):
        #抓取每本書的 link
        le = Linkextractor(restrict_css = 'article.product_pod h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback = self.parse_book)
        #抓取下一頁 link
            le = Linkextractor(restrict_css = 'ul.pager li.next')
            links = le.extract_links(response)
            if links:
                next_url = links[o].url
                yield scrapy.Request(next_url,callbook = self.parse)
    #書籍的5個項目抓取
    def parse_book(self,response):
        book = BookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['price'] = sel.css('p.price_color::text').extract_first()
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating([A-Za-z]+)')
        sel = response.css('table.table.table-striped')
        book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\(\\d+) arailable')
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()
        yield book