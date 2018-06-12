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
#一行代码打印九九乘法表
print([ i % 2 for i in range(10) ]) #[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print( i % 2 for i in range(10) ) #<generator object <genexpr> at 0x000000000273CCA8>

python里面的坑: 函数的默认参数是一个list 
当第一次执行的时候实例化了一个list 
第二次执行还是用第一次执行的时候实例化的地址存储 
所以三次执行的结果就是 [1, 1, 1] 想每次执行只输出[1] ，默认参数应该设置为None'''
