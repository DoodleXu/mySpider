import re
import scrapy
from bs4 import BeautifulSoup
from mySpider.items import zxzjItem

class zxzjSpider(scrapy.Spider):
    name = 'zxzj'
    allowed_domains = ['zxzj.fun']
    start_urls = ['https://www.zxzj.fun/list/3-1.html']

    def parse(self, response):
        pattern = re.compile(r'-\d+.html">尾')
        num_pattern = re.compile(r'\d+')
        last_page = num_pattern.search(pattern.search(response.text).group()).group() # 最大页
        for page in range(1, int(last_page)):
            next_page_url = f'https://www.zxzj.fun/list/3-{page}.html'
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_children)

    def parse_children(self, response):
        item = zxzjItem()
        soup = BeautifulSoup(response.text, "html.parser")
        all_a = soup.find_all(class_="stui-vodlist__thumb lazyload")
        for a in all_a:
            item['title'] = a['title']
            item['update'] = a.get_text() # 获取子标签内所有文本
            item['link'] = a['data-original']
            yield item
