'''
os与sys模块的官方解释如下:
os:这个模块提供了一种方便的使用操作系统函数的方法
sys:这个模块可供访问由解释器使用或维护的变量和与解释器进行交互的函数
总结:
os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;
sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境;
os常见操作
os.remove(‘path/filename’) 删除文件
os.rename(oldname, newname) 重命名文件
os.walk() 生成目录树下的所有文件名
os.chdir('dirname') 改变目录
os.mkdir/makedirs('dirname')创建目录/多层目录
os.rmdir/removedirs('dirname') 删除目录/多层目录
os.rmdir/removedirs('dirname') 删除目录/多层目录
os.listdir('dirname') 列出指定目录的文件
os.getcwd() 取得当前工作目录
os.chmod() 改变目录权限
os.path.basename(‘path/filename’) 去掉目录路径，返回文件名
os.path.dirname(‘path/filename’) 去掉文件名，返回目录路径
sys常见操作
sys.argv 命令行参数List，第一个元素是程序本身路径
sys.modules.keys() 返回所有已经导入的模块列表
sys.exc_info() 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
sys.exit(n) 退出程序，正常退出时exit(0)
sys.hexversion 获取Python解释程序的版本值，16进制格式如：0x020403F0
sys.version 获取Python解释程序的版本信息
sys.maxint 最大的Int值
sys.maxunicode 最大的Unicode值


如何生成一个随机数？
import random # 随机模块
data = list(range(10))
print(data)  # 打印有序的列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(data) # 使有序变为无序 
print(data) # 打印无序的列表 [4, 2, 5, 1, 6, 3, 9, 8, 0, 7]


如何使用python删除一个文件？
若想利用python删除windows里的文件，这里需要使用os模块！那接下来就看看利用os模块是如何删除文件的！
具体实现方法如下！
os.remove(path)
删除文件 path. 如果path是一个目录， 抛出 OSError错误。如果要删除目录，请使用rmdir().
remove() 同 unlink() 的功能是一样的 
在Windows系统中，删除一个正在使用的文件，将抛出异常。在Unix中，目录表中的记录被删除，但文件的存储还在
import os
my_file = 'D:/text.txt' # 文件路径
if os.path.exists(my_file): # 如果文件存在
    #删除文件，可使用以下两种方法。
    os.remove(my_file) # 则删除
    #os.unlink(my_file)
else:
    print('no such file:%s'%my_file)
os.removedirs(path) 
递归地删除目录。类似于rmdir(), 如果子目录被成功删除， removedirs() 将会删除父目录；但子目录没有成功删除，将抛出错误。
例如， os.removedirs(“foo/bar/baz”) 将首先删除baz目录，然后再删除bar和 foo, 如果他们是空的话，则子目录不能成功删除，将抛出 OSError异常
os.rmdir(path) 
删除目录 path，要求path必须是个空目录，否则抛出OSError错误
import os
for root, dirs, files in os.walk(top, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
import shutil
shutil.rmtree()


面向对象的继承有什么特点？
继承的优点：
　　1、建造系统中的类，避免重复操作。
　　2、新类经常是基于已经存在的类，这样就可以提升代码的复用程度
继承的特点：
　　1、在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。有别于C#
　　2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
　　3、Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。
      （先在本类中查找调用的方法，找不到才去基类中找）


什么是super
super() 函数是用于调用父类(超类)的一个方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表

class FooParent:  
  def bar(self, message):  
    print(message)  
class FooChild(FooParent):  
  def bar(self, message):  
    FooParent.bar(self, message)  
>>> FooChild().bar("Hello, Python.")  
Hello, Python.

class A:  
  def __init__(self):  
    print("Enter A")  
    print("Leave A")  
class B(A):  
  def __init__(self):  
    print("Enter B")  
    A.__init__(self)  
    print("Leave B")  
class C(A):  
  def __init__(self):  
    print("Enter C")  
    A.__init__(self)  
    print("Leave C")  
class D(A):  
  def __init__(self):  
    print("Enter D")  
    A.__init__(self)  
    print("Leave D")  
class E(B, C, D):  
  def __init__(self):  
    print("Enter E")  
    B.__init__(self)  
    C.__init__(self)  
    D.__init__(self)  
    print("Leave E")  
E()

结果为：

Enter E
Enter B
Enter A
Leave A
Leave B
Enter C
Enter A
Leave A
Leave C
Enter D
Enter A
Leave A
Leave D
Leave E


是否使用过functools中的函数？
import functools
foo = functools.partial(int, base=8)
foo('11111')  # print 4681
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
  return int(x, base)
>>> int2('1000000')
64
>>> int2('1010101')
85
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
所以，简单总结functools.partial的作用就是，
把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单


__new__()方法的特性：
   __new__()方法是在类准备将自身实例化时调用。
   __new__()方法始终都是类的静态方法，即使没有被加上静态方法装饰器
第一个参数cls是当前正在实例化的类。
   如果要得到当前类的实例，应当在当前类中的__new__()方法语句中调用当前类的父类 的__new__()方法。
例如，如果当前类是直接继承自object，那当前类的__new__()方法返回的对象应该为：
def __new__(cls, *args, **kwargs):
   ...
   return object.__new__(cls)

class Foo(object):
    def __init__(self, *args, **kwargs):
        ...
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)    
    
# 以上return等同于 
# return object.__new__(Foo, *args, **kwargs)
# return Stranger.__new__(cls, *args, **kwargs)
# return Child.__new__(cls, *args, **kwargs)


静态方法和类方法区别？
class Foo(object):  
    def test(self): #定义了实例方法  
        print("object")  
    @classmethod  # 装饰器
    def test2(clss): #定义了类方法  
        print("class")  
    @staticmethod  # 装饰器
    def test3(): #定义了静态方法  
        print("static")
实例方法访问方式：
ff=Foo()
ff.test();//通过实例调用  
Foo.test(ff)//直接通过类的方式调用，但是需要自己传递实例引用
类方法访问方式：
Foo.test2();
如果Foo有了子类并且子类覆盖了这个类方法，最终调用会调用子类的方法并传递的是子类的类对象
class Foo2(Foo):  
    @classmethod  
    def test2(self):  
        print(self)  
        print("foo2 object")  
f2=Foo2()  
print(f2.test2())

输出结果：
<class '__main__.Foo2'>
foo2 object
None
静态方法调用方式：
Foo.test3();//直接静态方式调用

实例方法针对的是实例，类方法针对的是类，他们都可以继承和重新定义，而静态方法则不能继承，可以认为是全局函数


列举面向对象中的特殊成员以及应用场景？
__doc__  描述类的信息
class Foo(object):  
    # 单引号和双引号都可以  
    """这里描述类的信息"""  
    def func(self):  
        pass  
print(Foo.__doc__) 
显示的结果：
    这里描述类的信息

__call__ 对象后面加括号，触发执行
# __call__方法的执行是由对象加括号触发的，即：对象()或者 类()()  
class Foo(object):  
    def __call__(self, *args, **kwargs):  
        print("running call", args, kwargs)  
foo = Foo()  
foo(1, 2, 3, name = "UserPython")   
Foo()(1, 2, 3, name = "UserPython")

# __call__方法的执行是由对象加括号触发的，即：对象()或者 类()()  
class Foo(object):  
    def __call__(self, *args, **kwargs):  
        print("running call", args, kwargs)  
foo = Foo()  
foo(1, 2, 3, name = "UserPython")   
Foo()(1, 2, 3, name = "UserPython") 
running call(1,2,3){'name' : 'UserPython'}
running call(1,2,3){'name' : 'UserPython'}


什么是反射？以及应用场景
http://www.cnblogs.com/zhuifeng-mayi/p/9230975.html


metaclass作用及应用场景？

metaclass能有什么用处，先来个感性的认识：
1. 你可以自由的、动态的修改/增加/删除 类的或者实例中的方法或者属性
2. 批量的对某些方法使用decorator，而不需要每次都在方法的上面加入@decorator_func
3. 当引入第三方库的时候，如果该库某些类需要patch的时候可以用metaclass
4. 可以用于序列化(参见yaml这个库的实现，我没怎么仔细看）
5. 提供接口注册，接口格式检查等
6. 自动委托(auto delegate)
7. more...

也就是说metaclass的实例化结果是类，而class实例化的结果是instance。我是这么理解的：
metaclass是类似创建类的模板，所有的类都是通过他来create的(调用__new__)，这使得你可以自由的控制
创建类的那个过程，实现你所需要的功能
一般情况下, 如果你要用类来实现metaclass的话，该类需要继承于type，而且通常会重写type的__new__方法来控制创建过程。

如何使用metaclass
类继承于type, 例如： class Meta(type):pass
将需要使用metaclass来构建class的类的__metaclass__属性（不需要显示声明，直接有的了）赋值为Meta（继承于type的类）

 构建一个函数，例如叫metaclass_new, 需要3个参数：name, bases, attrs，
name: 类的名字
bases: 基类，通常是tuple类型
attrs: dict类型，就是类的属性或者函数
将需要使用metaclass来构建class的类的__metaclass__属性（不需要显示声明，直接有的了）赋值为函数metaclas_new

metaclass 原理：
metaclass的原理其实是这样的：当定义好类之后，创建类的时候其实是调用了type的__new__方法为这个类分配内存空间，创建
好了之后再调用type的__init__方法初始化（做一些赋值等）。所以metaclass的所有magic其实就在于这个__new__方法里面了
说说这个方法：__new__(cls, name, bases, attrs)
cls: 将要创建的类，类似与self，但是self指向的是instance，而这里cls指向的是class
name: 类的名字，也就是我们通常用类名.__name__获取的。
bases: 基类
attrs: 属性的dict。dict的内容可以是变量(类属性），也可以是函数（类方法）

例子：
#!/usr/bin/python  
#coding :utf-8  
def ma(cls):  
    print 'method a'    
def mb(cls):  
    print 'method b'  

method_dict = {  
    'ma': ma,  
    'mb': mb,  
}  
 
class DynamicMethod(type):  
    def __new__(cls, name, bases, dct):  
        if name[:3] == 'Abc':  
            dct.update(method_dict)  
        return type.__new__(cls, name, bases, dct) 
  
    def __init__(cls, name, bases, dct):  
        super(DynamicMethod, cls).__init__(name, bases, dct)  

class AbcTest(object):  
    __metaclass__ = DynamicMethod 
    def mc(self, x):  
        print x * 3  
class NotAbc(object):  
    __metaclass__ = DynamicMethod  
    def md(self, x):  
        print x * 3  
def main():  
    a = AbcTest()  
    a.mc(3)  
    a.ma()  
    print dir(a)  
    b = NotAbc()  
    print dir(b) 
if __name__ == '__main__':  
    main()  
######还是有点难#####后续重点看#######
https://www.cnblogs.com/liunnis/articles/4606371.html
