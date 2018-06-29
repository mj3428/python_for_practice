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
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表
