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

select:                    
相关链接：http://www.cnblogs.com/Anker/archive/2013/08/14/3258674.html

该函数准许进程指示内核等待多个事件中的任何一个发送，并只在有一个或多个事件发生或经历一段指定的时间后才唤醒。
函数原型如下：
#include <sys/select.h>
#include <sys/time.h>
int select(int maxfdp1,fd_set *readset,fd_set *writeset,fd_set *exceptset,const struct timeval *timeout)
返回值：就绪描述符的数目，超时返回0，出错返回-1

函数参数介绍如下：
（1）第一个参数maxfdp1指定待测试的描述字个数，它的值是待测试的最大描述字加1（因此把该参数命名为maxfdp1），
    描述字0、1、2...maxfdp1-1均将被测试。因为文件描述符是从0开始的。
（2）中间的三个参数readset、writeset和exceptset指定我们要让内核测试读、写和异常条件的描述字。
如果对某一个的条件不感兴趣，就可以把它设为空指针。
struct fd_set可以理解为一个集合，这个集合中存放的是文件描述符，可通过以下四个宏进行设置：
          void FD_ZERO(fd_set *fdset);           //清空集合
          void FD_SET(int fd, fd_set *fdset);   //将一个给定的文件描述符加入集合之中
          void FD_CLR(int fd, fd_set *fdset);   //将一个给定的文件描述符从集合中删除
          int FD_ISSET(int fd, fd_set *fdset);   // 检查集合中指定的文件描述符是否可以读写 
（3）timeout告知内核等待所指定描述字中的任何一个就绪可花多少时间。其timeval结构用于指定这段时间的秒数和微秒数。
         struct timeval{
                   long tv_sec;   //seconds
                   long tv_usec;  //microseconds
                        };
这个参数有三种可能：
（1）永远等待下去：仅在有一个描述字准备好I/O时才返回。为此，把该参数设置为空指针NULL。
（2）等待一段固定时间：在有一个描述字准备好I/O时返回，但是不超过由该参数所指向的timeval结构中指定的秒数和微秒数。
（3）根本不等待：检查描述字后立即返回，这称为轮询。为此，该参数必须指向一个timeval结构，而且其中的定时器值必须为0。

poll:              
相关链接：http://www.cnblogs.com/Anker/archive/2013/08/15/3261006.html

poll的机制与select类似，与select在本质上没有多大差别，管理多个描述符也是进行轮询
根据描述符的状态进行处理，但是poll没有最大文件描述符数量的限制
poll和select同样存在一个缺点就是，包含大量文件描述符的数组被整体复制于用户态和内核的地址空间之间，
而不论这些文件描述符是否就绪，它的开销随着文件描述符数量的增加而线性增大

函数格式如下所示：
# include <poll.h>
int poll ( struct pollfd * fds, unsigned int nfds, int timeout);

pollfd结构体定义如下：
struct pollfd {
int fd;         /* 文件描述符 */
short events;         /* 等待的事件 */
short revents;       /* 实际发生了的事件 */
} ; 
每一个pollfd结构体指定了一个被监视的文件描述符，可以传递多个结构体，指示poll()监视多个文件描述符。
每个结构体的events域是监视该文件描述符的事件掩码，由用户来设置这个域。revents域是文件描述符的操作结果事件掩码，内核在调用返回时设置这个域。
events域中请求的任何事件都可能在revents域中返回。合法的事件如下：
    POLLIN 　　　　　　　　有数据可读。
　　POLLRDNORM 　　　　  有普通数据可读。
　　POLLRDBAND　　　　　 有优先数据可读。
　　POLLPRI　　　　　　　　 有紧迫数据可读。
　　POLLOUT　　　　　　      写数据不会导致阻塞。
　　POLLWRNORM　　　　　  写普通数据不会导致阻塞。
　　POLLWRBAND　　　　　   写优先数据不会导致阻塞。
　　POLLMSGSIGPOLL 　　　　消息可用。
　　此外，revents域中还可能返回下列事件：
　　POLLER　　   指定的文件描述符发生错误。
　　POLLHUP　　 指定的文件描述符挂起事件。
　　POLLNVAL　　指定的文件描述符非法。
这些事件在events域中无意义，因为它们在合适的时候总是会从revents中返回。
　使用poll()和select()不一样，你不需要显式地请求异常情况报告。
　POLLIN | POLLPRI等价于select()的读事件，POLLOUT |POLLWRBAND等价于select()的写事件。
  POLLIN等价于POLLRDNORM |POLLRDBAND，而POLLOUT则等价于POLLWRNORM。
  例如，要同时监视一个文件描述符是否可读和可写，我们可以设置 events为POLLIN |POLLOUT。
  在poll返回时，我们可以检查revents中的标志，对应于文件描述符请求的events结构体。
  如果POLLIN事件被设置，则文件描述符可以被读取而不阻塞。
  如果POLLOUT被设置，则文件描述符可以写入而不导致阻塞。
  这些标志并不是互斥的：它们可能被同时设置，表示这个文件描述符的读取和写入操作都会正常返回而不阻塞。
