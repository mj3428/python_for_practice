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
