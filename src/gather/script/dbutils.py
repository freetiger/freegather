# -*- coding: utf-8 -*-
'''
Created on 2015年1月14日

@author: heyuxing
'''

import datetime
import MySQLdb
from gather.models import WeixinInfo, WeixinArticle
from MySQLdb.constants.FIELD_TYPE import NULL

def getConnect():
    host = 'localhost'
    port = 3306
    database = 'weixinarticle'
    user = 'root'
    password = '1161hyx'
    charset="utf8"
    return MySQLdb.connect(host=host, port=port, db=database,user=user,passwd=password,charset=charset)

def saveWeixinArticle(weixin_info_id, weixin_name, weixin_no, openid, title, url, content, publish_date, thumbnail_url, thumbnail_path):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("insert into gather_weixinarticle(weixin_info_id, weixin_name, weixin_no, openid, title, url, content, publish_date, thumbnail_url, thumbnail_path, create_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (weixin_info_id, weixin_name, weixin_no, openid, title, url, content, publish_date, thumbnail_url, thumbnail_path, datetime.datetime.now()))
    weixin_article_id=int(cur.lastrowid)
    conn.commit()
    cur.close()
    conn.close()
    return weixin_article_id
    
def getWeixinArticleUrls(weixin_info_id):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("SELECT url FROM gather_weixinarticle WHERE weixin_info_id="+str(weixin_info_id))
    datas = cur.fetchall()  
    urls = []
    for data in datas:
        urls.append(data[0])
    cur.close()
    conn.close()
    
    return urls

def getWeixinArticleList(id=None, weixin_info_id=None, weixin_name=None, weixin_no=None, openid=None, reproduced_num=None, offset=None, limit=None):
    sql = []
    sql.append("SELECT id, weixin_info_id, weixin_name, weixin_no, openid, title, url, content, publish_date, thumbnail_url, thumbnail_path, reproduced_num, create_date FROM gather_weixinarticle ")
    if id is not None:
        sql.append(" and id="+str(id))
    if weixin_info_id is not None:
        sql.append(" and weixin_info_id="+str(weixin_info_id))
    if weixin_name is not None:
        sql.append(" and weixin_name='"+weixin_name+"'")
    if weixin_no is not None:
        sql.append(" and weixin_no='"+weixin_no+"'")
    if openid is not None:
        sql.append(" and openid='"+openid+"'")
    if reproduced_num is not None:
        if reproduced_num is NULL:
            sql.append(" and reproduced_num is NULL" )
        else:
            sql.append(" and reproduced_num="+str(reproduced_num) ) #再升华TODO
    if offset is not None and limit is not None:
        sql.append(" limit "+str(offset)+","+str(limit))
        
    if len(sql)>1:
        if sql[1].count("and")>0:
            sql[1] = " WHERE "+sql[1][4:]
        elif sql[1].count("limit")>0:
            pass
        else:
            print "getWeixinArticleList sql error!"
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("".join(sql))
    datas = cur.fetchall()  
    weixinArticleList = []
    for data in datas:
        weixinArticle = WeixinArticle()
        weixinArticle.id = data[0]
        weixinArticle.weixin_info_id = data[1]
        weixinArticle.name = data[2]
        weixinArticle.weixin_no = data[3]
        weixinArticle.openid = data[4]
        weixinArticle.title = data[5]
        weixinArticle.url = data[6]
        weixinArticle.content = data[7]
        weixinArticle.publish_date = data[8]
        weixinArticle.thumbnail_url = data[9]
        weixinArticle.thumbnail_path = data[10]
        weixinArticle.reproduced_num = data[11]
        weixinArticle.create_date = data[12]
        weixinArticleList.append(weixinArticle)
    cur.close()
    conn.close()
    
    return weixinArticleList

def getWeixinArticleMaxPublishDate(weixin_info_id):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("SELECT MAX(publish_date) FROM gather_weixinarticle WHERE weixin_info_id="+str(weixin_info_id))
    datas = cur.fetchall()  
    cur.close()
    conn.close()
    
    return datas[0][0] if len(datas)>0 else None

def updateWeixinArticleById(id, weixin_name=None, weixin_no=None, openid=None, publish_date=None, thumbnail_url=None, thumbnail_path=None):
    updateSql = []
    updateSql.append("UPDATE gather_weixinarticle SET ")
    if weixin_name is not None:
        updateSql.append(",weixin_name='"+weixin_name+"'")
    if weixin_no is not None:
        updateSql.append(",weixin_no='"+weixin_no+"'")
    if openid is not None:
        updateSql.append(",openid='"+openid+"'")
    if publish_date is not None:
        updateSql.append(",publish_date='"+publish_date+"'")
    if thumbnail_url is not None:
        updateSql.append(",thumbnail_url='"+str(thumbnail_url)+"'")
    if thumbnail_path is not None:
        updateSql.append(",thumbnail_path='"+thumbnail_path+"'")
    updateSql.append(" WHERE id="+str(id))
    if len(updateSql)>2:
        if updateSql[1].count(",")>0:
            updateSql[1] = updateSql[1][1:]
        else:
            print "updateWeixinInfoById sql error!"
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("".join(updateSql))
    conn.commit()
    cur.close()
    conn.close()
    
def updateWeixinInfoById(id, weixin_name=None, weixin_no=None, openid=None, last_scan_date=None, update_num=None, create_date=None):
    updateSql = []
    updateSql.append("UPDATE gather_weixininfo SET ")
    if weixin_name is not None:
        updateSql.append(",weixin_name='"+weixin_name+"'")
    if weixin_no is not None:
        updateSql.append(",weixin_no='"+weixin_no+"'")
    if openid is not None:
        updateSql.append(",openid='"+openid+"'")
    if last_scan_date is not None:
        updateSql.append(",last_scan_date='"+last_scan_date+"'")
    if update_num is not None:
        updateSql.append(",update_num="+str(update_num))
    if create_date is not None:
        updateSql.append(",create_date='"+create_date+"'")
    updateSql.append(" WHERE id="+str(id))
    if len(updateSql)>2:
        if updateSql[1].count(",")>0:
            updateSql[1] = updateSql[1][1:]
        else:
            print "updateWeixinInfoById sql error!"
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("".join(updateSql))
    conn.commit()
    cur.close()
    conn.close()
    
def getWeixinInfoList(id=None, weixin_name=None, weixin_no=None, openid=None, offset=None, limit=None):
    sql = []
    sql.append("SELECT id, weixin_name, weixin_no, openid, last_scan_date, update_num, create_date FROM gather_weixininfo ")
    if id is not None:
        sql.append(" and id="+str(id))
    if weixin_name is not None:
        sql.append(" and weixin_name='"+weixin_name+"'")
    if weixin_no is not None:
        sql.append(" and weixin_no='"+weixin_no+"'")
    if openid is not None:
        sql.append(" and openid='"+openid+"'")
    if offset is not None and limit is not None:
        sql.append(" limit "+str(offset)+","+str(limit))
        
    if len(sql)>1:
        if sql[1].count("and")>0:
            sql[1] = " WHERE "+sql[1][4:]
        elif sql[1].count("limit")>0:
            pass
        else:
            print "getWeixinInfoList sql error!"
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("".join(sql))
    datas = cur.fetchall()  
    weixinInfoList = []
    for data in datas:
        weixinInfo = WeixinInfo()
        weixinInfo.id = data[0]
        weixinInfo.name = data[1]
        weixinInfo.weixin_no = data[2]
        weixinInfo.openid = data[3]
        weixinInfo.last_scan_date = data[4]
        weixinInfo.update_num = data[5]
        weixinInfo.create_date = data[6]
        weixinInfoList.append(weixinInfo)
    #print weixinInfoList[0].id,weixinInfoList[0].name,weixinInfoList[0].weixin_no,weixinInfoList[0].openid,weixinInfoList[0].last_scan_date,weixinInfoList[0].update_num,weixinInfoList[0].create_date
    cur.close()
    conn.close()
    
    return weixinInfoList

def saveWeixinArticleReproduced(weixin_info_id, weixin_article_id, reproduced_num, by_text):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("insert into gather_weixinarticlereproduced(weixin_info_id, weixin_article_id, reproduced_num, by_text, create_date) values (%s,%s,%s,%s,%s)" , (weixin_info_id, weixin_article_id, reproduced_num, by_text, datetime.datetime.now()))
    weixin_article_reproduced_id=int(cur.lastrowid)
    conn.commit()
    cur.close()
    conn.close()
    return weixin_article_reproduced_id

def saveWeixinArticleReproducedRecord(weixin_article_reproduced_id, weixin_name, openid, title, url, publish_date):
    conn = getConnect()
    cur = conn.cursor()
    cur.execute("insert into gather_weixinarticlereproducedrecord(weixin_article_reproduced_id, weixin_name, openid, title, url, publish_date, create_date) values (%s,%s,%s,%s,%s,%s,%s)" , (weixin_article_reproduced_id, weixin_name, openid, title, url, publish_date, datetime.datetime.now()))
    weixin_article_reproduced_record_id=int(cur.lastrowid)
    conn.commit()
    cur.close()
    conn.close()
    return weixin_article_reproduced_record_id

if __name__ == "__main__" :
    #getWeixinInfoList(id=1)
    #print getWeixinArticleUrls(weixin_info_id=1)
    
#     t=time.strptime('2014-3-7','%Y-%m-%d')
#     print time.strftime('%Y-%m-%d', t)
    max_publish_date = getWeixinArticleMaxPublishDate(1)
    print type(max_publish_date),max_publish_date
    


