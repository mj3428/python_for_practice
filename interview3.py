'''
用尽量多的方法实现单例模式
Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码
1.
#foo1.py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()

#foo.py
from foo1 import singleton
2.
直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象
先执行了类的__new__方法（我们没写时，默认调用object.__new__），实例化对象;
然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式;
class Singleton(object):
    def __new__(cls,a):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance
    def __init__(self,a):
        self.a = a
    def aa(self):
        print(self.a)

a = Singleton("a")
变种：利用类的静态方法或者类方法，实现对函数初始化的控制
该方法需要手动调用静态方法实现实例。本质上是手动版的__new__方法
3.
执行元类的 元类的__new__方法和__init__方法用来实例化类对象，__call__ 方法用来对实例化的对象的实例即类的对象进行控制
__call__方法会调用实例类的 __new__方法，用于创建对象
返回对象给__call__方法，然后调用类对象的 __init__方法，用于对对象初始化
class Singleton1(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super(Singleton1,self).__init__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singleton1,self).__call__(*args, **kwargs)
        return self.__instance
class Singleton2(type):
    _inst = {}
    def __call__(cls, *args, **kwargs):
        print(cls)
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton2, cls).__call__(*args)
        return cls._inst[cls]
class C(metaclass=Singleton1):
    pass
4.
装饰器用来控制类调用__call__方法
def singleton(cls, *args, **kw):
    instance = {}
    def _singleton(args):
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton
class A:
    pass

异常处理写法与跑出异常：
执行的流程分两类：
1.try->若有异常发生->except->finally
2.try->若无异常发生->else->finally
其中try块执行了可能抛出异常的语句，except块负责处理抛出的异常，处理的尝试顺序与多个except块的编写顺序一致
当尝试发现第一个异常类型匹配的except块时就进入该块内执行该except块的语句
最后一个不指定异常类型的except:块匹配任何类型的异常（由于所有异常都继承自Exception类所有except Exception：与不指定异常类型效果一致）
except块至少要有一个，可以使用pass语句
except:
　　pass
表示“抓到”异常后不进行任何处理
finally类是可选的块，如前面的流程所示，无论是否有异常抛出，只要finally块存在就会被最终执行
（该块中的语句一般用于关闭打开的资源，比如在try块中打开的磁盘文件）

with open('abc.txt', 'r') as f:
　　f语句块....
上面的f就是打开的文件对象，而采用with..as..方式会在执行完f语句块后自动关闭打开的文件资源
而不用自己写finally语句块。
例子：
class myerr(Exception):
    def __init__(self,err):
        Exception.__init__(self)
        self.err=err
try:
    raise myerr('myexception')
except myerr as var :
    print(var.err)
定义自己的异常类一般都继承自Exception类，初始化时同时使用Exception类的__init__方法
引发自己定义的异常的语法是raise exceptiontype(arg...),直接生成该异常类的一个实例（实例化时需要的参数自行提供）并抛出该异常
在捕获异常时使用except exceptiontype as var的语法获取异常实例var，从而可以在后续的处理中访问该异常实例的属性
输出为：
    myexception

什么是面向对象的mro
一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：

子类永远在父类前面
如果有多个父类，会根据它们在列表中的顺序被检查
如果对下一个类存在两个合法的选择，选择第一个父类
用途:
避免多重继承
super使用一致
不要混用经典类和新式类
调用父类的时候注意检查类层次

事实上，super 和父类没有实质性的关联。
super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类

