## redis中数据库默认是多少个db 及作用？  
redis下，数据库是由一个整数索引标识，而不是由一个数据库名称。默认情况下，一个客户端连接到数据库0。  
redis配置文件中下面的参数来控制数据库总数：  
/etc/redis/redis.conf  
文件中，有个配置项 databases = 16 //默认有16个数据库

## python操作redis的模块？
```
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
#host是redis主机需要redis服务端和客户端都启动 redis默认端口是6379

r = redis.Redis(connection_pool=pool)
r.set('food', 'mutton', ex=3) #key是"food" value是"mutton" 将键值对存入redis缓存
#ex，过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None

print(r.get('food'))  #mutton 取出键food对应的值
```

##  hash， set，zset，list 中存储过多的元素
以hash为例，原先的正常存取流程是  hget(hashKey, field) ; hset(hashKey, field, value) 
现在，固定一个桶的数量，比如 10000， 每次存取的时候，先在本地计算field的hash值，模除 10000， 确定了该field落在哪个key上。
```
newHashKey  =  hashKey + (*hash*(field) % 10000）;   
hset (newHashKey, field, value) ;  
hget(newHashKey, field)
```

## redis主从复制原理  
从容量上，单个Redis服务器内存容量有限，就算一台Redis服务器内容容量为256G，  
也不能将所有内容用作Redis存储内存，一般来说，单台Redis最大使用内存不应该超过20G。  
### 原理
1、Slave启动成功连接到master后会发送一个sync命令；  
2、Master接到命令启动后的存盘进程，同时收集所有接收到的用于修改数据集命令，在后台进程执行完毕之后，master将传送整个数据文件到slave，以完成一次完全同步；  
3、全量复制：而slave服务在数据库文件数据后，将其存盘并加载到内存中；  
4、增量复制：Master继续将新的所有收集到的修改命令依次传给slave，完成同步；  
5、但是只要是重新连接master，一次完全同步（全量复制）将被自动执行。  
### 哨兵模式（sentinel）
反客为主的自动版，能够后台监控Master库是否故障，如果故障了根据投票数自动将slave库转换为主库。一组sentinel能同时监控多个Master    
使用步骤：  
1、在Master对应redis.conf同目录下新建sentinel.conf文件，名字绝对不能错；  
2、配置哨兵，在sentinel.conf文件中填入内容：  
sentinel monitor 被监控数据库名字（自己起名字） ip port 1  
说明：上面最后一个数字1，表示主机挂掉后slave投票看让谁接替成为主机，得票数多少后成为主机。    
### 启动哨兵模式
命令键入：redis-sentinel /myredis/sentinel.conf  
注：上述sentinel.conf路径按各自实际情况配置  
复制的缺点：  
延时，由于所有的写操作都是在Master上操作，然后同步更新到Slave上，所以从Master同步到Slave机器有一定  
的延迟，当系统很繁忙的时候，延迟问题会更加严重，Slave机器数量的增加也会使得这个问题更加严重。  
### 乐观复制
Redis采用了复制的策略。容忍在一定时间内主从数据库的内容是不同的，但是两者的数据最终会保持一致。  

具体来说，Redis主从数据库之间的复制数据的过程本身是异步的，这意味着，主数据库执行完客户端的写请求后会立即将命令在主数据库的执行结果返回给客户端，而不会等待从数据库收到该命令后再返回给客户端。  
这一特性保证了复制后主从数据库的性能不会受到影响，但另一方面也会产生一个主从数据库数据不一致的时间窗口，当主数据库执行一条写命令之后，主数据库的数据已经发生变动，然而在主数据库将该命令传送给从数据库之前，如果两个数据库之间的连接断开了，此时二者间的数据就不一致了。  
从这个角度看，主数据库无法得知命令最终同步给了几个从数据库，不过Redis提供了两个配置选项来限制只有至少同步给指定数量的数据库时，主数据库才是可写的：  
min-slaves-to-write 3  
min-slave2-max-lag 10  
第一个参数表示只有当3个或3个以上的从数据库连接到主库时，主数据库才是可写的，否则返回错误。  
第二个参数表示允许从数据库失去连接的最长时间，该选项默认是关闭的，在分布式系统中，打开并合理配置该选项可以降低主从架构因为网络分区导致的数据不一致问题。  

