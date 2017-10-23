# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BjsZengZiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id  = scrapy.Field()
    name  = scrapy.Field()
    location  = scrapy.Field()
    start_date  = scrapy.Field()
    end_date  = scrapy.Field()
    industry  = scrapy.Field()
    nmjzjze  = scrapy.Field()
    nmjzjdycgbl  = scrapy.Field()
    zyfwjg  = scrapy.Field()
    jyjg  = scrapy.Field()

    ygdsfcyzz = scrapy.Field()
    zgsfcyzz = scrapy.Field()
    nxzzczb = scrapy.Field()
    nzjtzfsl = scrapy.Field()
    zzhqygqjg = scrapy.Field()
    zzfazynr = scrapy.Field()
    zzdchzzdtj = scrapy.Field()
    xxfbqmdap = scrapy.Field()
    mjzjyt = scrapy.Field()
    zs = scrapy.Field()
    fddbr = scrapy.Field()
    clrq = scrapy.Field()
    zczb = scrapy.Field()
    sszb = scrapy.Field() #实收资本
    gdgs = scrapy.Field() #股东个数
    zgrs = scrapy.Field() #职工人数
    jyfw = scrapy.Field() #经营范围
    qygqjg = scrapy.Field() # 企业股权结构，用orderdict
    zycwzb = scrapy.Field() # 主要财务指标，用oderdict
    rzfjcwjlx = scrapy.Field() #融资方决策文件类型
    gzjgjg = scrapy.Field() #国资监管机构
    gjczqyhzgbmmc = scrapy.Field() #国家出资企业或主管部门名称
    pzdwmc = scrapy.Field() #批准单位名称
    pzwjlx = scrapy.Field() #批准文件类型
    qtxypldsx = scrapy.Field() #其他需要披露的事项
    tzfzgtj = scrapy.Field() #投资方资格条件
    zztj = scrapy.Field() #增资条件
    bzjjehbl = scrapy.Field() #保证金金额或办理
    jnsj = scrapy.Field() #交纳时间
    bzjczfs = scrapy.Field() #保证金处置方式
    zyfs = scrapy.Field() #择优方式
    zyfazynr = scrapy.Field() #择优方案主要内容








