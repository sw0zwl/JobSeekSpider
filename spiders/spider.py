from scrapy import Spider
from scrapy.selector import Selector
from testSeek.items import JobItem

class JobSpider(Spider):
    name = 'jobs'
    allow_domains = ['seek.com.au']
    start_urls = [
    'https://www.seek.com.au/jobs?keywords=software+engineer'
    ]

    def parse(self, reponse):
        titles = reponse.xpath('//article')
        items = []

        for each in titles:
            item = JobItem()
            item["title"] = each.xpath('span[2]/span/h1/a/text()').extract()
            item["link"] = each.xpath('span[2]/span/h1/a/@href').extract()
            print item['title'], item['link']
            items.append(item)
            
        return items