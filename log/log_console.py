#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/22 16:17
# @Author  : CoLoDoo
# @Site    : 
# @File    : log_console.py
# @Software: PyCharm

import color

class LogConsole:

    # 初始化
    def __init__(self):
        self.clr = color.Color()

    # 打印日志
    def print_log(self, log, type):
        # 正常日志
        if type == 'ok':
            self.clr.print_blue_text((self.get_log(log)))
        if type == 'error':
            self.clr.print_red_text(self.get_log(log))
        if type == 'warming':
            self.clr.print_green_text(self.get_log(log))

    # 取得日志信息
    def get_log(self, log):
        re_log = '[*] ' + log
        return re_log

    # 清理本地日志
    def clear_log(self):
        pass