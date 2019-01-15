#coding=utf-8  
import urllib2  
import urllib  
import re  
import threading  
import sys  
from time import ctime  
import time  
rlock = threading.RLock()  
def vote(proxyIP,i,urls):  
    try:  
        #print "voting...%d..." % i  
        #使用代理IP  
        proxy_support = urllib2.ProxyHandler(proxyIP)  
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)  
        #定义Opener  
  
        urllib2.install_opener(opener)  
        #把opener绑定到全局  
  
        sendt = '投票'.decode('utf-8').encode('gb2312')  
  
        #设置刷票地址  
        #post数据bn  
        values = {}  
        req = urllib2.urlopen(urls)  
        #直接打开这个URL  
        html = req.read()  
        #读取返回数据  
        if html.find('true'.decode('utf-8').encode('gb2312')):  
            print "投票 [%d] 成功" % i  
            return 1  
        else:  
            print "投票 [%d] 失败" % i  
            return 0;  
    except Exception:  
        return False  
  
if __name__ == "__main__":  
    args = sys.argv  
    if(len(args) == 3):  
        ipFile = open(args[1]);  
        ipList = ipFile.readlines()  
        ipFile.close()  
        length = range(len(ipList))  
        threads = []  
        for i in length:  
            ipLine = ipList[i]  
  
            ip=ipLine.strip()  
            proxy_ip = {'http': ip}  
            t = threading.Thread(target=vote,args=(proxy_ip,i,args[2]))  
            print "get ",args[2],ip  
            threads.append(t)  
        for i in length:  
            threads[i].start();  
            if i%100:  
                time.sleep(5)  
                #每100个线程等待 5秒  
        for i in length:  
            threads[i].join()  
  
    else:  
        print """刷票工具 
                python brush.py IP文件 Get地址: 
 
#其余参考
#https://blog.csdn.net/qq_42435653/article/details/80653376
