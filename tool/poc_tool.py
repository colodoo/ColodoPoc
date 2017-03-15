#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/12 1:26
# @Author  : CoLoDoo
# @Site    : 
# @File    : poc_tool.py
# @Software: PyCharm

import requests
import json

class PocTool:
    """docstring for PocClass"""
    timeout = 10
    headers = (
        {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:5.0) Gecko/20100101 Firefox/5.0",
         "Accept": "text/plain"},
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"},
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"},
    )
    codes = (
        200, 500, 406, 401
    )

    # 初始化
    def __init__(self, url):
        self.url = url

    # 包含识别
    # 返回结果为0 or 1
    def check_key_in_value(self, key, value):
        if key in value:
            return 1
        else:
            return 0

    # 取得相应请求
    # 返回结果为请求
    def get_request(self, url='', headerNum=0):
        tmp_url = url if url != '' else self.url
        if headerNum != 0:
            request = requests.get(tmp_url, headers=self.headers[headerNum], timeout=self.timeout)
        else:
            request = requests.get(tmp_url, headers=self.headers[0], timeout=self.timeout)
        return request

    # 取得url中的参数
    # 以列表的形式返回
    def get_send_values(self):
        values_list = list()
        values_string = self.url.split('?')[1:][0]
        for tmp in values_string.split('&'):
            values_list.append(tmp.split('='))
        return values_list

    # 把list对象转换成json对象
    def list_dic_tuple_2json(self, list_dic_tuple):
        return json.dumps(list_dic_tuple, indent=4)