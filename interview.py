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
所以三次执行的结果就是 [1, 1, 1] 想每次执行只输出[1] ，默认参数应该设置为None


解释型和编译型编程语言的区别：
解释型语言编写的程序不需要编译，在执行的时候，专门有一个解释器能够将VB语言翻译成机器语言
每个语句都是执行的时候才翻译。这样解释型语言每执行一次就要翻译一次，效率比较低。

用编译型语言写的程序执行之前，需要一个专门的编译过程，通过编译系统，
把源高级程序编译成为机器语言文件，翻译只做了一次，运行时不需要翻译，
所以编译型语言的程序执行效率高，但也不能一概而论，
部分解释型语言的解释器通过在运行时动态优化代码，甚至能够使解释型语言的性能超过编译型语言。


求结果：
v1 = 1 or 3                    #解析：3 and 4即3与4为3，但是由于是短路操作符，结果为4，
v2 = 1 and 3                         是因为and运算符必须所有的运算数都是true才会把所有的运算数都解析，并且返回最后一个变量
v3 = 0 and 2 and 1                   即为4；改变一下顺序4 and 3 ，结果也不一样，即为3.
v4 = 0 and 2 or 1                    或逻辑（or），即只要有一个是true，即停止解析运算数
v5 = 0 and 2 or 1 or 4               返回最近为true的变量，即 3 or 4，值为3；改变顺序4 or 3 即为4.
v6 = 0 or False and 1                如果 x 为假，x 决定了结果为假，返回 x 0为假
print(v1,v2,v3,v4,v5,v6) #答案：1 3 0 1 1 False


列举 Python2和Python3的区别:
在 Python 2 中， print 被视为一个语句而不是一个函数，这是一个典型的容易弄混的地方，因为在 Python 中的许多操作都需要括号内的参数来执行
当编程语言处理字符串类型时，也就是一个字符序列，它们可以用几种不同的方式来做，以便计算机将数字转换为字母和其他符号。

Python 2 默认使用 ASCII 字母表，因此当您输入“Hello，Sammy！”时， Python 2 将以 ASCII 格式处理字符串。
被限定为在多种扩展形式上的数百个字符，
用ASCII 进行字符编码并不是一种非常灵活的方法，特别是使用非英语字符时。
要使用更通用和更强大的Unicode字符编码，这种编码支持超过128,000个跨越现今和历史的脚本和符号集的字符，你必须输入
u“Hello，Sammy！”前缀 u 代表 Unicode。
Python 3 默认使用 Unicode，这节省了程序员多余的开发时间，并且您可以轻松地在程序中直接键入和显示更多的字符。
因为 Unicode 支持更强大的语言字符多样性以及 emoji 的显示，所以将它作为默认字符编码来使用，能确保全球的移动设备在您的开发项目中都能得到支持


用一行代码实现数值交换：
a = 1
b = 2
a,b=b,a
print(a,b)  #a=2,b=1


Python3和Python2中 int 和 long的区别？
long整数类型被Python3废弃，统一使用int


xrange和range的区别？
range 函数说明：range([start,] stop[, step])，根据start与stop指定的范围以及step设定的步长，生成一个序列。
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(1,5)
[1, 2, 3, 4]
>>> range(0,6,2)
[0, 2, 4]
xrange 函数说明：用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器。
xrange示例:
>>> xrange(5)
xrange(5)
>>> list(xrange(5))
[0, 1, 2, 3, 4]
>>> xrange(1,5)  
xrange(1, 5)
>>> list(xrange(1,5))
[1, 2, 3, 4]
>>> xrange(0,6,2)
xrange(0, 6, 2)
>>> list(xrange(0,6,2))
[0, 2, 4]
要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间，这两个基本上都是在循环的时候用


文件操作时：xreadlines和readlines的区别？
二者使用时相同，但返回类型不同，xreadlines返回的是一个生成器，readlines返回的是list


布尔值为false的5种情况
数字0、特殊值的 null、NaN、undefined、字符串""


pass的作用？
空语句 do nothing
if true:
    pass #do nothing
else:
    pass #do something
　　2、保证格式完整
def iplaypython():
    pass
　　3、保证语义完整
while True:
    pass


*arg和**kwarg作用
*args：可以理解为只有一列的表格，长度不固定。
**kwargs：可以理解为字典，长度也不固定。
args和kwarg不是必须成对出现，也不是必须叫这个名字，也可以叫*x和**y。写成这样，只是一种约定俗成
1、函数调用里的*arg和**kwarg：
（1）*arg：元组或列表“出现”
　   **kwarg：字典“出没”
（2）分割参数
2、函数定义时传的*arg /**kwarg:
（1）接收参数


简述Python的深浅拷贝以及应用场景？
浅拷贝指仅仅拷贝数据集合的第一层数据，深拷贝指拷贝数据集合的所有层。
所以对于只有一层的数据集合来说深浅拷贝的意义是一样的，比如字符串，数字，还有仅仅一层的字典、列表、元祖等


