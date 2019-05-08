#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import argparse
from config import load_contact
from alert import Alert


class Alarm():

    def parse_args(self,args):
        parser = argparse.ArgumentParser()
        parser.add_argument('--level',dest='level',help='warning, distater')
        parser.add_argument('--domain',dest='domain',help='for instance: sina_www, if rule_name start with freq-500,then sina_www-501')
        parser.add_argument('--rulename', dest='rulename', help='rulename')
        parser.add_argument('--type', dest='type', help='frequence, flatline')
        parser.add_argument('--num_events', dest='num_events', help='num_events')
        parser.add_argument('--timeframe', dest='timeframe', help='timeframe')
        parser.add_argument('--reqtime_gt', dest='reqtime_gt', help='request time greater than')
        self.args = parser.parse_args(args)

    def __init__(self,args):
        self.rule = {}
        self.parse_args(args)
        self.rule['level'] = self.args.level
        self.rule['domain'] = self.args.domain
        self.rule['rulename'] = self.args.rulename
        self.rule['type'] = self.args.type
        self.rule['num_events'] = self.args.num_events
        self.rule['timeframe'] = self.args.timeframe
        self.rule['reqtime_gt'] = self.args.reqtime_gt
        if re.match('freq-status-500', self.rule['rulename']):
            self.rule['domain'], self.rule['status']=self.rule['domain'].split('-')[0], self.rule['domain'].split('-')[1]


    def start(self):
        alert = Alert(self.rule)
        alert.alert()


def main(args=None):
    if not args:
        args = sys.argv[1:]
    alarm = Alarm(args)
    alarm.start()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
