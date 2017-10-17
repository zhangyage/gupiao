#!/usr/bin/env python
# -*- coding:utf-8 -*-
#启动页面

from  flask import Flask,render_template,request,flash,url_for,redirect
import get_data
from models.model import Gu_conctol,Gu_user
import reptile



app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def index():
    form = request.form
    gname = form.get('select_name')
    if not gname:
        gname = u'振华股份'   
    price,date,gname= get_data.price_date(gname=gname)
    #获取股票信息select传股票数值（股票名称）
    gu = Gu_conctol()
    info_name = gu.DictSelect()
    
    return render_template('index.html',price=price,date=date,gname=gname,select_data=info_name)

@app.route('/index',methods=['POST'])
def indexs():
    form = request.form
    gname = form.get('select_name')
    if not gname:
        gname = u'振华股份'   
    price,date,gname= get_data.price_date(gname=gname)
    #获取股票信息select传股票数值（股票名称）
    gu = Gu_conctol()
    info_name = gu.DictSelect()
    
    return render_template('index.html',price=price,date=date,gname=gname,select_data=info_name)

@app.route('/admin')
def admin():
    #添加的爬虫股票信息
    gu = Gu_conctol()
    info = gu.DictSelect()
    
    #购买股票展示
    g = Gu_user()
    h = g.DictSelect()
    
    goumaigupiao_info =[]
    for i in h:
        i = list(i)
        #条用函数得到事实价格
        sprice = reptile.update(i[6])
        i.append(sprice)
        #计算盈亏率追加列表 
        i.append(round(((sprice-i[3])/i[3])*100,2))
        #round(num,n)  规定数字保留的位数
        goumaigupiao_info.append(i)
    return render_template('admin.html',data_info=info,gmjl=goumaigupiao_info)


#提交股票爬虫信息   h
@app.route('/gu_insert',methods=['POST'])
def gu_insert():
    form = request.form
    gname = form.get('gname')
    gnum = form.get('gnum')
    glink = form.get('glink')
    g_down = form.get('g_down')
    g_up = form.get('g_up')
    
    if not gnum:
        flash("Please input gnum!")
        return redirect(url_for('admin'))
    
    if not gname:
        flash("Please input gname!")
        return redirect(url_for('admin')) 

    if not glink:
        flash("Please input glink!")
        return redirect(url_for('admin'))
    
    gu = Gu_conctol()
    result = gu.Insertdata(gname, gnum, glink, g_down, g_up)
    if result == 'False':
        flash("insert data failed!")
        return redirect(url_for('admin'))
    else:
        flash("insert data success!")
        #return render_template('admin.html')
        return redirect(url_for('admin'))   
    
#提交股票购买信息  h 
@app.route('/gu_price',methods=['POST'])
def gu_price():
    form = request.form
    gnum = form.get('gnum')
    gprice = form.get('gprice')
    numbers = form.get('numbers')
    
    if not gnum:
        flash("aaa")
        return redirect(url_for('admin'))
    if not gprice:
        flash("aaa")
        return redirect(url_for('admin'))
    if not numbers:
        flash("aaa")
        return redirect(url_for('admin'))
    
    gu = Gu_user()
    result = gu.Insertdata(gnum=gnum, gprice=gprice, numbers=numbers)
    if result == 'False':
        flash("insert data failed!")
        return redirect(url_for('admin'))
    else:
        flash("insert data success!")
        return redirect(url_for('admin'))
    

#404页面捕获使用
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
    
    
if __name__ =='__main__':
    app.run()