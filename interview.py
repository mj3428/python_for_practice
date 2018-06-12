'''
v = dict.fromkeys(['k1','k2'],[])
v['k1'].append(666)
print(v)
v['k1'] = 777
print(v) #{'k1': [666], 'k2': [666]}  {'k1': 777, 'k2': [666]}'''

'''def num():
    return [lambda x:i*x for i in range(4)]
print([i for i in range(4)])
#print(num())
print ([m(2) for m in num()]) #[6, 6, 6, 6]'''

'''print("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1, 10)))
#一行代码打印九九乘法表'''

