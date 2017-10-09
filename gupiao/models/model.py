#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utility.sql_helper import MySqlHelper
import datetime

#爬虫数据存入表
class Gu_info:
    def __init__(self):
        self.sqlHelper = MySqlHelper()  
       
    def Insertdata(self,name,num,pice,Itime=datetime.datetime.now().strftime('%Y-%m-%d')):
        '''插入当天休市股价记录
        @param gu_name:股票名称
        @param gu_num:股票代码
        @param gu_price:股票价格
        @param create_date:插入时间
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into gu_info(gu_name,gu_num,gu_price,create_date) values(%s,%s,%s,%s)'
        params = (name,num,pice,Itime)
        result = self.sqlHelper.InsSample(sql, params)
        
        if not result:
            print False
        else:
            print True  
            
    def Selectdate(self,gname):
        '''
        @获取股票数据对应的价格和日期
        '''
        sql = 'SELECT * from gu_info where gu_name=%s'
        params = (gname)
        result = self.sqlHelper.GetDict(sql,params)
        return result

#爬虫获取信息表
class Gu_conctol:
    def __init__(self):
        self.sqlHelper = MySqlHelper()   
    def Insertdata(self,gname,gnum,glink,g_down='',g_up=''):
        '''插入当天休市股价记录
        @param gu_name:股票名称
        @param gu_num:股票代码
        @param gu_price:股票价格
        @param create_date:插入时间
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into gu_conctol(gu_name,gu_num,link,yuzhi_down,yuzhi_up) values(%s,%s,%s,%s,%s)'
        params = (gname,gnum,glink,g_down,g_up)
        result = self.sqlHelper.InsSample(sql, params)
        
        if not result:
            return False
        else:
            return True           
    
        
    def DictSelect(self):
        '''
                            获取添加的股票信息
        '''
        sql = 'SELECT * from gu_conctol'
        params = ()
        data = self.sqlHelper.GetDict(sql,params)
        return data
    

#用户股票购买表
class Gu_user:
    def __init__(self):
        self.sqlHelper = MySqlHelper()
    def Insertdata(self,gnum,gprice,numbers,Itime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        '''插入当天休市股价记录
        @param gu_name:股票名称
        @param gu_num:股票代码
        @param gu_price:股票价格
        @param create_date:插入时间
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into gu_user(gu_num,number,price,date) values(%s,%s,%s,%s)'
        params = (gnum,numbers,gprice,Itime)
        result = self.sqlHelper.InsSample(sql, params)
        
        if not result:
            return False
        else:
            return True 
        
    
    def DictSelect(self):
        '''
                            获取添加的股票信息
        '''
        sql = 'SELECT u.id,u.gu_num,a.gu_name,u.price,u.number,u.date,a.link FROM gu_user as u INNER JOIN gu_conctol as a ON a.gu_num = u.gu_num ORDER BY u.date DESC'
        params = ()
        data = self.sqlHelper.GetDict(sql,params)
        return data    
    
    def Simple_update(self,gnum,gprice,gnumber,gid):
        '''
            @修改购买的股票信息
        '''
        sql = "update gu_user set gu_num=%s,price=%s,number=%s where id =%s"
        params = (gnum,gprice,gnumber,gid)
        result = self.sqlHelper.Update_Sample(sql, params)
        print result

        
        


    
    