import scrapy
# from myfirstPj.items import maoYanItem

class maoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = 'maoyan.com'
    start_urls = ['https://maoyan.com/films/1342846']

    def parse(self, response):
        fontList = response.selector.re(r'(//[\w+\.]+\w+/\w+/\w+\.woff)')
        # print(response.html())
        # fontList2 = response.selector.re(r'//vfile.meituan.net/colorstone/(\w+\.woff)')
        print('fontList == > ',fontList)
        # print('fontList2 == > ',fontList2)
