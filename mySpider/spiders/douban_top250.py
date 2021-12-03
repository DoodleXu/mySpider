import scrapy
from mySpider.items import doubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    cookies = {
        '_vwo_uuid_v2': 'D879F5A2D116F5DBF97427A0ECEA0313C|2b302d05bc8701716e541cc071946558',
        'push_doumail_num': '0',
        'push_noty_num': '0',
        'ap_v': '0,6.0',
        'ck': 'rj3Y',
        'douban-fav-remind': '1',
        'dbcl2': '186566664:L9PMCgw9S90',
        'll': '118267',
        'bid': 'Ru48Ls-AxCw',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers, cookies=self.cookies)

    def parse(self, response):
        item = doubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(u'(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url, headers=self.headers)