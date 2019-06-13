# 这是一个很好的范本
#/usr/bin/env python
# -*- coding: UTF-8 -*-
import cqplus
import json
import pymongo
import funcy as fy
import datetime
from import_data import MongodbConfig
import time
import random
import linecache

col_name = {'staff': u'日期及人员', 'customer': u'客户', 'contact': u'联系人', 'sales': u'销售负责人',
    'question': u'反馈问题', 'solution': u'处理结果'}
    # 'press': '发布时间', 'sourceid': '来源'}

def get_info(info):
    """
    通过原生语句字典,以及其他信息处理
    :param info: {str} 
    :return: {dict} info
    """
    info = info.replace("：",":") #中文的冒号替换
    info = info.strip()  # 处理可能的空字符
    info = info.split("\n")  # 分割每行
    if ":" not in info[0]:
        info[0] = u"日期及人员:" + info[0]
        pass
    info = [line.split(":", 1) for line in info]  # 分割冒号
    info = dict((k.strip(), v.strip()) for k, v in info)  # 处理可能的空字符
    dictionary = dict((k, info.get(v)) for k,v in col_name.items() if v in list(info.keys()))
    return dictionary

class MainHandler(cqplus.CQPlusHandler):
    def handle_event(self, event, params):
        self.logging.debug("hello world")
        if event == "on_timer":
            for key in params:
                self.logging.debug(key + " value : "+ str(type(params[key])))
#                if type(params[key]) == dict:
#                    for key2 in params[key]:
#                        if key2 == "TIMER":
#                            continue
#                        self.logging.debug(key2 + " value2 : "+ str(params[key][key2]))
                pass
        elif event == "on_private_msg":
            self.logging.debug(event)
            self.logging.debug(str(params["from_qq"]))
            self.logging.debug(params["msg"]) # msg是unicode的类型
            self.logging.debug(str(params["msg_id"]))
            if len(params["msg"]) > 15 and u"客户" in params["msg"]:
            #   params["msg"]
                dic1 = get_info(params["msg"])
                dic1.update({'sourceid': str(params["from_qq"]),
                             'press': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                # dic2 = dict((k, dic1[v]) for k,v in col_name.items() if v in list(dic1.keys()))
                MGDB = MongodbConfig(database='zjnad', collection='customer', dict=dic1)
                MGDB.data_to_db()
                # dic2 = MGDB.dict
                # with open('./test.json', 'w') as f:
                    # f.write(json.dumps(dic1, ensure_ascii=False))
                with open('./wangwei.txt', 'r') as f:
                    line = f.readlines()
                poem_p = line[random.randint(0,1690)].strip('\n').decode('gbk')

            time.sleep(random.uniform(0.4,1.8))
            cqplus._api.send_private_msg(params["env"], params["from_qq"], '好哒！小三已将数据存入本地\n此时此刻还想吟诗一首:' + poem_p)
            
#            for key in params:
#                self.logging.debug(key + " value : "+ str(type(params[key])))                
#                pass
        elif event == "on_group_msg":
            self.logging.debug(event)
            self.logging.debug(222)
            self.logging.debug(str(params["from_group"]))
            self.logging.debug(params["msg"]) # msg是unicode的类型
            for key in params:
                self.logging.debug(key + " value : "+ str(params[key]))
                pass
            if len(params["msg"]) > 15 and u"客户" in params["msg"]:
            #   params["msg"]
                dic1 = get_info(params["msg"])
                dic1.update({'sourceid': str(params["from_group"]),
                             'press': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                # dic2 = dict((k, dic1[v]) for k,v in col_name.items() if v in list(dic1.keys()))
                MGDB = MongodbConfig(database='zjnad', collection='customer', dict=dic1)
                MGDB.data_to_db()
                # dic2 = MGDB.dict
                # with open('./test.json', 'w') as f:
                    # f.write(json.dumps(dic1, ensure_ascii=False))
                with open('./wangwei.txt', 'r') as f:
                    line = f.readlines()
                poem_g = line[random.randint(0,1690)].strip('\n').decode('gbk')

            time.sleep(random.uniform(0.4,1.8))
            cqplus._api.send_group_msg(params["env"], params["from_group"], '好哒！小三已将数据存入本地\n此时此刻还想吟诗一首:' + poem_g)
            
            

        

            
            
            

        
