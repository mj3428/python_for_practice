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
