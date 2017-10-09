#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models.model import Gu_info


def price_date(gname):
    gupiao = Gu_info()
    price_date = gupiao.Selectdate(gname=gname)
    price = []
    date = []
    for i in price_date:
        price.append(i[3])
        date.append(int(i[4].strftime("%Y%m%d")))  
    return price , date ,gname

    