　timeout参数指定等待的毫秒数，无论I/O是否准备好，poll都会返回。timeout指定为负数值表示无限超时，使poll()一直挂起直到一个指定事件发生；
  timeout为0指示poll调用立即返回并列出准备好I/O的文件描述符，但并不等待其它的事件。这种情况下，poll()就像它的名字那样，一旦选举出来，立即返回。
　返回值和错误代码
　　成功时，poll()返回结构体中revents域不为0的文件描述符个数；如果在超时前没有任何事件发生，poll()返回0；
    失败时，poll()返回-1，并设置errno为下列值之一：
　　EBADF　　       一个或多个结构体中指定的文件描述符无效。
　　EFAULTfds　　 指针指向的地址超出进程的地址空间。
　　EINTR　　　　  请求的事件之前产生一个信号，调用可以重新发起。
　　EINVALnfds　　参数超出PLIMIT_NOFILE值。
　　ENOMEM　　     可用内存不足，无法完成请求。
  
epoll:
相关链接：http://www.cnblogs.com/Anker/archive/2013/08/17/3263780.html

epoll是在2.6内核中提出的，是之前的select和poll的增强版本。
相对于select和poll来说，epoll更加灵活，没有描述符限制。
epoll使用一个文件描述符管理多个描述符，将用户关系的文件描述符的事件存放到内核的一个事件表中，这样在用户空间和内核空间的copy只需一次。

epoll操作过程需要三个接口，分别如下：
#include <sys/epoll.h>
int epoll_create(int size);
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
（1） int epoll_create(int size);
　创建一个epoll的句柄，size用来告诉内核这个监听的数目一共有多大。这个参数不同于select()中的第一个参数，给出最大监听的fd+1的值。
  需要注意的是，当创建好epoll句柄后，它就是会占用一个fd值，在linux下如果查看/proc/进程id/fd/，
  是能够看到这个fd的，所以在使用完epoll后，必须调用close()关闭，否则可能导致fd被耗尽。

（2）int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
　　 epoll的事件注册函数，它不同与select()是在监听事件时告诉内核要监听什么类型的事件epoll的事件注册函数，
    它不同与select()是在监听事件时告诉内核要监听什么类型的事件，而是在这里先注册要监听的事件类型。
    第一个参数是epoll_create()的返回值，第二个参数表示动作，用三个宏来表示：
EPOLL_CTL_ADD：注册新的fd到epfd中；
EPOLL_CTL_MOD：修改已经注册的fd的监听事件；
EPOLL_CTL_DEL：从epfd中删除一个fd；
第三个参数是需要监听的fd，第四个参数是告诉内核需要监听什么事，struct epoll_event结构如下：
struct epoll_event {
  __uint32_t events;  /* Epoll events */
  epoll_data_t data;  /* User data variable */
};
events可以是以下几个宏的集合：
EPOLLIN ：表示对应的文件描述符可以读（包括对端SOCKET正常关闭）；
EPOLLOUT：表示对应的文件描述符可以写；
EPOLLPRI：表示对应的文件描述符有紧急的数据可读（这里应该表示有带外数据到来）；
EPOLLERR：表示对应的文件描述符发生错误；
EPOLLHUP：表示对应的文件描述符被挂断；
EPOLLET： 将EPOLL设为边缘触发(Edge Triggered)模式，这是相对于水平触发(Level Triggered)来说的。
EPOLLONESHOT：只监听一次事件，当监听完这次事件之后，如果还需要继续监听这个socket的话，需要再次把这个socket加入到EPOLL队列里
（3） int epoll_wait(int epfd, struct epoll_event * events, int maxevents, int timeout);
　    等待事件的产生，类似于select()调用。参数events用来从内核得到事件的集合，maxevents告之内核这个events有多大，
      这个maxevents的值不能大于创建epoll_create()时的size，参数timeout是超时时间（毫秒，0会立即返回，-1将不确定，也有说法说是永久阻塞）。
      该函数返回需要处理的事件数目，如返回0表示已超时。
epoll对文件描述符的操作有两种模式：LT（level trigger）和ET（edge trigger）。LT模式是默认模式，LT模式与ET模式的区别如下：

　　LT模式：当epoll_wait检测到描述符事件发生并将此事件通知应用程序，应用程序可以不立即处理该事件。
           下次调用epoll_wait时，会再次响应应用程序并通知此事件。

　　ET模式：当epoll_wait检测到描述符事件发生并将此事件通知应用程序，应用程序必须立即处理该事件。
           如果不处理，下次调用epoll_wait时，不会再次响应应用程序并通知此事件。
ET模式在很大程度上减少了epoll事件被重复触发的次数，因此效率要比LT模式高。
epoll工作在ET模式的时候，必须使用非阻塞套接口，以避免由于一个文件句柄的阻塞读/阻塞写操作把处理多个文件描述符的任务饿死。
'''
