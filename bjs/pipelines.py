# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from .items import BjsZengZiItem

FILEPREX = '定增项目——'

class BjsPipeline(object):
    def process_item(self, item, spider):
        line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
               "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
               "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
               "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
               "%s"%(item['id'],item['name'],item['location'],item['industry'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz'],
                     item['ygdsfcyzz']
                     )
        return item

    def open_spider(self,spider):
        file_name = FILEPREX+str(datetime.date.today())
        self.fh = open(file_name,'w',encoding='utf-8')

        #写表头
        self.fh.write("项目编号,标的名称,融资方所在地区,融资方所属行业,"
                      "原股东是否参与增资,"
                      "职工是否参与增资,"
                      "拟募集资金总额,"
                      "拟募集资金对应持股比例,"
                      "拟新增注册资本,"
                      "拟征集投资方数量,"
                      "增资后企业股权结构,"
                      "增资方案主要内容,"
                      "增资达成或终止条件,"
                      "信息发布期满的安排,"
                      "募集资金用途,"
                      "住所,"
                      "法定代表人,"
                      "成立日期,"
                      "注册资本,"
                      "实收资本,"
                      "股东个数,"
                      "职工个数,"
                      "经营范围,"
                      "股东名称1,"
                      "出资比例1,"
                      "股东名称2,"
                      "出资比例2,"
                      "股东名称3,"
                      "出资比例3,"
                      "股东名称4,"
                      "出资比例4,"
                      "股东名称5,"
                      "出资比例5,"
                      "股东名称6,"
                      "出资比例6,"
                      "股东名称7,"
                      "出资比例7,"
                      "股东名称8,"
                      "出资比例8,"
                      "股东名称9,"
                      "出资比例9,"
                      "股东名称10,"
                      "出资比例10,"
                      "第一年资产,"
                      "第一年负债,"
                      "第一年所有者权益,"
                      "第一年营业收入,"
                      "第一年营业利润,"
                      "第一年净利润,"
                      "第二年资产,"
                      "第二年负债,"
                      "第二年所有者权益,"
                      "第二年营业收入,"
                      "第二年营业利润,"
                      "第二年净利润,"
                      "第三年资产,"
                      "第三年负债,"
                      "第三年所有者权益,"
                      "第三年营业收入,"
                      "第三年营业利润,"
                      "第三年净利润,"
                      "最近一期财务日期,"
                      "最近一期资产,"
                      "最近一期负债,"
                      "最近一期所有者权益,"
                      "最近一期营业收入,"
                      "最近一期营业利润,"
                      "最近一期净利润,"
                      "融资方决策文件类型,"
                      "国资监管机构,"
                      "国家出资企业或主管部门名称,"
                      "批准单位名称,"
                      "批准文件类型,"
                      "其他需要披露的事项"
                      "投资方资格条件,"
                      "增资条件,"
                      "保证金金额或比例,"
                      "交纳时间,"
                      "保证金处置方式,"
                      "择优方式,"
                      "择优方案主要内容"
                      "\n")

    def close_spider(self,spider):
        self.fh.close()