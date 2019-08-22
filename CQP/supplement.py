补充两个常用的生成方法

#生成AT某QQ
def AtQQ (qq):
    return '[CQ:at,qq=%s]'% (str(qq))
    
#生成表情,传入表情号
def CQFace (faceid):
    return '[CQ:at,id=%s]'% (str(faceid))
