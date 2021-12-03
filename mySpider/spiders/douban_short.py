import scrapy

from mySpider.items import douban_shortItem


class DoubanShortSpider(scrapy.Spider):
    name = 'douban_short'
    allowed_domains = ['douban.com']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    cookies = {
        'bid' : 'O4pY1LfrdQ4',
        'dbcl2' : '186566664:x+8A+d3YF8E',
        'ck' : '66VH',
        '__utmc' : '30149280',
        '__utmz' : '30149280.1637829769.1.1.utmcsr = open.weixin.qq.com | utmccn = (referral) | utmcmd = referral | utmcct = /',
        '__utmc' : '223695111',
        '__utmz' : '223695111.1637829769.1.1.utmcsr = open.weixin.qq.com | utmccn = (referral) | utmcmd = referral | utmcct = /',
        'push_noty_num' : '0',
        'push_doumail_num' : '0',
        '_vwo_uuid_v2' : 'D2991D2B29F982D5180D7339C5FB478E8 | f10f6546c663d597a1c2ca1ccb095062',
        '_pk_ref.100001.4cf6' : '["", "", 1637888803, "https://open.weixin.qq.com/"]',
        '__utma' : '30149280.1031828967.1637829769.1637829769.1637888804.2',
        '__utma' : '223695111.1935566457.1637829769.1637829769.1637888804.2',
        '_pk_id.100001.4cf6' : '7b36a5f51ea7a61e.1637829768.2.1637888855.1637829806.',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/subject/30382416/comments'
        yield scrapy.Request(url, headers=self.headers, cookies=self.cookies)

    def parse(self, response):
        item = douban_shortItem()
        shorts = response.xpath('//div[@id="comments"]/div')
        for short in shorts:
            try:
                item['votes'] = short.xpath(
                    './/div[2]/h3/span[1]/span/text()').extract()[0]
                item['id'] = short.xpath(
                    './/div[2]/h3/span[2]/a/text()').extract()[0]
                item['rating'] = short.xpath(
                    './/div[2]/h3/span[2]/span[2]/@class').re(u'\d')[0]
                item['date'] = short.xpath(
                    './/div[2]/h3/span[2]/span[3]/text()').extract()[0].strip()
                item['content'] = short.xpath(
                    './/div[2]/p/span/text()').extract()[0]
                yield item
            except:
                pass

        next_url = response.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/subject/30382416/comments' + next_url[0]
            yield scrapy.Request(next_url, headers=self.headers, cookies=self.cookies)
