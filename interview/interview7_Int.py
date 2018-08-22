'''

python协程深入理解：http://www.cnblogs.com/zhaof/p/7631851.html

haproxy是什么以及作用？
haproxy和keepalived的综合理解参照：https://blog.csdn.net/tuolaji8/article/details/52870791
haproxy原理：https://www.cnblogs.com/skyflask/p/6970151.html

HAProxy与LVS的异同
通过之前文章的介绍，大家应该基本清楚了HAProxy负载均衡与LVS负载均衡的优缺点和异同了。下面就这两种负载均衡软件的异同做一个简单总结：
1）两者都是软件负载均衡产品，但是LVS是基于Linux操作系统实现的一种软负载均衡，而HAProxy是基于第三应用实现的软负载均衡。
2）LVS是基于四层的IP负载均衡技术，而HAProxy是基于四层和七层技术、可提供TCP和HTTP应用的负载均衡综合解决方案。
3）LVS工作在ISO模型的第四层，因此其状态监测功能单一，而HAProxy在状态监测方面功能强大，可支持端口、URL、脚本等多种状态检测方式。
4）HAProxy虽然功能强大，但是整体处理性能低于四层模式的LVS负载均衡，而LVS拥有接近硬件设备的网络吞吐和连接负载能力。
综上所述，HAProxy和LVS各有优缺点，没有好坏之分，要选择哪个作为负载均衡器，要以实际的应用环境来决定。


什么是负载均衡？
负载均衡是由多台服务器以对称的方式组成一个服务器集合，每台服务器都具有等价的地位，都可以单独对外供应效力而无须其他服务器的辅助。
经过某种负载分管技术，将外部发送来的央求均匀分配到对称结构中的某一台服务器上，而接收到央求的服务器独登时回应客户的央求。
均衡负载可以平均分配客户央求到服务器列阵，籍此供应快速获取重要数据，解决很多并发访问效力问题。
这种群集技术可以用最少的出资取得接近于大型主机的性能。

根据DNS的负载均衡
经过DNS效力中的随机姓名解析来完结负载均衡，在DNS服务器中，可认为多个不同的地址配置同一个姓名，
而最终查询这个姓名的客户机将在解析这个姓名时得到其中一个地址。
因此，关于同一个姓名，不同的客户时机得到不同的地址，他们也就访问不同地址上的Web服务器，然后达到负载均衡的目的。

反向署理负载均衡
运用署理服务器可以将央求转发给内部的Web服务器，让署理服务器将央求均匀地转发给多台内部Web服务器之一上，然后达到负载均衡的目的。
这种署理方式与一般的署理方式有所不同，标准署理方式是客户运用署理访问多个外部Web服务器，
而这种署理方式是多个客户运用它访问内部Web服务器，因此也被称为反向署理模式。Apusic负载均衡器就归于这种类型的。

NAT的负载均衡技术
网络地址变换为在内部地址和外部地址之间进行变换，以便具备内部地址的计算机能访问外部网络，
而当外部网络中的计算机访问地址变换网关拥有的某一外部地址时，地址变换网关能将其转发到一个映射的内部地址上。
因此如果地址变换网关能将每个衔接均匀变换为不同的内部服务器地址，
尔后外部网络中的计算机就各自与自己变换得到的地址上服务器进行通讯，然后达到负载分管的目的。

负载均衡服务器的好处
由于网民数量激增，网络访问路径过长，用户的访问质量简略遭到严重影响，尤其是当用户与网站之间的链路被出人意料的流量拥塞时。
而这种情况经常发生在异地互联网用户急速增加的运用上。
这时候，如果在效力端运用负载均衡(GSLB)技术，就可以合理分管系统负载、提高系统可靠性、支持网站内容的虚拟化。
高智能化、高可靠性、高可用性、服务器负载均衡。

什么是RPC概念和应用？
RPC 的主要功能目标是让构建分布式计算（应用）更容易，在提供强大的远程调用能力时不损失本地调用的语义简洁性。
为实现该目标，RPC 框架需提供一种透明调用机制让使用者不必显式的区分本地调用和远程调用，基于 stub 的结构来实现。
下面我们将具体细化 stub 结构的实现。
RPC 调用分以下两种：
1. 同步调用  
   客户方等待调用执行完成并返回结果。  
2. 异步调用  
   客户方调用后不用等待执行结果返回，但依然可以通过回调通知等方式获取返回结果。  
   若客户方不关心调用返回结果，则变成单向异步调用，单向调用不用返回结果。

拆解了 RPC 实现结构的各个组件组成部分
1. RpcServer  
   负责导出（export）远程接口  
2. RpcClient  
   负责导入（import）远程接口的代理实现  
3. RpcProxy  
   远程接口的代理实现  
4. RpcInvoker  
   客户方实现：负责编码调用信息和发送调用请求到服务方并等待调用结果返回  
   服务方实现：负责调用服务端接口的具体实现并返回调用结果  
5. RpcProtocol  
   负责协议编/解码  
6. RpcConnector  
   负责维持客户方和服务方的连接通道和发送数据到服务方  
7. RpcAcceptor  
   负责接收客户方请求并返回请求结果  
8. RpcProcessor  
   负责在服务方控制调用过程，包括管理调用线程池、超时时间等  
9. RpcChannel  
   数据传输通道
详细链接：https://blog.csdn.net/lipp555/article/details/52610540


简述asynio模块的作用和应用
异步网络操作
并发
协程

关于asyncio的一些关键字的说明：
  event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数
  coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。
                  协程对象需要注册到事件循环，由事件循环调用。
  task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态
  future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别
  async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口

import time
import asyncio

now = lambda : time.time()
async def do_some_work(x):
    print("waiting:", x)
start = now()
# 这里是一个协程对象，这个时候do_some_work函数并没有执行
coroutine = do_some_work(2)
print(coroutine)
#  创建一个事件loop
loop = asyncio.get_event_loop()
# 将协程加入到事件循环loop
loop.run_until_complete(coroutine)
print("Time:",now()-start)
在上面带中我们通过async关键字定义一个协程（coroutine）,当然协程不能直接运行，需要将协程加入到事件循环loop中
asyncio.get_event_loop：创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，并启动事件循环

import asyncio
import time

now = lambda: time.time()
async def do_some_work(x):
    print("waiting:", x)
start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print(task)
loop.run_until_complete(task)
print(task)
print("Time:",now()-start)
结果为：
<Task pending coro=<do_some_work() running at /app/py_code/study_asyncio/simple_ex2.py:13>>
waiting: 2
<Task finished coro=<do_some_work() done, defined at /app/py_code/study_asyncio/simple_ex2.py:13> result=None>
Time: 0.0003514289855957031
创建task后，在task加入事件循环之前为pending状态，当完成后，状态为finished
关于上面通过loop.create_task(coroutine)创建task,同样的可以通过 asyncio.ensure_future(coroutine)创建task
关于这两个命令的官网解释： https://docs.python.org/3/library/asyncio-task.html#asyncio.ensure_future
asyncio.ensure_future(coro_or_future, *, loop=None)
Schedule the execution of a coroutine object: wrap it in a future. Return a Task object.
If the argument is a Future, it is returned directly

绑定回调，在task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
import time
import asyncio

now = lambda : time.time()
async def do_some_work(x):
    print("waiting:",x)
    return "Done after {}s".format(x)

def callback(future):
    print("callback:",future.result())

start = now()
coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
print(task)
task.add_done_callback(callback)
print(task)
loop.run_until_complete(task)
print("Time:", now()-start)
结果为：
<Task pending coro=<do_some_work() running at /app/py_code/study_asyncio/simple_ex3.py:13>>
<Task pending coro=<do_some_work() running at /app/py_code/study_asyncio/simple_ex3.py:13>
    cb=[callback() at /app/py_code/study_asyncio/simple_ex3.py:18]>
waiting: 2
callback: Done after 2s
Time: 0.00039196014404296875
  通过add_done_callback方法给task任务添加回调函数，当task（也可以说是coroutine）执行完成的时候,就会调用回调函数。
并通过参数future获取协程执行的结果。这里我们创建 的task和回调里的future对象实际上是同一个对象


★★★简述gevent模块（单线程高并发）？
上下文切换：当CPU从执行一个线程切换到执行另外一个线程的时候，它需要先存储当前线程的本地的数据，程序指针等，
           然后载入另一个线程的本地数据，程序指针等，最后才开始执行。这种切换称为“上下文切换”(“context switch”)
　　　　　　CPU会在一个上下文中执行一个线程，然后切换到另外一个上下文中执行另外一个线程,上下文切换并不廉价。如果没有必要，应该减少上下文切换的发生

进程: 一个程序需要运行所需的资源的集合
每个进程数据是独立的
每个进程里至少有一个线程
每个进程里有可以多有个线程
线程数据是共享的
进程间共享数据的代价是高昂的,所以要尽量避免进程间的数据共享
线程间的数据本来就是共享的
线程要修改同一份数据，必须加锁，互斥锁mutex
生产者消费者:1.解耦2.提高程序的运行效率,把中间等待的时间省去

多线程场景: IO密集型，因为IO操作基本不占用CPU，所以多用在web，爬虫，socket交互
多进程场景:CPU密集型,大数据分析,金融分析,这样用的IO就很少，因为这个进程会进行大量的运算, 但是如果切换了进程,就会变慢

协程:微线程, 协程是一种用户态的轻量级线程,CPU不知道它的存在,
协程拥有自己的寄存器上下文和栈.协程调度切换时,将寄存器上下文和栈保存到其他地方,在切回来的时候,恢复先前保存的寄存器上下文和栈，
因此协程能保留上一次调用时的状态(即所有局部状态的一个特定组合,)，每次过程重入时,就相当于上一次调用的状态, 也就是进入上一次离开时所处逻辑流的位置

协程的好处：(是程序级别切换，CPU是不知道的.)
1.无需线程上下文切换,
2.无需原子操作锁定及同步开销 ,什么是原子操作？：是不需要同步的!!,是指不会被线程调度打断的操作；
                                            这种操作一旦开始，就运行到结束,中间不会有任何  context switch（切换到另一个线程,）
　　　　　　　　　　　　　　　　　　　　　　　　原子操作可以是一个步骤，也可以是多个操作步骤，但是其顺序是不可以被打乱，或者切割掉只执行部分。
                                            视作整体是原子性的核心
3.方便切换控制流,简化编程模型
4.高并发 + 高扩展 + 低成本：一个CPU支持上万的协程都不是问题,所以很适合用于高并发处理
坏处-----:
  1.无法利用多核资源,协程的本质是个单线程,它不能同时将单个CPU的多个核用上, 协程需要配合进程才能在多CPU上，  适用于CPU密集型应用
  2.进程阻塞 （Blocking）  操作 如IO操作时，会阻塞掉整个程序
----什么条件符合才能称之为协程？
　　A.必须在只有一个单线程里实现并发
　　B.修改共享数据不需要加锁
　　C.用户程序里自己保持多个控制流的上下文栈
　　D.一个协程遇到IO操作自动切换到其他协程！！！！！！
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet,
它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。  
详细链接：https://www.cnblogs.com/zcqdream/p/6196040.html


twisted框架的使用和应用？
Twisted 官方说，“ Twisted is an event-driven networking framework ”。
Twisted 对event 的管理机制，可划分为后台和前台两种形式。
后台的管理，是Twisted 框架的内在机制，自动运行，对程序员透明无须干预，在程序文本中不见其踪迹。
前台的管理，是Twisted 授权程序员，在程序文本中显式写码来实现。程序员的工作，主要是按照既定的方式，实现 event。
我们所关心、所用到的，是这部分东西（API）。 
Twisted 众多的 event，分门别类、层次有序。前台管理中，有两个特别的 object，一个叫 reactor ，另一个叫defered。
特别之处，在于它俩起着“事件管理器”的作用。下面，说说它俩。 

统领全局的 reactor 
在 Twisted 应用中，reactor 的任务是为程序运行建立必须的全局循环（event loop），所起的作用，相当于 Python 应用中的 MainLoop()。
reactor 的用法很简单，一般只用两个：reactor.run() 启动全局循环，reactor.stop() 停止全局循环（程序终止）。 
如果程序中没有调用reactor.stop() 的语句，程序将处于死循环，可以按键 Ctrl-C 强制退出。 
下面是一个例子： 
from twisted.internet import reactor 
import time 

def printTime( ): 
  print "Current time is", time.strftime("%H:%M:%S") 
def stopReactor( ): 
  print "Stopping reactor" 
  reactor.stop( ) 
  reactor.callLater(1, printTime) 
#定时器，1秒钟后调用printTime() 
  reactor.callLater(2, printTime) 
  reactor.callLater(3, printTime) 
  reactor.callLater(5, stopReactor) 
#定时器，5秒钟后调用stopReactor() 
  print "Running the reactor..." 
  reactor.run( ) 
  print "Reactor stopped." 

提升效率的 defferred 
这个“异步”功能的代表就是 defferred。 
当然，defferred “异步”功能的实现，与多线程完全不同，具有以下特点： 
１、defferred 产生的 event，是函数调用返回的对象； 
２、defferred 代表一个连接任务，负责报告任务执行的延迟情况和最终结果； 
３、对defferred 的操作，通过预定的“事件响应器”（event handler）进行。 
有了defferred，即可对任务的执行进行管理控制。防止程序的运行，由于等待某项任务的完成而陷入阻塞停滞，提高整体运行的效率。 
建议只关注黑体字的语句，它们反映了defferred的用法。涉及的两个class，是Twisted建立网络连接的固定套路，后面会专门说它。 
# connectiontest.py 
from twisted.internet import reactor, defer, protocol 
class CallbackAndDisconnectProtocol(protocol.Protocol): 
# Twisted建立网络连接的固定套路 
def connectionMade(self): 
  self.factory.deferred.callback("Connected!") 
# “事件响应器”handleSuccess对此事件作出处理 
  self.transport.loseConnection( ) 
class ConnectionTestFactory(protocol.ClientFactory): 
# Twisted建立网络连接的固定套路 
  protocol = CallbackAndDisconnectProtocol 
def __init__(self): 
  self.deferred = defer.Deferred( ) 
# 报告发生了延迟事件，防止程序阻塞在这个任务上 
  def clientConnectionFailed(self, connector, reason): 
  self.deferred.errback(reason) 
# “事件响应器”handleFailure对此事件作出处理 

def testConnect(host, port): 
  testFactory = ConnectionTestFactory( ) 
  reactor.connectTCP(host, port, testFactory) 
  return testFactory.deferred 
# 返回连接任务的deferred 
def handleSuccess(result, port): 
# deferred“事件响应器”：连接任务完成的处理 
  print "Connected to port %i" % port 
  reactor.stop( ) 
def handleFailure(failure, port): 
# deferred“事件响应器”：连接任务失败的处理 
  print "Error connecting to port %i: %s" % ( 
  port, failure.getErrorMessage( )) 
  reactor.stop( ) 
if __name__ == "__main__": 
  import sys 
  if not len(sys.argv) == 3: 
    print "Usage: connectiontest.py host port" 
  sys.exit(1) 
  host = sys.argv[1] 
  port = int(sys.argv[2]) 
  connecting = testConnect(host, port) 
# 调用函数，返回deferred 
  connecting.addCallback(handleSuccess, port) 
# 建立deferred“事件响应器” 
  connecting.addErrback(handleFailure, port) 
# 建立deferred“事件响应器” 
  reactor.run( )
'''
