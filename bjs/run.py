#coding=utf-8
# from scrapy.cmdline import execute
import datetime
# from .mail import Mail
#
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import json
import sys
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
# from email.utils import parseaddr, formataddr
import smtplib
from socket import timeout


class Mail():
    def __init__(self,config_file=None):
        if config_file is not None:
            self.config(config_file)
            self.login()


    def config(self,config_file):
        """
        读取配置文件信息，配置邮箱的发送地址，服务器，密码等
        :param config_file:
        :return:
        """
        try:
            with open(config_file) as f:
                mailCfg = json.load(f)
        except:
            print('无法载入邮件配置信息，请检查')
            sys.exit(-1)

        self.fromaddr = mailCfg['fromaddr']
        self.to = mailCfg['to']
        self.passwd = mailCfg['passwd']
        self.server = mailCfg['server']

    def compose(self,title,main_msg,paylaod_dict={}):
        """
        封装邮件，填写标题，内容，附加附件
        :param title:
        :param main_msg:
        :param paylaod_dict: {name:file_path}
        :return:
        """
        self.msg = MIMEMultipart()
        self.msg['From'] = self.fromaddr
        self.msg['To'] = self.to
        self.msg['Subject'] = Header(title, 'utf-8').encode()

        payloadindex = 0
        payloadtxt = ''
        for file_name,file in paylaod_dict.items():
            with open(file, 'rb') as f:
                # 设置附件的MIME和文件名，这里是png类型:
                mime = MIMEBase('text', 'csv', filename=file_name)
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename=file_name)
                mime.add_header('Content-ID', '<%s>' % (payloadindex))
                mime.add_header('X-Attachment-Id', '%s' % (payloadindex))
                # 把附件的内容读进来:
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                self.msg.attach(mime)

                # 设置正文中对附件的应用
                # payloadtxt += '<p><img src="cid:%s"></p>' % (payloadindex)
            # 附件引用自增1
            # payloadindex += 1
        # mailtxt = '<html><body><h1>%s</h1>' % (main_msg) + payloadtxt + '</body></html>'
        mailtxt = main_msg
        self.msg.attach(MIMEText(mailtxt, 'plain', 'utf-8'))

    def login(self,timeout=30*60):
        self.mail_service = smtplib.SMTP(self.server, 25)
        # server.set_debuglevel(1)
        self.mail_service.login(self.fromaddr, self.passwd)

    def _send(self,send_to):
        self.mail_service.sendmail(self.fromaddr, send_to, self.msg.as_string())

    def send(self,send_to=None):
        if send_to is None:
            send_to = self.to

        try:
            self._send(send_to)
        except:
            self.login()
            self._send(send_to)



if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl('BJS_ZENGZI')
    process.start() # the script will block here until the crawling is finished

    FILEPREX = '定增项目_'
    mail_server = Mail('mailConfig.json')
    file = FILEPREX+str(datetime.date.today())+'.csv'
    paylad={file:os.path.join(os.getcwd(),file)}
    mail_server.compose('定增项目更新-%s'%str(datetime.date.today()),'请检查附件',paylad)
    mail_server.send()
