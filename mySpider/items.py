# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class zxzjItem(scrapy.Item):
    title  = scrapy.Field()    # 标题
    link   = scrapy.Field()     # 链接
    update = scrapy.Field()   # 更新至


class doubanItem(scrapy.Item):
    ranking    = scrapy.Field()  # 排名
    movie_name = scrapy.Field()  # 电影名称
    score      = scrapy.Field()  # 评分
    score_num  = scrapy.Field()  # 评论人数


class douban_shortItem(scrapy.Item):
    votes   = scrapy.Field()  # 有用投票
    id      = scrapy.Field()  # 用户ID
    rating  = scrapy.Field()  # 用户打分
    date    = scrapy.Field()  # 短评日期
    content = scrapy.Field()  # 短评内容
