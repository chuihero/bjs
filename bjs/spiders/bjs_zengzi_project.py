#coding = utf-8

import scrapy
from collections import OrderedDict
from ..items import BjsZengZiItem

class ZengZiProject(scrapy.Spider):
    name = 'BJS_ZENGZI'

    start_urls = [
        'http://www.cbex.com.cn/ztym/zzkgb/indexcsmore.shtml'
    ]

    def parse(self, response):
        urls = response.xpath('//div[@id="right"]/div[@class="xmxx"]//td[@class="xmbt_name"]/font/a/@href').extract()

        for url in urls:
            yield scrapy.Request(url,callback=self.parse_proj)

        #增加下一页的解析
        next_page = response.xpath('//node()[contains(text(),"下页")]/@href').extract()
        if next_page:
            url = response.urljoin(next_page[0])
            next_page.pop()
            print('解析下一页为：%s'%url)
            yield scrapy.Request(url,self.parse)




    def parse_proj(self,response):
        zengzi = BjsZengZiItem()
        content = response.xpath('//table[@class="gp_info"]')

        start_date = response.xpath('//node()[contains(text(),"项目发布起始日期")]/following::td/text()')[0].extract()
        zengzi['start_date']= start_date.split()[0]
        zengzi['end_date']= response.xpath('//node()[contains(text(),"项目发布截止日期")]/following::td/text()')[0].extract()

        zengzi['id']= content.xpath('//node()[contains(text(),"项目编号")][@class="gp_infoname"]/following::td/text()')[0].extract()
        zengzi['name']= content.xpath('//node()[contains(text(),"标的名称")][@class="gp_infoname"]/following::td/text()')[0].extract()
        location = content.xpath('//node()[contains(text(),"融资方所在地区")][@class="gp_infoname"]/following::td/text()')[0].extract()
        zengzi['location'] = location.split()[0]
        try:
            zengzi['industry'] = content.xpath('//node()[contains(text(),"融资方所属行业")][@class="gp_infoname"]/following::td/text()')[0].extract()
        except:
            print('网页数据解析错误')
            zengzi['industry'] = 'Null'
        try:
            ygdsfcyzz = content.xpath('//node()[contains(text(),"原股东是否参与增资")][@class="gp_infoname"]/following::td/text()')[0].extract()
            zengzi['ygdsfcyzz']= ygdsfcyzz.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['ygdsfcyzz'] = 'Null'
        try:
            zgsfcyzz = content.xpath('//node()[contains(text(),"职工是否参与增资")]/following::td[1]/text()')[0].extract()
            zengzi['zgsfcyzz']= zgsfcyzz.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zgsfcyzz'] = 'Null'
        try:
            nmjzjze = content.xpath('//node()[contains(text(),"拟募集资金总额")]/following::td[1]/text()')[0].extract()
            zengzi['nmjzjze']= nmjzjze.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['nmjzjze'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"拟募集资金对应持股比例")]/following::td[1]/text()')[0].extract()
            zengzi['nmjzjdycgbl']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['nmjzjdycgbl'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"拟新增注册资本")]/following::td[1]/text()')[0].extract()
            zengzi['nxzzczb']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['nxzzczb'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"拟征集投资方数量")]/following::td[1]/text()')[0].extract()
            zengzi['nzjtzfsl']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['nzjtzfsl'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"增资后企业股权结构")]/following::td[1]/text()')[0].extract()
            zengzi['zzhqygqjg']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zzhqygqjg'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"增资方案主要内容")]/following::td[1]/p/text()')[0].extract()
            zengzi['zzfazynr']= ''.join(_temp.split())
        except:
            print('网页数据解析错误')
            zengzi['zzfazynr'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"增资达成或终止的条件")]/following::td[1]/p/text()')[0].extract()
            zengzi['zzdchzzdtj']= ''.join(_temp.split())
        except:
            print('网页数据解析错误')
            zengzi['zzdchzzdtj'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"信息发布期满的安排")]/following::td[1]/text()').extract()
            zengzi['xxfbqmdap']= ''.join([i.split()[0] for i in _temp])
        except:
            print('网页数据解析错误')
            zengzi['xxfbqmdap'] ='Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"募集资金用途")]/following::td[1]/text()')[0].extract()
            zengzi['mjzjyt']= ''.join(_temp.split())
        except:
            print('网页数据解析错误')
            zengzi['mjzjyt'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"住所")]/following::td[1]/text()')[0].extract()
            zengzi['zs']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zs'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"法定代表人")]/following::td[1]/text()')[0].extract()
            zengzi['fddbr']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['fddbr'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"成立日期")]/following::td[1]/text()')[0].extract()
            zengzi['clrq']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['clrq'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"注册资本")]/following::td[1]/text()')[1].extract()
            zengzi['zczb']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zczb'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"实收资本")]/following::td[1]/text()')[0].extract()
            zengzi['sszb']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['sszb'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"股东个数")]/following::td[1]/text()')[0].extract()
            zengzi['gdgs']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['gdgs'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"职工人数")]/following::td[1]/text()')[0].extract()
            zengzi['zgrs']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zgrs'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"经营范围")]/following::td[1]/text()')[0].extract()
            zengzi['jyfw']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['jyfw'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"融资方决策文件类型")]/following::td[1]/p/text()')[0].extract()
            zengzi['rzfjcwjlx']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['rzfjcwjlx'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"国资监管机构")]/following::td[1]/p/text()')[0].extract()
            zengzi['gzjgjg']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['gzjgjg'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"国家出资企业或")]/following::td[1]/p/text()')[0].extract()
            zengzi['gjczqyhzgbmmc']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['gjczqyhzgbmmc'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"批准单位名称")]/following::td[1]/p/text()')[0].extract()
            zengzi['pzdwmc']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['pzdwmc'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"批准文件类型")]/following::td[1]/p/text()')[0].extract()
            zengzi['pzwjlx']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['pzwjlx'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"其他需要披露的事项")]/following::td[1]/text()')[0].extract()
            zengzi['qtxypldsx']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['qtxypldsx'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"投资方资格条件")]/following::td[1]/text()')[1].extract()
            zengzi['tzfzgtj']= ''.join(_temp.split())
        except:
            print('网页数据解析错误')
            zengzi['tzfzgtj'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"增资条件")]/following::td[1]/p/text()')[0].extract()
            zengzi['zztj']= ''.join(_temp.split())
        except:
            print('网页数据解析错误')
            zengzi['zztj'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"保证金金额或比例")]/following::td[1]/text()')[0].extract()
            zengzi['bzjjehbl']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['bzjjehbl'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"交纳时间")]/following::td[1]/text()')[0].extract()
            zengzi['jnsj']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['jnsj'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"保证金处置方式")]/following::td[1]/text()')[0].extract()
            zengzi['bzjczfs']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['bzjczfs'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"择优方式")]/following::td[1]/text()')[0].extract()
            zengzi['zyfs']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zyfs'] = 'Null'
        try:
            _temp = content.xpath('//node()[contains(text(),"择优方案主要内容")]/following::td[1]//text()')[0].extract()
            zengzi['zyfazynr']= _temp.split()[0]
        except:
            print('网页数据解析错误')
            zengzi['zyfazynr'] = 'Null'

        #企业股权处理
        rows = int(content.xpath('//td[contains(text(),"企业股权结构")][@rowspan]/@rowspan')[0].extract())
        _gudongs = content.xpath('//td[contains(text(),"企业股权结构")][@rowspan]/parent::tr//following::tr')[0:rows-1]
        zengzi['qygqjg']= [i.xpath('td/text()').extract() for i in _gudongs]
        # 不满10人的处理
        while len(zengzi['qygqjg'])<10:
            zengzi['qygqjg'].append(['Null','Null'])

        #主要财务处理
        rows = int(content.xpath('//td[contains(text(),"主要财务指标")][@rowspan]/@rowspan')[0].extract())
        times = int((rows-2)/4) -1 # 不算最近一期在内
        _years = content.xpath('//td[contains(text(),"主要财务指标")][@rowspan]/parent::tr/following::tr')[0:(4*times):4]
        years = [i.xpath('td[@rowspan]/text()')[0].extract() for i in _years]

        _temp = content.xpath('//td[contains(text(),"主要财务指标")][@rowspan]/parent::tr/following::tr')[1:(4*times):2]
        caiwushuju = [i.xpath('td/text()').extract() for i in _temp]

        # 最近一期财务数据
        _date = content.xpath('//td[contains(text(),"最近一期财务数据")][@colspan]/parent::tr/following::tr[1]/td[1]/text()')[0].extract()
        last_date = _date.split()[0]
        _caiwu = content.xpath('//td[contains(text(),"最近一期财务数据")][@colspan]/parent::tr/following::tr')[1:4:2]
        _last_caiwu = [i.xpath('td/text()').extract() for i in _caiwu]
        _last_caiwu[0] = [i.split()[0] for i in _last_caiwu[0]]
        last_caiwu = _last_caiwu[0].copy()
        last_caiwu.extend(_last_caiwu[1] if _last_caiwu[1] else ['0','0','0'])


        # zengzi['zycwzb']= OrderedDict()
        zengzi['zycwzb']= []
        for index in range(len(years)):
            if years[index]:
                _d = caiwushuju[index*2].copy()
                _d.extend(caiwushuju[index*2+1])
                zengzi['zycwzb'].append([years[index],_d])
        # 不满三年的处理
        while len(zengzi['zycwzb'])<3:
            zengzi['zycwzb'].append(['Null',['0','0','0','0','0','0']])
        #最近财务数据
        zengzi['zycwzb'].append([last_date, last_caiwu])



        yield zengzi


















