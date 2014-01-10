#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import sys
import os
import traceback
from bs4 import BeautifulSoup
import time
import optparse
from optparse import OptionParser 
from ConfigParser import SafeConfigParser

escape_strs_myav=["1","2","3","4","5","6","7","8","9","10",u"最後",u"MYAV 市集公告及貼文規則集中區"]

escape_strs_AA=[u"「站務公告」隨身版合併至耳機版",u"【二手版】團購特別辦法",u"新手必看的相關規則 & 貼圖教學",u"【二手版版規】發文前請先參閱",u"【本站論壇規則】請善用檢舉功能",u"二手版發文前請看版規(嚴禁販售保固卡)",u"【本站論壇規則】新手請至「新手發問版」簽到"]

escape_strs=["1","2","3","4","5","6","7","8","9","10",u"最後",u"MYAV 市集公告及貼文規則集中區",u"「站務公告」隨身版合併至耳機版",u"【二手版】團購特別辦法",u"新手必看的相關規則 & 貼圖教學",u"【二手版版規】發文前請先參閱",u"【本站論壇規則】請善用檢舉功能",u"二手版發文前請看版規(嚴禁販售保固卡)",u"【本站論壇規則】新手請至「新手發問版」簽到"]

class audio_crawler():
    def __init__(self,show=False):
        self.all_results=[]
        self.show=show

    def myav_new(self,pages=3):
      base_url=u"http://www.myav.com.tw/market/"
      try:  
        find_results=[]
        find_results_url=[]
        for page in range(1,pages+1):
            url="http://www.myav.com.tw/market/forumdisplay.php?forumid=44&pagenumber=%s" %page
            result=urllib.urlopen(url).read()
            a= unicode(result, 'big5')
            # work aroud : skip illegal parameter setting in this web page
            b=a.split(u"硬體新品市場置頂及延長時數收費方式")[1]
            soup = BeautifulSoup(b)
            tmp=soup.find_all("td")
            for i in tmp:
                if i != None:
                    if i.a != None:
                        if i.a.has_attr("target"):
                            if i.a["target"] == u"newwin":
#                                if i.a.string != None:
                                    if i.a.string not in escape_strs:
                                        find_results.append(i.a.string)
                                        find_results_url.append(base_url+i.a["href"])
                                        self.all_results.append(i.a.string)
        if self.show:
          print "=======myav======="
          for i in find_results:
              print i
          print "=================="
        return find_results , find_results_url

      except Exception:
          print "Exception in myav"
          print sys.exc_info()[1]
          print traceback.extract_tb(sys.exc_info()[2])
      return  find_results , find_results_url
    def myav(self,pages=3):
      base_url=u"http://www.myav.com.tw/market/"
      try:  
        find_results=[]
        find_results_url=[]
        for page in range(1,pages+1):
            url="http://www.myav.com.tw/market/forumdisplay.php?forumid=15&pagenumber=%s" %page
            result=urllib.urlopen(url).read()
#     b=result.split("硬體二手市場置頂及延長時數收費方式(限二手)")[1]
            a= unicode(result, 'big5')
            # work aroud : skip illegal parameter setting in this web page
            b=a.split(u"硬體二手市場置頂及延長時數收費方式(限二手)")[1]
            soup = BeautifulSoup(b)
            tmp=soup.find_all("td")
            for i in tmp:
                if i != None:
                    if i.a != None:
                        if i.a.has_attr("target"):
                            if i.a["target"] == u"newwin":
                                if i.a.string != None:
                                    if i.a.string not in escape_strs:
                                        find_results.append(i.a.string)
                                        find_results_url.append(base_url+i.a["href"])
                                        self.all_results.append(i.a.string)
        if self.show:
          print "=======myav======="
          for i in find_results:
              print i
          print "=================="
        return find_results , find_results_url

      except Exception:
          print "Exception in myav"
          print type(result)
          print sys.exc_info()[1]
          print traceback.extract_tb(sys.exc_info()[2])
      return  find_results , find_results_url

    def AA(self,pages=3):
        find_results=[]
        find_results_url=[]
        base_url=u"http://www.andaudio.com/phpbb3/"
        for page in range(0,pages):
            page=page*45
            url="http://www.andaudio.com/phpbb3/viewforum.php?f=1&start=%s" %page
            result=urllib.urlopen(url).read()
            soup = BeautifulSoup(result)
            r=soup.find_all("dt")
            for result in r:
                if result.a:
                    if result.a.string not in escape_strs:
