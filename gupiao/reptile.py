#!/usr/bin/env python
# -*- coding:utf-8 -*-

#返回实时价格

import urllib2
import re

def update(url):
    #url = "http://hq.sinajs.cn/list=sh603067"

    rep = urllib2.Request(url)
    
    rep.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")
    rep.add_header("Host","hq.sinajs.cn")
    rep.add_header("Referer","http://finance.sina.com.cn/realstock/company/sh603067/nc.shtml")
    #这个是key：value的关系具体的值可以通过使用浏览器的开发者模式自行查找定义
    #可以伪造头部的很多字段和值
    resp = urllib2.urlopen(rep)
    
    info = resp.read().decode('gbk')
    #读取对象，定义输出字符为中文避免乱码
    
    name = info.split(',')[0].split('\"')[1]
    nums = info.encode('utf-8').split(',')[0]
    num = int(re.findall(r'\d+',nums)[0])
    price =  float(info.split(',')[3])
    return price

# url = "http://hq.sinajs.cn/list=sh603067"
# print update(url)   
    
