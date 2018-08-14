'''
1. OSI七层和TCP/IP四层的关系
1.1 OSI引入了服务、接口、协议、分层的概念，TCP/IP借鉴了OSI的这些概念建立TCP/IP模型。
1.2 OSI先有模型，后有协议，先有标准，后进行实践；而TCP/IP则相反，先有协议和应用再提出了模型，且是参照的OSI模型。
1.3 OSI是一种理论下的模型，而TCP/IP已被广泛使用，成为网络互联事实上的标准。
TCP：transmission control protocol 传输控制协议
UDP：user data protocol 用户数据报协议
七层：应用层（Application）、表示层（Presentation）、会话层（Session）、传输层（Transport）
      网络层（Network）、数据链路层（Data Link）、物理层（Physical）
七层结构记忆方法：应、表、会、传、网、数、物
应用层协议需要掌握的是：HTTP（Hyper text transfer protocol）、FTP（file transfer protocol）、
                      SMTP（simple mail transfer rotocol）、POP3（post office protocol 3）、
                      IMAP4（Internet mail access protocol）

TCP/IP四层模型
应用层：对应OSI中的应用层、表示层、会话层
物理链路层：对应OSI中的数据链路层、物理层（也有叫网络接口层）


C/S架构和B/S架构？
C/S架构软件（即客户机/服务器模式）分为客户机和服务器两层：
第一层是在客户机系统上结合了表示与业务逻辑，第二层是通过网络结合了数据库服务器
简单的说就是第一层是用户表示层，第二层是数据库层。客户端和服务器直接相连，这两个组成部分都承担着重要的角色

C/S架构的优点
a. 客户端和服务器直接相连。点对点的连接方式更安全，可以直接操作本地文本，比较方便。
b. 客户端可以处理一些逻辑事务。可以进行数据处理和数据存储，提供一定的帮助。
c. 客户端直接操作界面。

3. C/S架构的缺点
a> C/S架构适用于局域网，对网速的要求比较高。
b> 客户端界面缺乏通用性，且当业务更改时就需要更改界面，重新编写。
c> 随着用户数量的增多，会出现通信拥堵、服务器响应速度慢等情况。
d> 系统的维护也比较麻烦

B/S架构
是C/S架构的一种改进，可以说属于三层C/S架构
第一层是浏览器（即客户端）只有简单的输入输出功能，处理极少部分的事务逻辑
第二层是WEB服务器，扮演着信息传送的角色
第三层是数据库服务器，它存放着大量的数据

2.B/S架构的优点
a> 浏览器和数据库服务器采用多对多的方式连接。因此适合在广域网里实现巨大的互联网，甚至是全球网，有着很强大的信息共享性。
b> 浏览器只处理一些简单的逻辑事务，负担小。
c> 数据都集中存放在数据库服务器，所以不存在数据不一致现象。
d> 随着服务器负载的增加，可以平滑地增加服务器的个数并建立集群服务器系统，然后在各个服务器之间做负载均衡。
e> B/S建立在广域网上，所以需要的网速要求不高。
f> 不需要安装客户端，只要能连上网，就能随时随地的浏览页面。
g> 能有效地保护数据平台和管理访问权限，确保服务器数据库的数据安全。

3. B/S架构的缺点
a> 服务器承担着重要的责任，数据负荷较重。一旦发生服务器“崩溃”等问题，后果不堪设想。
b> 页面需要不断地动态刷新，当用户增多时，网速会变慢。


简述三次握手、四次挥手的流程？

（1）序号：Seq序号，占32位，用来标识从TCP源端向目的端发送的字节流，发起方发送数据时对此进行标记。
（2）确认序号：Ack序号，占32位，只有ACK标志位为1时，确认序号字段才有效，Ack=Seq+1。
（3）标志位：共6个，即URG、ACK、PSH、RST、SYN、FIN等，具体含义如下：
       （A）URG：紧急指针（urgent pointer）有效。
       （B）ACK：确认序号有效。
       （C）PSH：接收方应该尽快将这个报文交给应用层。
       （D）RST：重置连接。
       （E）SYN：发起一个新连接。
       （F）FIN：释放一个连接。

需要注意的是：
（A）不要将确认序号Ack与标志位中的ACK搞混了。
（B）确认方Ack=发起方Req+1，两端配对。 

（1）第一次握手：
Client将标志位SYN置为1，随机产生一个值seq=J，并将该数据包发送给Server，Client进入SYN_SENT状态，等待Server确认。
（2）第二次握手：
Server收到数据包后由标志位SYN=1知道Client请求建立连接，
Server将标志位SYN和ACK都置为1，ack=J+1，随机产生一个值seq=K，
并将该数据包发送给Client以确认连接请求，Server进入SYN_RCVD状态。
（3）第三次握手：
Client收到确认后，检查ack是否为J+1，ACK是否为1，
如果正确则将标志位ACK置为1，ack=K+1，并将该数据包发送给Server，
Server检查ack是否为K+1，ACK是否为1，如果正确则连接建立成功，Client和Server进入ESTABLISHED状态，
完成三次握手，随后Client与Server之间可以开始传输数据了。

所谓四次挥手（Four-Way Wavehand）即终止TCP连接，就是指断开一个TCP连接时，
需要客户端和服务端总共发送4个包以确认连接的断开。
在socket编程中，这一过程由客户端或服务端任一方执行close来触发
第一次挥手：
Client发送一个FIN，用来关闭Client到Server的数据传送，Client进入FIN_WAIT_1状态。
第二次挥手：
Server收到FIN后，发送一个ACK给Client，确认序号为收到序号+1（与SYN相同，一个FIN占用一个序号），Server进入CLOSE_WAIT状态。
第三次挥手：
Server发送一个FIN，用来关闭Server到Client的数据传送，Server进入LAST_ACK状态。
第四次挥手：
Client收到FIN后，Client进入TIME_WAIT状态，接着发送一个ACK给Server，
确认序号为收到序号+1，Server进入CLOSED状态，完成四次挥手


ARP协议
ARP（Address Resolution Protocol）即地址解析协议，
用于实现从 IP 地址到 MAC 地址的映射，即询问目标IP对应的MAC地址；
在网络通信中，主机和主机通信的数据包需要依据OSI模型从上到下进行数据封装，当数据封装完整后，再向外发出
所以在局域网的通信中，不仅需要源目IP地址的封装，也需要源目MAC的封装
一般情况下，上层应用程序更多关心IP地址而不关心MAC地址，所以需要通过ARP协议来获知目的主机的MAC地址，完成数据封装
详细查找，里面包含图解https://www.cnblogs.com/csguo/p/7527303.html


TCP和UDP的区别？
TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接
TCP提供可靠的服务;UDP尽最大努力交付，即不保证可靠交付
UDP具有较好的实时性，工作效率比TCP高，适用于对高速传输和实时性有较高的通信或广播通信
每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信
TCP对系统资源要求较多，UDP对系统资源要求较少
TCP编程的服务器端一般步骤是： 
　1、创建一个socket，用函数socket()； SOCKET SocketListen =socket(AF_INET,SOCK_STREAM, IPPROTO_TCP);
　2、设置socket属性，用函数setsockopt(); * 可选 
　3、绑定IP地址、端口等信息到socket上，用函数bind(); SOCKET_ERROR = bind(SocketListen,(const sockaddr*)&addr,sizeof(addr))
　4、开启监听，用函数listen()；   SOCKET_ERROR == listen(SocketListen,2)
　5、接收客户端上来的连接，用函数accept()； SOCKET SocketWaiter = accept(SocketListen,_Out_struct sockaddr *addr_Inout_  int *addrlen);
　6、收发数据，用函数send()和recv()，或者read()和write(); 
　7、关闭网络连接； closesocket(SocketListen);closesocket(SocketWaiter);
　8、关闭监听；
UDP编程的服务器端一般步骤是： 
　1、创建一个socket，用函数socket()； 
　2、设置socket属性，用函数setsockopt();* 可选 
　3、绑定IP地址、端口等信息到socket上，用函数bind(); 
　4、循环接收数据，用函数recvfrom(); 
　5、关闭网络连接；
 

局域网与广域网
内网：即所说的局域网，比如学校的局域网，局域网内每台计算机的IP地址在本局域网内具有互异性，是不可重复的。但两个局域网内的内网IP可以有相同的
外网：即互联网，局域网通过一台服务器或是一个路由器对外连接的网络，这个IP地址是惟一的
一个局域网里所有电脑的内网IP是互不相同的,但共用一个外网IP
当你家里买了两台电脑，你想组建一个局域网，你除了要用网线和路由器等设备将两台电脑相连，
你还要将两台电脑设置固定IP，比如电脑A设为192.168.1.2，电脑B设为192.168.1.3，
这样你就可以用这两个IP地址互相访问两台电脑，但这两个IP地址只在这两台电脑间有效，对外网无效

内网IP是以下面几个段开头的IP.用户可以自己设置.常用的内网IP地址: 
10.x.x.x 
172.16.x.x至172.31.x.x 
192.168.x.x 


为何基于tcp协议的通信比基于udp协议的通信更可靠
tcp:可靠 对方给了确认收到信息，才发下一个，如果没收到确认信息就重发


什么是socket？简述基于tcp协议的套接字通信流程
Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。 socket == 片面说: ip + 端口
    服务端：socket(),bind(),listen(),accept(),recv(),send(),close()
    客户端：socket(),connect(),send(),recv(),close()
    
    
什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？
    粘包：数据粘在一起，主要因为：接收方不知道消息之间的界限，不知道一次性提取多少字节的数据造成的
    数据量比较小，时间间隔比较短，就合并成了一个包，这是底层的一个优化算法（Nagle算法）
    
    
I/O多路复用？
等待数据准备好（waiting for data to be ready）。对于一个套接口上的操作，这一步骤关系到数据从网络到达，并将其复制到内核的某个缓冲区。
将数据从内核缓冲区复制到进程缓冲区（copying the data from the kernel to the process）
IO多路复用是指内核一旦发现进程指定的一个或者多个IO条件准备读取，它就通知该进程
   （1）当客户处理多个描述字时（一般是交互式输入和网络套接口），必须使用I/O复用。
   （2）当一个客户同时处理多个套接口时，而这种情况是可能的，但很少出现。
   （3）如果一个TCP服务器既要处理监听套接口，又要处理已连接套接口，一般也要用到I/O复用。
   （4）如果一个服务器即要处理TCP，又要处理UDP，一般要使用I/O复用。
   （5）如果一个服务器要处理多个服务或多个协议，一般要使用I/O复用。
与多进程和多线程技术相比，I/O多路复用技术的最大优势是系统开销小，系统不必创建进程/线程


select、poll、epoll 模型的区别？
