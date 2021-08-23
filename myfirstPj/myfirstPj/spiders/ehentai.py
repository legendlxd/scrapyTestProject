import scrapy
from myfirstPj.items import MyfirstpjItem
class EhentaiSpider(scrapy.Spider):
    name = 'ehentai'
    allowed_domains = ['e-hentai.org']
    start_urls = ['https://e-hentai.org/tag/webtoon']
    # start_urls = ['https://baidu.com']
    # def start_requests(self):
    #     proxy = "http://13.213.74.144:9090"
    #     yield scrapy.Request(self.start_urls[0],meta={"proxy":proxy})
    def parse(self, response):
        items = MyfirstpjItem()
        lists = response.xpath('//div[@class="glthumb"]/div/img')
        titleLists = response.xpath('//div[@class="glink"]')
        ContentUrls = response.xpath('//td[@class="gl3c glname"]/a/@href')
        index = 0
        for i in lists:
            items['coverImg']=i.xpath('/@src')
            items['title']=titleLists[index]
            items['contentUrl']=ContentUrls[index]
            index += 1
            yield items
        
