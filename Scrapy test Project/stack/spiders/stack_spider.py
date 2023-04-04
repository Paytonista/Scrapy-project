from scrapy import Spider
from scrapy.selector import Selector


from stack.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains= ["books.toscrape.com"]
    start_urls=["http://books.toscrape.com/"]
    def parse(self, response):
        bookTitles = Selector(response).xpath("//article[@class='product_pod']//h3")

        for bookTitle in bookTitles:
            item = StackItem()
            item['bookTitle'] = bookTitle.xpath("a/@title").extract()[0]
            item['bookPrice'] = bookTitle.xpath("//p[@class='price_color']").extract()[0]
            yield item

            next_page_url = response.xpath("//li[@class='next']/a/@href")
            if next_page_url:
              yield response.follow(next_page_url[0], callback=self.parse)


        
