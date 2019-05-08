# -*- coding: utf-8 -*-

import sys
import time
import urllib
import urllib2
import smtplib
import importlib
import uuid
from email.mime.text import MIMEText
from email.utils import formatdate
from email.header import Header
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from aliyunsdk_SingleCallByTtsRequest import SingleCallByTtsRequest
from dingtalkchatbot.chatbot import DingtalkChatbot
from util import logger

def alert_channel_sms(contactor, msg):
    data = {
        'account': "youraccount",
        'pswd': "yourpswd",
        'needstatus': "true",
        'msg': msg,
        'mobile': contactor,
    }
    data = urllib.urlencode(data).encode('utf-8')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }
    alert_url = urllib2.Request('http://yourip/msg/HttpBatchSendSM', data, headers)
    rest = urllib2.urlopen(alert_url)
    logger.info('sms -> '+ contactor + ",msg -> " + msg)

def alert_channel_mail(contactor,msg):
    default_encoding = 'utf-8'
    if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)

    smtpHost = 'smtp.exmail.qq.com'
    smtpPort = '25'
    sslPort = '465'
    fromMail = 'yourname@sina.com'
    username = 'yourname@sina.com'
    password = 'yourpwd'

    def send_mail(to_list, subject, content):
        encoding = 'utf-8'
        mail = MIMEText(content.encode(encoding), 'plain', encoding)
        mail['Subject'] = Header(subject, encoding)
        mail['From'] = fromMail
        mail['To'] = to_list
        mail['Date'] = formatdate()

        try:
            smtp = smtplib.SMTP_SSL(smtpHost, sslPort)
            smtp.ehlo()
            smtp.login(username, password)
            smtp.sendmail(fromMail, to_list, mail.as_string())
            smtp.close()
        except Exception as e:
            print("e")

    send_mail(contactor, msg, '')
    logger.info('mail -> '+ contactor + ",msg -> " + msg)


def alert_channel_voice(contactor):

    REGION = "cn-hangzhou"
    PRODUCT_NAME = "Dyvmsapi"
    DOMAIN = "dyvmsapi.aliyuncs.com"

    # ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
    ACCESS_KEY_ID = "yourkeyid"
    ACCESS_KEY_SECRET = "yourkeysecret"

    # 阿里云的语音报警系统用哪个固定电话呼出
    aliyun_show_number = "02566825180"

    # 阿里云的语音报警系统用哪个语音模版呼出
    aliyun_tts_code = "TTS_11111"

    acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
    region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)

    def tts_call(business_id, called_number, called_show_number, tts_code, tts_param=None):
        ttsRequest = SingleCallByTtsRequest()
        # 申请的语音通知tts模板编码,必填
        ttsRequest.set_TtsCode(tts_code)
        # 设置业务请求流水号，必填。后端服务基于此标识区分是否重复请求的判断
        ttsRequest.set_OutId(business_id)
        # 语音通知的被叫号码，必填。
        ttsRequest.set_CalledNumber(called_number)
        # 语音通知显示号码，必填。
        ttsRequest.set_CalledShowNumber(called_show_number)
        # tts模板变量参数
        if tts_param is not None:
            ttsRequest.set_TtsParam(tts_param)
        # 调用tts文本呼叫接口，返回json
        ttsResponse = acs_client.do_action_with_exception(ttsRequest)
        return ttsResponse

    __business_id = uuid.uuid1()
    params = ""
    tts_call(__business_id, contactor, aliyun_show_number, aliyun_tts_code, params)
    logger.info('voice -> ' + contactor)


def alert_channel_ding(contactor, msg):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % (contactor)
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(msg)
    logger.info('ding -> '+ contactor + ",msg -> " + msg)