#                         find_results.append(result.text.split(u"發表於")[-1].split(u",")[0]+result.a.string)
                         find_results.append(result.a.string)
                         find_results_url.append(base_url+result.a["href"])
                         self.all_results.append(result.a.string)
        if self.show:
          print "=========AA========="
          for i in find_results:
              print i
          print "===================="

        return find_results,find_results_url

    def ptt(self,pages=3,num=0):
        find_results=[]
        find_results_url=[]
        base_url=u"http://www.ptt.cc"
        
        url="http://www.ptt.cc/bbs/Headphone/index.html"
        result=urllib.urlopen(url).read()
        soup = BeautifulSoup(result)
        r=soup.find_all("a")
        for item in r:
            if (item.string==u"‹ 上頁"):
                href = item['href']
                lastpage=href.split("/")[-1].split(".")[0][5:]
        lastpage = int (lastpage) + 1 
        i=0
        if num >0: 
            while find_results_url.__len__() < num:
                page = lastpage - i
                url="http://www.ptt.cc/bbs/Headphone/index%s.html" %page
                result=urllib.urlopen(url).read()            
                soup = BeautifulSoup(result)
                result=soup.find_all("div")
                result=result[8:]
                find_str_title=u""
                find_str_date=u""
                find_str_author=u""
                index=0     
                i=i+1
                for r in result:
                    if r["class"][0]==u"title":
                        if r.a:
                            find_str_title=r.a.string                   
                            if find_str_title.rfind(u"交易") != -1:
                                find_results_url.insert(index,base_url+r.a["href"])
                    if r["class"][0]==u"date":
                        find_str_date=r.string
                    if r["class"][0]==u"author":
                        if find_str_title.rfind(u"交易") != -1:
                            find_str_author=r.string
        #               find_str = find_str_date + "__" + find_str_author + "__" + find_str_title
                            find_str = find_str_date + "__" + find_str_title
                            find_results.insert(index,find_str)                    
                            self.all_results.append(find_str)
                            index=index+1
                        find_str_title=u""
                        find_str_date=u""
                        find_str_author=u""
        else:
            for i in range(0,pages):
                page = lastpage - i
                url="http://www.ptt.cc/bbs/Headphone/index%s.html" %page
                result=urllib.urlopen(url).read()            
                soup = BeautifulSoup(result)
                result=soup.find_all("div")
                result=result[8:]
                find_str_title=u""
                find_str_date=u""
                find_str_author=u""
                index=0            
                for r in result:
                    if r["class"][0]==u"title":
                        if r.a:
                            find_str_title=r.a.string                   
                            if find_str_title.rfind(u"交易") != -1:
                                find_results_url.insert(index,base_url+r.a["href"])
                    if r["class"][0]==u"date":
                        find_str_date=r.string
                    if r["class"][0]==u"author":
                        if find_str_title.rfind(u"交易") != -1:
                            find_str_author=r.string
    #                    find_str = find_str_date + "__" + find_str_author + "__" + find_str_title
                            find_str = find_str_date + "__" + find_str_title
                            find_results.insert(index,find_str)                    
                            self.all_results.append(find_str)
                            index=index+1
                        find_str_title=u""
                        find_str_date=u""
                        find_str_author=u""

        if self.show:
          print "========ptt========="
          for i in find_results:
              print i
          print "===================="

        find_results.reverse()
        find_results_url.reverse()
        return find_results,find_results_url

    def show_all(self,pages=3):
        print "processing PTT"
        self.ptt(pages)
        print "processing AA"
        self.AA(pages)
        print "processing myav"
        self.myav(pages)
        f=open("audio_result",'w')
        for record in self.all_results:
            print record
            f.write(record.encode('utf-8'))
            f.write('\n')
        f.close()

    def gen_html(self,pages=3,web_root=""):
        import markup
        ptt=[]
        ptt_url=[]
        AA=[]
        AA_url=[]
        myav=[]
        myav_url=[]
        myav_new=[]
        myav_new_url=[]
        print "processing PTT"
        ptt,ptt_url=self.ptt(num=pages*20)
        print "processing AA"
        AA,AA_url=self.AA(pages)
        print "processing myav 二手"
        myav,myav_url=self.myav(pages)
        print "processing myav 新品"
        myav_new,myav_new_url=self.myav_new(pages)

        encode_ptt=[]
        encode_AA=[]
        encode_myav=[]
        encode_myav_new=[]

        encode_ptt_url = []
        encode_AA_url = []
        encode_myav_url = []
        encode_myav_new_url=[]

        for record in ptt:
            encode_ptt.append(record)
        for record in ptt_url:
            encode_ptt_url.append(record)

        for record in AA:
            encode_AA.append(record)
        for record in AA_url:
            encode_AA_url.append(record)

        for record in myav:
            encode_myav.append(record)
        for record in myav_url:
            encode_myav_url.append(record)
        
        for record in myav_new:
            encode_myav_new.append(record)
        for record in myav_new_url:
            encode_myav_new_url.append(record)

        page = markup.page()
        page.init( title="Search Result",
                   charset="utf-8",
                   header="",
                   footer="" )
        
        page.p(u"==================================================")
        page.p(u"PTT")
        for i in range(0,encode_ptt.__len__()):
            text=encode_ptt[i]
            link=encode_ptt_url[i]
            page.a( text, class_='internal', href=link )
            page.p("")
        page.p(u"==================================================")
        page.p(u"AA")
        for i in range(0,encode_AA.__len__()):
            text=encode_AA[i]
            link=encode_AA_url[i]
            page.a( text, class_='internal', href=link )
            page.p("")
        page.p(u"==================================================")
        page.p(u"MYAV二手")
        for i in range(0,encode_myav.__len__()):
            text=encode_myav[i]
            link=encode_myav_url[i]
            page.a( text, class_='internal', href=link )
            page.p("")
        page.p(u"==================================================")
        page.p(u"MYAV新品")
        for i in range(0,encode_myav_new.__len__()):            
            text=encode_myav_new[i]
            link=encode_myav_new_url[i]
            page.a( text, class_='internal', href=link )
            page.p("")
        c = page.get_result()
        '''
        f=open("a.html",'w')
        f.write(c.encode('utf-8'))
        f.close()
        '''
        print "=====generate web page complete====="
        return c

if __name__ == '__main__':
    optParser = OptionParser()
    parser = SafeConfigParser()
    parser.read('/Users/sniper/crawler.conf')
    optParser.add_option("-s", 
            "--show", 
            action = "store_true", 
            default=parser.getboolean('core', 'show'),
            dest = "show") 
    optParser.add_option("-p", 
            "--page", 
            action = "store", 
            default=parser.getint('core', 'pages'),
            type = "int", 
            dest = "page") 

    web_root=parser.get('core', 'web_root')
    options, args = optParser.parse_args()
    
    a=audio_crawler(show=options.show)
    a.gen_html(pages=options.page,web_root=web_root)
