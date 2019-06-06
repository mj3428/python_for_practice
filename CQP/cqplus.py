# 这是一个很好的范本
# -*- coding:utf-8 -*-

import cqplus


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
            self.logging.debug(params["msg"])
            self.logging.debug(str(params["msg_id"]))
            cqplus._api.send_private_msg(params["env"],params["from_qq"],str(params["msg_id"]))
            
            
#            for key in params:
#                self.logging.debug(key + " value : "+ str(type(params[key])))                
#                pass
        elif event == "on_group_msg":
            self.logging.debug(event)
            self.logging.debug(222)
            for key in params:
                self.logging.debug(key + " value : "+ str(params[key]))
                pass
            
            
            

        
