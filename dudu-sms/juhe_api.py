#!/usr/bin/python
# coding:utf-8
import urllib
from sqlalchemy import create_engine
from sqlalchemy.sql import text


def connect_mysql(distinct):
    try:
        engine = create_engine('mysql+pymysql://zlzy:Zlzy1708@zlzy.cqlpyzw4wcmk.us-west-2.rds.amazonaws.com:3306/zlzy?charset=utf8', pool_recycle=3600, echo=True)
        connection = engine.connect()
        t = text("select telephone from zlzy.cable_company_info where address2 like :x")
        t = t.bindparams(x=distinct)
        ret = connection.execute(t)
        print(ret)
        connection.close()
        return ret
    except Exception as e:
        print(e)
        return None


def sendsms(appkey, mobile, tpl_id, tpl_value):
    sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改

    params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
             (appkey, mobile, tpl_id, urllib.request.quote(tpl_value))  # 组合参数

    wp = urllib.request.urlopen(sendurl + "?" + params)
    result = wp.read()  # 获取接口返回内容
    print(result)
    # result = json.loads(content)


if __name__ == '__main__':
    appkey = '87c08ff081da89551097faa422833582'  # 您申请的短信服务appkey
    tpl_id = '20480'  # 申请的短信模板ID,根据实际情况修改
    tpl_value = ''  # 短信模板变量,根据实际情况修改
    result = connect_mysql('测试地址')
    if result:
        for mobile in result:
            if mobile[0].startswith('1'):
                sendsms(appkey, mobile[0], tpl_id, tpl_value)  # 请求发送短信
