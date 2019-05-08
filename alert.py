# -*- coding: utf-8 -*-

import sys
import urlparse
import time
import re
from config import get_contact_by_domain
from config import get_dingtoken_by_domain
from alert_channel import alert_channel_mail
from alert_channel import alert_channel_sms
from alert_channel import alert_channel_voice
from alert_channel import alert_channel_ding

class Alert(object):
    def __init__(self,rule):
        self.level = rule['level']
        self.domain = rule['domain']
        self.rulename = rule['rulename']
        self.type = rule['type']
        self.num_events = rule['num_events']
        self.timeframe = rule['timeframe']
        self.status = rule.get('status',None)
        self.reqtime_gt = rule.get('reqtime_gt',None)
        self.make_contactor()
        self.make_msg()


    def make_contactor(self):
        self.contacts_mail = get_contact_by_domain(self.domain,'mail')
        self.contacts_phone = get_contact_by_domain(self.domain, 'phone')
        self.contacts_ding = get_dingtoken_by_domain(self.domain)


    def make_msg(self):
        """
        get msg by rulename
        freq-status-*, warning: sina_www status of 500 exceed 30 per 2min
        freq-reqtime-*, warning: sina_www request time greater than 5sec exceed 30 per 2min
        """
        if re.match("freq-status-", self.rulename):
            self.msg = "%s: %s status of %s exceed %s per %s" % \
                       (self.level, self.domain, self.status, self.num_events, self.timeframe)
        elif re.match("freq-reqtime-", self.rulename):
            self.msg = "%s: %s request time greater than %s exceed %s per %s" % \
                       (self.level, self.domain, self.reqtime_gt, self.num_events, self.timeframe)
        else:
            self.msg = ''

    def send_alert_by_email(self):
        for contact in self.contacts_mail:
            alert_channel_mail(contact, self.msg)

    def send_alert_by_ding(self):
        for contact in self.contacts_ding:
            alert_channel_ding(contact, self.msg)

    def send_alert_by_sms(self):
        for contact in self.contacts_phone:
            alert_channel_sms(contact,self.msg)

    def send_alert_by_voice(self):
        for contact in self.contacts_phone:
            alert_channel_voice(contact)

    def alert(self):
        self.send_alert_by_ding()
        self.send_alert_by_email()
        self.send_alert_by_sms()
        if self.level == 'disaster':
            self.send_alert_by_voice()

