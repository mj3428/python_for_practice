## redis中数据库默认是多少个db 及作用？  
redis下，数据库是由一个整数索引标识，而不是由一个数据库名称。默认情况下，一个客户端连接到数据库0。  
redis配置文件中下面的参数来控制数据库总数：  
/etc/redis/redis.conf  
文件中，有个配置项 databases = 16 //默认有16个数据库

## python操作redis的模块？
```
import redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)#host是redis主机需要redis服务端和客户端都启动 redis默认端口是6379
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
```
