# -*- coding: utf-8 -*-
from scrapy import Spider
from financial_news.items import FinancialNewsItem

month = '08'
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']


class FinancialNewsSpider(Spider):
    name = "financial_news"
    allowed_domains = ["news.10jqka.com.cn/"]
    start_urls = []
    for day in days:
        start_urls.append("http://news.10jqka.com.cn/today_list/2016"+month+day+"/")

    def parse(self, response):

        news_set = response.xpath('/html/body/div/div/div/ul/li/span')
        for news in news_set:
            item = FinancialNewsItem()
            item['title'] = news.xpath('./a/text()').extract()[0].encode('utf-8')
            item['dt'] = news.xpath('./span/text()').extract()[0].encode('utf-8')
            item['url'] = news.xpath('./a/@href').extract()[0].encode('utf-8')
            # self.log('headline='+news.xpath('./span/text()').encode('gbk'))
            yield item




