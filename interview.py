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


Python的可变类型与不可变类型
Python的每个对象都分为可变和不可变，主要的核心类型中，数字、字符串、元组是不可变的，列表、字典是可变的
对于不可变类型int，无论创建多少个不可变类型，只要值相同，都指向同个内存地址。同样情况的还有比较短的字符串
可变类型的话，以list为例。list在append之后，还是指向同个内存地址，因为list是可变类型，可以在原处修改


如何实现[‘1’,’2’,’3’]变成[1,2,3] ?
[int(k) for k in ['1','2','3']]


一行代码实现删除列表中重复的值
alist = [3,1,3,5,6,7,8,9]
blist = list(set(alist))


请用代码简答实现stack
stack的实现代码（使用python内置的list），实现起来是非常的简单，就是list的一些常用操作
class Stack(object):
    def __init__(object):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            raise LookupError('stack is empty!')

    def is_empty(self):
        return bool(self.stack)

    def top(self):
        #取出目前stack中最新的元素
        return self.stack[-1]
        

常用字符串格式化哪几种
print('hello %(first)s and %(second)s'%{'first':'df' , 'second':'another df'})最好用
print('hello {first} and {second}'.format(first='df',second='another df'))最先进


生成器、迭代器、可迭代对象 以及应用场景
可以直接作用于for循环的对象统称为：可迭代对象（Iterable）
可以被next调用并不断返回下一个值的对象称为：迭代器（Iterator）
把list、dict、str等Iterable变成Iterator可以使用iter()函数

from collections import Iterator
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance(iter('abc'), Iterator))
True
True
True
True


用Python实现一个二分查找的函数
data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]

def binary_search(dataset,find_num):
    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:  # find it
            print("找到数字", dataset[mid])
        elif dataset[mid] > find_num:  # 找的数在mid左面
            print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:  # 找的数在mid右面
            print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:  # find it
            print("找到数字啦", dataset[0])
        else:
            print("没的分了,要找的数字[%s]不在列表里" % find_num)
binary_search(data,20)


谈谈你对闭包的理解：
在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。
这样就构成了一个闭包
　  一般情况下，在我们认知当中，如果一个函数结束，函数的内部所有东西都会释放掉，还给内存，局部变量都会消失。
但是闭包是一种特殊情况，如果外函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，
就把这个临时变量绑定给了内部函数，然后自己再结束。
def outer(a):
    b = 10
    def inner():
        print(a+b)
    return inner

if __name__ == '__main__':
    demo = outer(5)
    demo()
    demo2 = outer(7)
    demo2()
'''
未完待续