## redis中的sentinel的作用
Redis-Sentinel是Redis官方推荐的高可用性(HA)解决方案，当用Redis做Master-slave的高可用方案时，  
假如master宕机了，Redis本身(包括它的很多客户端)都没有实现自动进行主备切换，  
而Redis-sentinel本身也是一个独立运行的进程，它能监控多个master-slave集群，发现master宕机后能进行自动切换  
### 主要功能
1.不时地监控redis是否按照预期良好地运行;  
2.如果发现某个redis节点运行出现状况，能够通知另外一个进程(例如它的客户端);  
3.能够进行自动切换。当一个master节点不可用时，能够选举出master的多个slave  
(如果有超过一个slave的话)中的一个来作为新的master,其它的slave节点会将它所追随的master的地址改为被提升为master的slave的新地址。

## 如何实现redis集群?
### 客户端分片
客户端分片是把分片的逻辑放在Redis客户端实现，通过Redis客户端预先定义好的路由规则，把对Key的访问转发到不同的Redis实例中，最后把返回结果汇集.  
客户端分片方案有下面这些缺点：  
　　●这是一种静态的分片方案，需要增加或者减少Redis实例的数量，需要手工调整分片的程序。  
　　●可运维性差，集群的数据出了任何问题都需要运维人员和开发人员一起合作，减缓了解决问题的速度，增加了跨部门沟通的成本。  
　　●在不同的客户端程序中，维护相同的分片逻辑成本巨大。
### Twemproxy
Twemproxy是由Twitter开源的Redis代理，其基本原理是：Redis客户端把请求发送到Twemproxy，  
Twemproxy根据路由规则发送到正确的Redis实例，最后Twemproxy把结果汇集返回给客户端。  
Twemproxy的优点如下：  
　　●客户端像连接Redis实例一样连接Twemproxy，不需要改任何的代码逻辑。  
　　●支持无效Redis实例的自动删除。  
　　●Twemproxy与Redis实例保持连接，减少了客户端与Redis实例的连接数。  
Twemproxy的缺点如下：  
　　●由于Redis客户端的每个请求都经过Twemproxy代理才能到达Redis服务器，这个过程中会产生性能损失。  
　　●没有友好的监控管理后台界面，不利于运维监控。  
　　●最大的问题是Twemproxy无法平滑地增加Redis实例。对于运维人员来说，当因为业务需要增加Redis实例时工作量非常大。  
Twemproxy作为最被广泛使用、最久经考验、稳定性最高的Redis代理，在业界被广泛使用。  
### Redis 3.0集群
Redis 3.0集群采用了P2P的模式，完全去中心化。Redis把所有的Key分成了16384个slot，  
每个Redis实例负责其中一部分slot。集群中的所有信息（节点、端口、slot等），都通过节点之间定期的数据交换而更新。
工作流程如下：  
　　（1） Redis客户端在Redis2实例上访问某个数据。  
　　（2） 在Redis2内发现这个数据是在Redis3这个实例中，给Redis客户端发送一个重定向的命令。  
　　（3） Redis客户端收到重定向命令后，访问Redis3实例获取所需的数据。  
  Redis 3.0的集群方案有以下两个问题：  
　　●一个Redis实例具备了“数据存储”和“路由重定向”，完全去中心化的设计。  
      这带来的好处是部署非常简单，直接部署Redis就行，不像Codis有那么多的组件和依赖。  
      但带来的问题是很难对业务进行无痛的升级，如果哪天Redis集群出了什么严重的Bug，就只能回滚整个Redis集群。    
　　●对协议进行了较大的修改，对应的Redis客户端也需要升级。  
      升级Redis客户端后谁能确保没有Bug？而且对于线上已经大规模运行的业务，升级代码中的Redis客户端也是一个很麻烦的事情。  
